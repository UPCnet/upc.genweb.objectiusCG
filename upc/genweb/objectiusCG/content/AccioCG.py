# -*- coding: utf-8 -*-
#
# File: AccioCG.py
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
    StringField(
        name='correu_RG',
        widget=StringField._properties['widget'](
            label="Adreca de correu del Responsable de Gestio",
            label_msgid='objectiusCG_label_correu_RG',
            i18n_domain='upc.genweb.objectiusCG',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

AccioCG_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class AccioCG(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IAccioCG)

    meta_type = 'AccioCG'
    _at_rename_after_creation = True

    schema = AccioCG_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    security.declarePublic('send_mail')
    def send_mail(self,mail,to,subject):
        """
        """
        host = self.MailHost

        result = host.secureSend(mail,
                                to.encode('UTF-8'),
                                'relay@upcnet.es'.encode('UTF-8'),
                                subject=subject,
                                subtype='plain',
                                charset='UTF-8',
                                debug=False,
                                From='relay@upcnet.es'.encode('UTF-8'))



registerType(AccioCG, PROJECTNAME)
# end of class AccioCG

##code-section module-footer #fill in your manual code here
##/code-section module-footer



