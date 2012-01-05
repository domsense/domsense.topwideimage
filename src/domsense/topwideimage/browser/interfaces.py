from zope import interface
from plone.theme.interfaces import IDefaultPloneLayer


class IWideImagesContainer(interface.Interface):
    """ marker interface for wide images container
    """

class ITheme(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """


