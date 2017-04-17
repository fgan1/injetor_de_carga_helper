#!/usr/bin/python
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import urllib2
from mock import patch, Mock, MagicMock

from bin.cachet.cachet import Cachet
from bin.cachet.cachet_api_v1 import CachetApiV1

CONST_CACHET_COMPONENTS_RESPONSE="components_response.txt"
CONST_CACHET_COMPONENTS_RESPONSE_COMPONENT_NAME="compute_lsd.manager.naf.lsd.ufcg.edu.br"

CONST_STATUS_CODE_200=200

class CachetTest(unittest.TestCase):

	def setUp(self):
		# self.endpoint = "http://10.30.0.1591"
		# self.token = "wg0UlbLXqmFv4JlPijP21"
		self.__cachet = Cachet()

	
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_get_components(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_COMPONENTS_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		components = self.__cachet.get_components("")
		self.assertEqual(12, len(components))

	# @unittest.skip("testing skipping")
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_get_component_by_name(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_COMPONENTS_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		component = self.__cachet.get_component_by_name("", CONST_CACHET_COMPONENTS_RESPONSE_COMPONENT_NAME)
		self.assertEqual(CONST_CACHET_COMPONENTS_RESPONSE_COMPONENT_NAME, component.get_name())

	def test_(self):
		

# Utils 

def get_response_cachet_api_v1(name_file):
	relative_path = 'resources/%s' % (name_file)
	current_dir = os.getcwd()
	file = open(os.path.join(current_dir, relative_path), 'r')
	content = file.read()
	return content

def defineMockResponse(mock_urlopen, response, status_code):
	mock_response = MagicMock()
	mock_response.getcode.return_value = status_code
	mock_response.read.return_value = response
	mock_urlopen.return_value = mock_response	

# Main

def main():
    unittest.main()

if __name__ == '__main__':
    main()