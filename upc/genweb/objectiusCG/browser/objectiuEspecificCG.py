from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName
from upc.genweb.objectiusCG.interfaces import IObjectiuEspecificCG

from plone.memoize.instance import memoize

class ObjectiuEspecificView(BrowserView):
    """Default view of a fitxa
    """

    # This template will be used to render the view. An implicit variable
    # 'view' will be available in this template, referring to an instance
    # of this class. The variable 'context' will refer to the cinema folder
    # being rendered.

    __call__ = ViewPageTemplateFile('objectiuEspecificCG-view.pt')

