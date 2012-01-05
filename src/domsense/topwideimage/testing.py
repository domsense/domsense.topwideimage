from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class DomsenseTopwideimage(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import domsense.topwideimage
        xmlconfig.file('configure.zcml',
                       domsense.topwideimage,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'domsense.topwideimage:default')

DOMSENSE_TOPWIDEIMAGE_FIXTURE = DomsenseTopwideimage()
DOMSENSE_TOPWIDEIMAGE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(DOMSENSE_TOPWIDEIMAGE_FIXTURE, ),
                       name="DomsenseTopwideimage:Integration")