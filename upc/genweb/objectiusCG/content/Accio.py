# -*- coding: utf-8 -*-
#
# File: Accio.py
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

from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema
from upc.genweb.objectiusCG.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    LinesField(
        name='correuRG',
        widget=LinesField._properties['widget'](
            label='Correurg',
            label_msgid='objectiusCG_label_correuRG',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Accio_schema = ATFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Accio(ATFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IAccio)

    meta_type = 'Accio'
    _at_rename_after_creation = True

    schema = Accio_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Accio, PROJECTNAME)
# end of class Accio

##code-section module-footer #fill in your manual code here
##/code-section module-footer



