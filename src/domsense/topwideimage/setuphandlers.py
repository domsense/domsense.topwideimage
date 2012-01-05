from zope.site.hooks import getSite

from zope import interface

from domsense.topwideimage.browser.interfaces import IWideImagesContainer
from domsense.topwideimage.config import CONTAINER_DEFAULT_ID
from domsense.topwideimage.config import CONTAINER_DEFAULT_TITLE


def setupVarious(context):

    if context.readDataFile('domsense.topwideimage.import_various.txt') is None:
        return

    site = getSite()
    if not hasattr(site,CONTAINER_DEFAULT_ID):
        site.invokeFactory('Folder',
                           CONTAINER_DEFAULT_ID,
                           title=CONTAINER_DEFAULT_TITLE)
        folder = getattr(site,CONTAINER_DEFAULT_ID)
        folder.markCreationFlag()
        interface.alsoProvides(folder,IWideImagesContainer)

        # set constrain on type
        if not folder.getConstrainTypesMode():
            folder.setConstrainTypesMode(1)
        # flush allowed types
        folder.setLocallyAllowedTypes(())
        # set proper type
        folder.setLocallyAllowedTypes(['Image','ATImage'])
        # omit from nav
        folder.getField('excludeFromNav').set(folder,True)
        folder.reindexObject()





