# -*- coding: utf-8 -*-
#
# File: objectiusCG.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "upc.genweb.objectiusCG"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
ADD_CONTENT_PERMISSIONS = {
    'ActivitatCG': 'objectiusCG: Add ActivitatCG',
    'ObjectiuGeneralCG': 'objectiusCG: Add ObjectiuGeneralCG',
    'ObjectiuEspecificCG': 'objectiusCG: Add ObjectiuEspecificCG',
    'AccioCG': 'objectiusCG: Add AccioCG',
}

setDefaultRoles('objectiusCG: Add ActivitatCG', ('Manager','Owner'))
setDefaultRoles('objectiusCG: Add ObjectiuGeneralCG', ('Manager','Owner'))
setDefaultRoles('objectiusCG: Add ObjectiuEspecificCG', ('Manager','Owner'))
setDefaultRoles('objectiusCG: Add AccioCG', ('Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from upc.genweb.objectiusCG.AppConfig import *
except ImportError:
    pass
