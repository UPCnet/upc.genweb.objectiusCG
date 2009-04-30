# -*- coding: utf-8 -*-
#
# File: ObjectiuGeneralCG.py
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

ObjectiuGeneralCG_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ObjectiuGeneralCG(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IObjectiuGeneralCG)

    meta_type = 'ObjectiuGeneralCG'
    _at_rename_after_creation = True

    schema = ObjectiuGeneralCG_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(ObjectiuGeneralCG, PROJECTNAME)
# end of class ObjectiuGeneralCG

##code-section module-footer #fill in your manual code here
##/code-section module-footer



