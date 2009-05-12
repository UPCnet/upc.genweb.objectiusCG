## Script (Python) "do_send_mail_rconsellg"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=Registered
##

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _

REQUEST = context.REQUEST

correu_rconsellg = context.getCorreu_RCG()

texte_correu = REQUEST.get('texte_del_miss','')

if correu_rconsellg:
    subject_text = """Notificaci�"""
    
    mail_text =  texte_correu + """\n\n""" + context.absolute_url()

    try:
        context.send_mail(mail_text, correu_rconsellg, subject_text)
        message = u'Correo enviat al Responsable del Consell de Govern'

    except:
            message = u'Error en el enviament del missatge. Comprovi la adreca electronique i torni a intentar-ho.'

else:
	message = u'Adre�a incorrecte.'


context.plone_utils.addPortalMessage(_(message))

return state
