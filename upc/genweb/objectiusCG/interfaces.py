from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

# -*- extra stuff goes here -*-

class IActivitatCG(Interface):
    """A Activitat Content Type
    """

class IAccioCG(Interface):
    """A Accion Content Type
    """

class IObjectiuEspecificCG(Interface):
    """A ObjectiuEspecific Content Type
    """

class IObjectiuGeneralCG(Interface):
    """A ObjectiuGeneral Content Type
    """


    
