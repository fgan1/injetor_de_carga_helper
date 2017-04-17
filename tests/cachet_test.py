#!/usr/bin/python
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import urllib2
import time
from mock import patch, Mock, MagicMock

from bin.cachet.cachet import Cachet
from bin.cachet.cachet import Incident
from bin.cachet.cachet import Metric
from bin.cachet.cachet import MetricPoint
from bin.cachet.cachet_api_v1 import CachetApiV1

CONST_CACHET_COMPONENTS_RESPONSE="components_response.json"
CONST_CACHET_COMPONENTS_RESPONSE_COMPONENTS_SIZE=12
CONST_CACHET_COMPONENTS_RESPONSE_COMPONENT_NAME="compute_lsd.manager.naf.lsd.ufcg.edu.br"

CONST_CACHET_GROUPS_COMPONENT_RESPONSE="groups_components_response.json"
CONST_CACHET_GROUPS_COMPONENT_RESPONSE_GROUPS_COMPONENTS_SIZE=4
CONST_CACHET_GROUPS_COMPONENT_RESPONSE_GROUP_COMPONENT_NAME="gc_lsd.manager.naf.lsd.ufcg.edu.br"

CONST_CACHET_CREATE_INCIDENT_RESPONSE="create_incident.json"
CONST_CACHET_CREATE_INCIDENT_RESPONSE_INCIDENT_ID=18

CONST_CACHET_CREATE_METRIC_RESPONSE="create_metric.json"
CONST_CACHET_CREATE_METRIC_RESPONSE_METRIC_ID=1

CONST_CACHET_CREATE_METRIC_POINT_RESPONSE="create_metric_point.json"
CONST_CACHET_CREATE_METRIC_POINT_RESPONSE_M_P_ID=1

CONST_CACHET_CREATE_METRICS_RESPONSE="get_metrics.json"
CONST_CACHET_CREATE_METRICS_RESPONSE_SIZE=2

CONST_STATUS_CODE_200=200

CONST_PATH_RESOURCES="resources"

class CachetTest(unittest.TestCase):

	def setUp(self):

		self.__cachet = Cachet()

	@unittest.skip("testing skipping")	
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_get_components(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_COMPONENTS_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		components = self.__cachet.get_components("")
		self.assertEqual(CONST_CACHET_COMPONENTS_RESPONSE_COMPONENTS_SIZE, len(components))

	@unittest.skip("testing skipping")
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_get_component_by_name(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_COMPONENTS_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		component = self.__cachet.get_component_by_name("", CONST_CACHET_COMPONENTS_RESPONSE_COMPONENT_NAME)
		self.assertEqual(CONST_CACHET_COMPONENTS_RESPONSE_COMPONENT_NAME, component.get_name())

	@unittest.skip("testing skipping")
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_get_group_componets(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_GROUPS_COMPONENT_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		group_components = self.__cachet.get_groups_component("")
		self.assertEqual(CONST_CACHET_GROUPS_COMPONENT_RESPONSE_GROUPS_COMPONENTS_SIZE, len(group_components))

	@unittest.skip("testing skipping")
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_get_group_component_by_name(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_GROUPS_COMPONENT_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		group_component = self.__cachet.get_group_component_by_name("", CONST_CACHET_GROUPS_COMPONENT_RESPONSE_GROUP_COMPONENT_NAME)
		self.assertEqual(CONST_CACHET_GROUPS_COMPONENT_RESPONSE_GROUP_COMPONENT_NAME, group_component.get_name())

	@unittest.skip("testing skipping")
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_create_incident(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_CREATE_INCIDENT_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		incident = Incident(None, None, None, None, None, None, None)
		incident = self.__cachet.create_incident("", incident, "")
		self.assertEqual(CONST_CACHET_CREATE_INCIDENT_RESPONSE_INCIDENT_ID, incident.get_id())
		
	@unittest.skip("testing skipping")
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_create_metric(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_CREATE_METRIC_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		metric = Metric(None, None, None, None, None)
		metric = self.__cachet.create_metric("", metric, "") 
		self.assertEqual(CONST_CACHET_CREATE_METRIC_RESPONSE_METRIC_ID, metric.get_id())

	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_get_metrics(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_CREATE_METRICS_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)				

		metrics = self.__cachet.get_metrics(self.endpoint)
		self.assertEqual(CONST_CACHET_CREATE_METRICS_RESPONSE_SIZE, len(metrics))

	@unittest.skip("testing skipping")
	@patch('bin.cachet.cachet_api_v1.urllib2.urlopen')
	def test_create_metric_point(self, mock_urlopen):
		response = get_response_cachet_api_v1(CONST_CACHET_CREATE_METRIC_POINT_RESPONSE)
		defineMockResponse(mock_urlopen, response , CONST_STATUS_CODE_200)

		metric_point = MetricPoint(None, None, None)
		metric_point = self.__cachet.create_metric_point("", metric_point, "") 
		self.assertEqual(CONST_CACHET_CREATE_METRIC_POINT_RESPONSE_M_P_ID, metric_point.get_id())

# Utils 

def get_response_cachet_api_v1(name_file):
	relative_path = '%s/%s' % (CONST_PATH_RESOURCES, name_file)
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