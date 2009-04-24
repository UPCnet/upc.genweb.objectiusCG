# -*- coding: utf-8 -*-
#
# File: Activitat.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import ATDocumentSchema
from upc.genweb.objectiusCG.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='correu_RG',
        widget=StringField._properties['widget'](
            label='Correu_rg',
            label_msgid='objectiusCG_label_correu_RG',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),
    BooleanField('send_rg',
	default = False,
	widget=BooleanWidget(
		label = 'send',
		description = 'Check this box if want to send an e-mail to Correu_rg',
		i18n_domain='upc.genweb.objectiusCG',
	),
    ),
    StringField(
        name='correu_RCG',
        widget=StringField._properties['widget'](
            label='Correu_rcg',
            label_msgid='objectiusCG_label_correu_RCG',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),
    BooleanField('send_rcg',
	default = False,
	widget=BooleanWidget(
		label = 'send',
		description = 'Check this box if want to send an e-mail to Correu_rcg',
		i18n_domain='upc.genweb.objectiusCG',
	),
    ),
    StringField(
        name='correu_Notificacions',
        widget=StringField._properties['widget'](
            label='Correu_notificacions',
            label_msgid='objectiusCG_label_correu_Notificacions',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),
    BooleanField('send_notificacions',
	default = False,
	widget=BooleanWidget(
		label = 'send',
		description = 'Check this box if want to send an e-mail to Correu_notificacions',
		i18n_domain='upc.genweb.objectiusCG',
	),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Activitat_schema = ATDocumentSchema.copy() + \
    schema.copy()

Activitat_schema['text'].widget.visible={'edit':'invisible', 'view':'invisible'}


##code-section after-schema #fill in your manual code here

#atdocmodified = ATDocumentSchemacopy.copy()
#Activitat_schema = atdocmodified + \
#   schema.copy()


##/code-section after-schema

class Activitat(ATDocument):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IActivitat)

    meta_type = 'Activitat'
    _at_rename_after_creation = True

    schema = Activitat_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Activitat, PROJECTNAME)
# end of class Activitat

##code-section module-footer #fill in your manual code here
##/code-section module-footer



