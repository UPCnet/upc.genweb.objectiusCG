# -*- coding: utf-8 -*-
#
# File: ObjectiuEspecificCG.py
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

from upc.genweb.objectiusCG.config import *

##code-section module-header #fill in your manual code here
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
##/code-section module-header

schema = Schema((

    TextField(
        name='title',
        widget=TextAreaWidget(
            label='Title',
            label_msgid='objectiusCG_label_title',
            i18n_domain='upc.genweb.objectiusCG',
        ),
        required=1,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ObjectiuEspecificCG_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
ObjectiuEspecificCG_schema = BaseFolderSchema.copy() + ATContentTypeSchema.copy() + \
    schema.copy()
##/code-section after-schema

class ObjectiuEspecificCG(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IObjectiuEspecificCG)

    meta_type = 'ObjectiuEspecificCG'
    _at_rename_after_creation = True

    schema = ObjectiuEspecificCG_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(ObjectiuEspecificCG, PROJECTNAME)
# end of class ObjectiuEspecificCG

##code-section module-footer #fill in your manual code here
##/code-section module-footer



