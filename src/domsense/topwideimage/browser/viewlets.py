from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from zope.component import getMultiAdapter
from plone.memoize.view import memoize

from domsense.topwideimage.browser.interfaces import IWideImagesContainer
from domsense.topwideimage.config import CONTAINER_DEFAULT_ID


class WideImageViewlet(ViewletBase):
    render = ViewPageTemplateFile('viewlet_wide.pt')

    images_container = None

    def update(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                            name=u'plone_portal_state')

        self.navigation_root_url = portal_state.navigation_root_url()

        portal = portal_state.portal()

        if hasattr(portal, CONTAINER_DEFAULT_ID):
            self.images_container = portal[CONTAINER_DEFAULT_ID]

    def available(self):
        images = self._get_images()
        return images and not IWideImagesContainer.providedBy(self.context)

    @memoize
    def _get_images(self):
        if not self.images_container:
            return None
        # XXX: are we sure that's better not to use catalog here???
        images = self.images_container.objectValues()
        return images

    @property
    def slide_enabled(self):
        images = self._get_images()
        return len(images) > 1

    @property
    def images(self):
        return self._get_images()
