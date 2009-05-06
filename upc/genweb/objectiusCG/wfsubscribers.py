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
    ##/code-section notificar



##code-section module-footer #fill in your manual code here
##/code-section module-footer

