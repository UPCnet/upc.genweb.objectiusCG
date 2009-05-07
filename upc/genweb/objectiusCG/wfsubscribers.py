# -*- coding: utf-8 -*-
#
# File: wfsubscribers.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


##code-section module-header #fill in your manual code here
##/code-section module-header


def notificar(obj, event):
    """generated workflow subscriber."""
    # do only change the code section inside this function.
    if not event.transition \
       or event.transition.id not in ['finalitzar'] \
       or obj != event.object:
        return
    ##code-section notificar #fill in your manual code here

    #obtenir dades consultor
    #pw = obj.portal_workflow
    #st = pw.getStatusOf("diagnostico_workflow", obj)
    #mt = getToolByName(obj, 'portal_membership')
    #member = mt.getMemberById(st['actor'])
    #nombre_consultor = member.getProperty('fullname')
    #email_consultor = member.getProperty('email')

    #obtenir mail notificacions
    #mt = getToolByName(obj, 'portal_membership')
    #notificacions = mt.getMemberById(obj.Creator())
    #mail_notificacions = notificacions.getProperty('email')
    mail_notificacions = obj.getCorreu_Notificacions()

    #construir i enviar correu
    host = obj.MailHost
    mail_text = """ From:%s
To: %s
Subject: Notificació
Content-Type: text/plain; charset=UTF-8

Aquest missatge és una notificació automàtica per comunicarli que l'Activitat: %s, ha finalitzat.

Salutacions.
""" % ('relay@upcnet.es',
   		mail_notificacions,
   		obj.absolute_url())

    host.send(mail_text)

    ##/code-section notificar


##code-section module-footer #fill in your manual code here
##/code-section module-footer

