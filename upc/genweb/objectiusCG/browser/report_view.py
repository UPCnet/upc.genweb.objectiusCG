from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_parent

class StateReportView(BrowserView):
    
    __call__ = ViewPageTemplateFile("templates/state_report_viewCG.pt")
    objectiusCG_portal_types = ('ObjectiuGeneralCG','ObjectiuEspecificCG','AccioCG','ActivitatCG',)
    
    allowed_states = ['no_iniciada','iniciada','finalitzada','totes']

    def __init__(self,context, request):
        self.context = context
        self.request = request
        
    def test(self, bool, yes, no):
        if bool:
            return yes
        else:
            return no

   
    def getResults(self, pt_type, path_id=None, state=None):
        
        state = self.request.get('state')

        portal_catalog = getToolByName(self.context, 'portal_catalog')

        if path_id is None:
            cur_path = '/'.join(self.context.getPhysicalPath())
        else:
            cur_path = "%s/%s" % ('/'.join(self.context.getPhysicalPath()), path_id)
        
        contentFilter={}

        contentFilter['portal_type']=pt_type
        contentFilter['path']= cur_path
        contentFilter['sort_on']='getObjPositionInParent'
        
        if pt_type == 'AccioCG':
            contentFilter['review_state'] = self.request.get('state')
            if state == 'totes':
                del(contentFilter['review_state'])

        return portal_catalog.searchResults(contentFilter)


    """
    def sendToFile(self):
        rows = ''

        objgens = self.getResults('ObjectiuGeneralCG')
        for objgen in objgens:
            rows = '%s%s\n' % (rows,'%s|||' % objgen.Title)
            objesps = self.getResults('ObjectiuEspecificCG',objgen.id)
            for objesp in objesps:
                rows = '%s%s\n' % (rows,'|%s||' % objesp.Title)
                
                accions = self.getResults('AccioCG',('%s/%s' %(objgen.id,objesp.id)))
                for accio in accions:
                    rows = '%s%s\n' % (rows,'||%s|' % accio.Title)
                    if self.request.get('ACCIO_ACT') == 'ACTIVITAT':

                        acts = self.getResults('ActivitatCG',('%s/%s/%s' %(objgen.id,objesp.id,accio.id)))
                        for act in acts:
                            rows = '%s%s\n' % (rows,'|||%s' % act.Title)

        self.request.RESPONSE.setHeader('content-disposition','filename=consulta.csv')
        self.request.RESPONSE.setHeader('Content-type','application/csv')
        
        return rows
    """
    def sendToFile(self):
        rows = ''

        objgens = self.getResults('ObjectiuGeneralCG')
        for objgen in objgens:
            rows = '%s%s\n' % (rows,'%s|||' % objgen.Title.replace('\r', '').replace('\n', '').replace('\t', ''))
            objesps = self.getResults('ObjectiuEspecificCG',objgen.id)
            for objesp in objesps:
                rows = '%s%s\n' % (rows,'|%s||' % objesp.Title.replace('\r', '').replace('\n', '').replace('\t', ''))
                
                accions = self.getResults('AccioCG',('%s/%s' %(objgen.id,objesp.id)))
                for accio in accions:
                    rows = '%s%s\n' % (rows,'||%s|' % accio.Title.replace('\r', '').replace('\n', '').replace('\t', ''))
                    if self.request.get('ACCIO_ACT') == 'ACTIVITAT':

                        acts = self.getResults('ActivitatCG',('%s/%s/%s' %(objgen.id,objesp.id,accio.id)))
                        for act in acts:
                            rows = '%s%s\n' % (rows,'|||%s' % act.Title.replace('\r', '').replace('\n', '').replace('\t', ''))

        self.request.RESPONSE.setHeader('content-disposition','filename=consulta.csv')
        self.request.RESPONSE.setHeader('Content-type','application/csv')
        
        return rows

    def buildInput(self,name=None):
        code = ''
        if name == 'state':
            if self.request.get('state') == 'no_iniciada':
                code = code+'<input type="radio" name="state" value="no_iniciada" checked="checked"/>&nbsp;No iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="iniciada"/>&nbsp;Iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="finalitzada"/>&nbsp;Finalitzada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="totes"/>&nbsp;Totes&nbsp;&nbsp;' 
            elif self.request.get('state') == 'iniciada':
                code = code+'<input type="radio" name="state" value="no_iniciada"/>&nbsp;No iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="iniciada" checked="checked"/>&nbsp;Iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="finalitzada"/>&nbsp;Finalitzada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="totes"/>&nbsp;Totes&nbsp;&nbsp;'                
            elif self.request.get('state') == 'finalitzada':
                code = code+'<input type="radio" name="state" value="no_iniciada"/>&nbsp;No iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="iniciada"/>&nbsp;Iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="finalitzada" checked="checked"/>&nbsp;Finalitzada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="totes"/>&nbsp;Totes&nbsp;&nbsp;' 
            elif self.request.get('state') == 'totes':
                code = code+'<input type="radio" name="state" value="no_iniciada"/>&nbsp;No iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="iniciada"/>&nbsp;Iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="finalitzada"/>&nbsp;Finalitzada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="totes" checked="checked"/>&nbsp;Totes&nbsp;&nbsp;'
            else:
                code = code+'<input type="radio" name="state" value="no_iniciada"/>&nbsp;No iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="iniciada"/>&nbsp;Iniciada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="finalitzada"/>&nbsp;Finalitzada&nbsp;&nbsp;'
                code = code+'<input type="radio" name="state" value="totes"/>&nbsp;Totes&nbsp;&nbsp;' 

        elif name == 'ACCIO_ACT':
            if self.request.get('ACCIO_ACT') == 'ACCIO':
                code = code+'<input type="radio" name="ACCIO_ACT" value="ACCIO" checked="checked"/>&nbsp;Acci&oacute; &nbsp;&nbsp;'
                code = code+'<input type="radio" name="ACCIO_ACT" value="ACTIVITAT"/>&nbsp;Activitat'
            elif self.request.get('ACCIO_ACT') == 'ACTIVITAT':
                code = code+'<input type="radio" name="ACCIO_ACT" value="ACCIO"/>&nbsp;Acci&oacute; &nbsp;&nbsp;'
                code = code+'<input type="radio" name="ACCIO_ACT" value="ACTIVITAT" checked="checked"/>&nbsp;Activitat'
            else:
                code = code+'<input type="radio" name="ACCIO_ACT" value="ACCIO"/>&nbsp;Acci&oacute; &nbsp;&nbsp;'
                code = code+'<input type="radio" name="ACCIO_ACT" value="ACTIVITAT"/>&nbsp;Activitat'

        elif name == 'display_mode':
            if self.request.get('display_mode') == 'Fitxer':
                code = code+'<input type="radio" name="display_mode" value="Pantalla"/>&nbsp;Pantalla&nbsp;&nbsp;'
                code = code+'<input type="radio" name="display_mode" value="Fitxer" checked="checked"/>&nbsp;Fitxer'
            else:
                code = code+'<input type="radio" name="display_mode" value="Pantalla" checked="checked"/>&nbsp;Pantalla&nbsp;&nbsp;'
                code = code+'<input type="radio" name="display_mode" value="Fitxer"/>&nbsp;Fitxer'
        else:
            code = code+'<input type="radio" name="state" value="no_iniciada"/>&nbsp;No iniciada&nbsp;&nbsp;'
            code = code+'<input type="radio" name="state" value="iniciada"/>&nbsp;Iniciada&nbsp;&nbsp;'
            code = code+'<input type="radio" name="state" value="finalitzada"/>&nbsp;Finalitzada&nbsp;&nbsp;'
            code = code+'<input type="radio" name="state" value="totes"/>&nbsp;Totes&nbsp;&nbsp;'

            code = code+'<input type="radio" name="ACCIO_ACT" value="ACCIO"/>&nbsp;Acci&oacute; &nbsp;&nbsp;'
            code = code+'<input type="radio" name="ACCIO_ACT" value="ACTIVITAT"/>&nbsp;Activitat'

            code = code+'<input type="radio" name="display_mode" value="Pantalla" checked="checked"/>&nbsp;Pantalla&nbsp;&nbsp;'
            code = code+'<input type="radio" name="display_mode" value="Fitxer"/>&nbsp;Fitxer'

        return code
