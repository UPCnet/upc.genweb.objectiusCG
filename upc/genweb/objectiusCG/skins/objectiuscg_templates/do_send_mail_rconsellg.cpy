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
    mail_text = """ From:%s
To: %s
Subject: Notificacio
Content-Type: text/plain; charset=UTF-8

Enlace :%s 

%s
""" % ('realy@upcnet.es',
   		correu_rconsellg,
   		context.absolute_url(),
   		texte_correu)
    try:
        context.plone_log(mail_text)
        context.send_mail(mail_text)
        message = u'Correo enviat al Responsable del Consell de Govern'

    except:
            message = u'Error en el enviament del missatge: %s . Comprovi la adreca electronique i torni a intentar-ho.'

else:
	message = u'Adreca incorrecte.'


context.plone_utils.addPortalMessage(_(message))

return state
