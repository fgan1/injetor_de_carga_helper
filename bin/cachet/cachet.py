#!/usr/bin/python
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import json

from bin.cachet.cachet_api_v1 import CachetApiV1

CONST_DATA_JSON_ATTR="data"
CONST_NAME_JSON_ATTR="name"
CONST_ID_JSON_ATTR="id"

CONST_ERROR_MESSAGE_CACHET_API_V1="CachetApiV1 Error."

class Cachet:

	def __init__(self):
		'''__init__ Constructor'''
		pass

	def get_components(self, endpoint):
		jsonStr = CachetApiV1.get_components(endpoint)
		if jsonStr == None:
			raise Exception(CONST_ERROR_MESSAGE_CACHET_API_V1)

		jsonObject = json.loads(jsonStr)
		componentsJsonArray = jsonObject[CONST_DATA_JSON_ATTR]
		components = []
		for componentJson in componentsJsonArray:
		    name = componentJson[CONST_NAME_JSON_ATTR]
		    id = componentJson[CONST_ID_JSON_ATTR]
		    components.append(Component(id, name))
		return components

	def get_component_by_name(self, endpoint, name):
		components = self.get_components(endpoint)
		if components == None or len(components) == 0:
			return None
		for component in components:
			if component.get_name() == name:
				return component
		return None

class Component:

	def __init__(self, id, name):
		self.__id = id
		self.__name = name
		pass

	def get_id(self):
		return self.__id

	def get_name(self):
		return self.__name

	def __str__(self):
		return "id : %s, name : %s" % (self.__id, self.__name)

	def __unicode__(self):
		return u"id : %s, name : %s" % (self.__id, self.__name)