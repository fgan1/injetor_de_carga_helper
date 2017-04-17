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
		# print(CachetApiV1.getGroupsComponent(endpoint))
		# print(CachetApiV1.getGroupComponent(endpoint, "1"))
		# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>@")
		# print(CachetApiV1.getComponents(endpoint))
		# print(CachetApiV1.getComponent(endpoint, "1"))
		# print(CachetApiV1.createComponent(endpoint, "testiii", token))
		# print(CachetApiV1.deleteComponent(endpoint, "14", token))
		# print(CachetApiV1.createIntent(endpoint, "name", "d", "1", "1", None, None, token))

		self.failUnless(True)

	def test_get_groups_component(self): 		
	    pass

	def mock_response(self, mock, body, code):
		pass

def main():
    unittest.main()

if __name__ == '__main__':
    main()