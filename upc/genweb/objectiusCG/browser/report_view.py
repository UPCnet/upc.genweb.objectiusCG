from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_parent

class StateReportView(BrowserView):
    
    render = ViewPageTemplateFile("templates/state_report_view.pt")
    objectiusCG_portal_types = ('ObjectiuGeneral','ObjectiuEspecific','Accio','Activitat',)
    
    def __init__(self,context, request):
        self.context = context
        self.request = request
        
    def test(self, bool, yes, no):
        if bool:
            return yes
        else:
            return no
    
    def getActivitatByState(self, state=None):
        import string
        
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        contentFilter={}
        
        cur_path = '/'.join(self.context.getPhysicalPath())
        contentFilter['portal_type']="Activitat"
        if state is not None:
            contentFilter['review_state']=[state]
        if self.request.get('state'):
            if self.request.get('state') == 'Completa':
                contentFilter['review_state']=''
            if self.request.get('state') != 'Completa':
                st = self.request.get('state')
                contentFilter['review_state'] = string.lower(st)
        contentFilter['path']= cur_path

        contentFilter['sort_on']='getObjPositionInParent'

        return portal_catalog.searchResults(contentFilter)
    
    def getActivitatAcquisitionChain(self,state=None):
        
        activitats = self.getActivitatByState(state)
        
        data = []
        for activitat in activitats:
            obj = activitat.getObject()
            accion = aq_parent(aq_inner(obj))
            obj_esp = aq_parent(aq_inner(accion))
            obj_gen = aq_parent(aq_inner(obj_esp))
            data.append({'obj_gen':obj_gen, 'obj_esp':obj_esp, 'accio':accio, 'activitat':obj})
            
        return data
    
    def getResults(self, pt_type, path_id=None):
        
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        if path_id is None:
            cur_path = '/'.join(self.context.getPhysicalPath())
        else:
            cur_path = "%s/%s" % ('/'.join(self.context.getPhysicalPath()), path_id)
            
        contentFilter={}
        contentFilter['portal_type']=pt_type
        contentFilter['path']= cur_path
        contentFilter['sort_on']='getObjPositionInParent'
        
        return portal_catalog.searchResults(contentFilter)
