#!/usr/bin/python
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import mock
from mock import patch, Mock

from bin.cachet.cachet_api_v1 import CachetApiV1

class CachetApiV1Test(unittest.TestCase):

	# TODO remove this method
	def test_(self): 
		endpoint = "http://10.30.0.159"
		token = "wg0UlbLXqmFv4JlPijP1"
		# print(CachetApiV1.getGroupsComponent(endpoint))
		# print(CachetApiV1.getGroupComponent(endpoint, "1"))
		# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>@")
		# print(CachetApiV1.getComponents(endpoint))
		# print(CachetApiV1.getComponent(endpoint, "1"))
		# print(CachetApiV1.createComponent(endpoint, "testiii", token))
		# print(CachetApiV1.deleteComponent(endpoint, "14", token))
		# print(CachetApiV1.createIntent(endpoint, "name", "d", "1", "1", None, None, token))

		self.failUnless(True)

	# @patch('bin.cachet.cachet_api_v1.CachetApiV1.urllib2')
	def test_get_groups_component(self): 		
	    # a = Mock()
	    # a.read.side_effect = ['resp1', '']
	    # mock_urlopen.return_value = a	
	    # mock('urlopen', returns_func="abc", tracker=None)
	    # print(CachetApiV1.getComponents("endpoint"))
	    # self.failUnless(True)
	    pass

	def mock_response(self, mock, body, code):
        response = Mock
        response.read = Mock(return_value=body)
        response.code = code

        self.request_object = Mock()
        mock.Request = Mock(return_value=self.request_object)

        mock.urlopen = Mock(return_value=response)

def main():
    unittest.main()

if __name__ == '__main__':
    main()