# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('objectiusCG: setuphandlers')
from upc.genweb.objectiusCG.config import PROJECTNAME
from upc.genweb.objectiusCG.config import DEPENDENCIES
import os
from Products.CMFCore.utils import getToolByName
import transaction
##code-section HEAD
from Products.CMFPlone.utils import _createObjectByType
##/code-section HEAD

def isNotobjectiusCGProfile(context):
    return context.readDataFile("objectiusCG_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotobjectiusCGProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()

def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotobjectiusCGProfile(context): return
    site = context.getSite()

    crearObjecte(site,'psio','Folder','Plans de Suport a la Igualtat d''Oportunitats','Carpeta arrel',exclude=True)

    crearObjecte(site.psio,'genere','Folder','Genere','Carpeta de Genere',exclude=False)

    crearObjecte(site.psio,'discapacitats','Folder','Discapacitats','Carpeta de Discapacitats',exclude=False)



##code-section FOOT
def getObjectStatus(context):
    pw = getToolByName(context, "portal_workflow") 
    object_workflow = pw.getWorkflowsFor(context)[0].id
    object_status = pw.getStatusOf(object_workflow,context)
    return object_status

def doWorkflowAction(context):
    pw = getToolByName(context, "portal_workflow") 
    object_workflow = pw.getWorkflowsFor(context)[0].id
    object_status = pw.getStatusOf(object_workflow,context)
    try:
        pw.doActionFor(context,'publish',wf_id='genweb_simple')
    except:
        pass
                    
    
def crearObjecte(context,id,type_name,title,description,exclude=False,constrains=None):
    pt = getToolByName(context,'portal_types')
    #import pdb;pdb.set_trace()
    if not getattr(context,id,False) and type_name in pt.listTypeTitles().keys():
        #creem l'objecte i el publiquem
        _createObjectByType(type_name, context, id)
    #populem l'objecte
    created = context[id]            
    doWorkflowAction(created)    
    created.setTitle(title)
    created.setDescription(description)
    created._at_creation_flag=False
    try:
        created.setExcludeFromNav(exclude)
    except:
        pass
    if constrains:
        created.setConstrainTypesMode(1)
        created.setLocallyAllowedTypes(tuple(constrains[0]+constrains[1]))
        created.setImmediatelyAddableTypes(tuple(constrains[0]))
                            
    created.reindexObject()
    return created
##/code-section FOOT
