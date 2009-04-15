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

    TextField(
        name='descripcio_act',
        widget=TextAreaWidget(
            label='Descripcio_act',
            label_msgid='objectiusCG_label_descripcio_act',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),
    LinesField(
        name='correuRG',
        widget=LinesField._properties['widget'](
            label='Correurg',
            label_msgid='objectiusCG_label_correuRG',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),
    LinesField(
        name='correuRCG',
        widget=LinesField._properties['widget'](
            label='Correurcg',
            label_msgid='objectiusCG_label_correuRCG',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),
    LinesField(
        name='correuNotificacions',
        widget=LinesField._properties['widget'](
            label='Correunotificacions',
            label_msgid='objectiusCG_label_correuNotificacions',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Activitat_schema = ATDocumentSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
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



