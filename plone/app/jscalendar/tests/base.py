import transaction
import unittest2 as unittest
from plone.app.jscalendar import testing
from plone.app import testing as ptesting


class IntegrationTestCase(unittest.TestCase):

    layer = testing.INTEGRATION

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        ptesting.setRoles(self.portal, ptesting.TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        ptesting.setRoles(self.portal, ptesting.TEST_USER_ID, ['Member'])
        self.folder = self.portal['test-folder']
