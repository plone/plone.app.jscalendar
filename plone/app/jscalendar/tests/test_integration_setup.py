import unittest2 as unittest
from plone.app.jscalendar.tests import base


class IntegrationTestSetup(base.IntegrationTestCase):
    """We tests the setup (install) of the addons. You should check all
    stuff in profile are well activated (browserlayer, js, content types, ...)
    """

    def test_skindirectory(self):
        skins = self.portal.portal_skins
        path = skins.getSkinPath('Plone Default')
        self.assertIn('plone_app_jscalendar', path)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
