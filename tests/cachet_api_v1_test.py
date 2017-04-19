#!/usr/bin/python
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
import mock
from mock import patch, Mock, MagicMock

from bin.cachet.cachet_api_v1 import CachetApiV1

class CachetApiV1Test(unittest.TestCase):

	# TODO or FIXME implement with mock ?
	# TODO check URL

	def setUp(self):
		pass

	def test_get_groups_component_error(self):
		response = CachetApiV1.get_groups_component("http://wrong_url")
		self.assertIsNone(response)

	def test_get_group_component_error(self):
		response = CachetApiV1.get_group_component("http://wrong_url", "id")
		self.assertIsNone(response)

	# TODO check headers and datas
	def test_create_group_component_error(self):
		response = CachetApiV1.create_group_component("http://wrong_url", "name", "token")
		self.assertIsNone(response)

	# TODO check headers and datas
	def test_delete_group_component_error(self):
		response = CachetApiV1.delete_group_component("http://wrong_url", "id", "token")
		self.assertIsNone(response)

	def test_get_components_error(self):
		response = CachetApiV1.get_components("http://wrong_url")
		self.assertIsNone(response)

	def test_get_component_error(self):
		response = CachetApiV1.get_component("http://wrong_url", "id")
		self.assertIsNone(response)

	# TODO check headers and datas
	def test_delete_component_error(self):
		response = CachetApiV1.delete_component("http://wrong_url", "id", "token")
		self.assertIsNone(response)	

	# TODO check headers and datas
	def test_create_component_error(self):
		response = CachetApiV1.create_component("http://wrong_url", "id", 1, 1, "token")
		self.assertIsNone(response)

	# TODO check headers and datas
	def test_create_intent_error(self):
		response = CachetApiV1.create_intent("http://wrong_url", "name", "message", "status", "visible", "componentId", "componentStatus", "token")
		self.assertIsNone(response)	

	def test_get_metrics(self):
		response = CachetApiV1.get_metrics("http://wrong_url")
		self.assertIsNone(response)

	# TODO check headers and datas
	def test_create_metric(self):
		response = CachetApiV1.create_metric("http://wrong_url", "name", "suffix", "description", "default_value", "token")
		self.assertIsNone(response)		

	# TODO check headers and datas
	def test_create_metric_point(self):
		response = CachetApiV1.create_metric_point("http://wrong_url", "metric_id", "value_point", "timestamp", "token")
		self.assertIsNone(response)		


def main():
    unittest.main()

if __name__ == '__main__':
    main()