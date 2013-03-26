from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
import plone.app.jscalendar

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                            zcml_package=plone.app.jscalendar,
                            additional_z2_products=[],
                            gs_profile_id='plone.app.jscalendar:default',
                            name="plone.app.jscalendar:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="plone.app.jscalendar:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="plone.app.jscalendar:Functional")
