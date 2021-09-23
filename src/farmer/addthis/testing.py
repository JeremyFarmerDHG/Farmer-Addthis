# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import farmer.addthis


class FarmerAddthisLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=farmer.addthis)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'farmer.addthis:default')


FARMER_ADDTHIS_FIXTURE = FarmerAddthisLayer()


FARMER_ADDTHIS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FARMER_ADDTHIS_FIXTURE,),
    name='FarmerAddthisLayer:IntegrationTesting',
)


FARMER_ADDTHIS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FARMER_ADDTHIS_FIXTURE,),
    name='FarmerAddthisLayer:FunctionalTesting',
)


FARMER_ADDTHIS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        FARMER_ADDTHIS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='FarmerAddthisLayer:AcceptanceTesting',
)
