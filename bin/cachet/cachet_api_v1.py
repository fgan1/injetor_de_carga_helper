#!/usr/bin/python
import urllib
import urllib2
import json
import logging

CONST_SUFIX_INTENT_URL="/api/v1/incidents"
CONST_SUFIX_COMPONENTS_URL="/api/v1/components"
CONST_SUFIX_GROUP_COMPONENTS_URL="/api/v1/components/groups"
CONST_HEADER_APP_KEY="X-Cachet-Token"

CONST_DELETE_METHOD="DELETE"
CONST_POST_METHOD="POST"

CONST_NAME_ATTR="name"
CONST_MESSAGE_ATTR="message"
CONST_STATUS_ATTR="status"
CONST_VISIBLE_ATTR="status"

logger = logging.getLogger(__name__)

# Cachet
# Api v1
class CachetApiV1:

	def __init__(self):
		'''__init__ Constructor'''

	@staticmethod
	def get_groups_component(endpoint):
		logger.debug("Getting groups component in %s." % (endpoint))		
		try:
			url = "%s%s" % (endpoint, CONST_SUFIX_GROUP_COMPONENTS_URL)
			return urllib2.urlopen(url).read()
		except Exception as e:
		    logging.exception("Error while get groups component.")
		    return None

	@staticmethod
	def get_group_component(endpoint, id):
		logger.debug("Getting group component(%s) in %s." % (id, endpoint))
		try:
			url = "%s%s/%s" % (endpoint, CONST_SUFIX_GROUP_COMPONENTS_URL, id)
			return urllib2.urlopen(url).read()
		except Exception as e:
		    logging.exception("Error while get group component(%s)." % (id))
		    return None		

	# TODO implement
	@staticmethod
	def create_group_component(endpoint, name, token):
		logger.debug("Creating group component in %s." % (endpoint))
		try:
			method = CONST_POST_METHOD
			url = "%s%s" % (endpoint, CONST_SUFIX_GROUP_COMPONENTS_URL)
			
			data = urllib.urlencode({CONST_NAME_ATTR : name})

			headers = {CONST_HEADER_APP_KEY: token}

			request = urllib2.Request(url, data=data, headers=headers)
			request.get_method = lambda: method
			response = urllib2.urlopen(request)
			return response.read()
		except Exception as e:
		    logging.exception("Error while create group component.")
		    return None		

	# TODO implement
	@staticmethod
	def delete_group_component(endpoint, id, token):
		logger.debug("Deleting group component(%s) in %s." % (id, endpoint))
		try:
			method = CONST_DELETE_METHOD
			url = "%s%s/%s" % (endpoint, CONST_SUFIX_GROUP_COMPONENTS_URL, id)

			headers = {CONST_HEADER_APP_KEY: token}

			request = urllib2.Request(url, data=None, headers=headers)
			request.get_method = lambda: method
			response = urllib2.urlopen(request)
			return response.read()
		except Exception as e:
		    logging.exception("Error while delete group component(%s)." % (id))
		    return None			


	@staticmethod
	def get_components(endpoint):
		logger.debug("Getting components in %s." % (endpoint))
		try:
			url = "%s%s" % (endpoint, CONST_SUFIX_COMPONENTS_URL)
			return urllib2.urlopen(url).read()
		except Exception as e:
		    logging.exception("Error while get components.")
		    return None				

	@staticmethod
	def get_component(endpoint, id):
		logger.debug("Getting component(%s) in %s." % (id, endpoint))
		try:
			url = "%s%s/%s" % (endpoint, CONST_SUFIX_COMPONENTS_URL, id)
			return urllib2.urlopen(url).read()
		except Exception as e:
		    logging.exception("Error while get component(%s)." % (id))
		    return None				

	@staticmethod
	def delete_component(endpoint, id, token):
		logger.debug("Deleting component(%s) in %s." % (id, endpoint))
		try:
			method = CONST_DELETE_METHOD
			url = "%s%s/%s" % (endpoint, CONST_SUFIX_COMPONENTS_URL, id)

			headers = {CONST_HEADER_APP_KEY: token}

			request = urllib2.Request(url, data=None, headers=headers)
			request.get_method = lambda: method
			response = urllib2.urlopen(request)
			return response.read()
		except Exception as e:
		    logging.exception("Error while delete component(%s)." % (id))
		    return None			

	@staticmethod
	def create_component(endpoint, name, token):
		logger.debug("Creating component in %s." % (endpoint))
		try:
			method = CONST_POST_METHOD
			url = "%s%s" % (endpoint, CONST_SUFIX_COMPONENTS_URL)
			
			data = urllib.urlencode({CONST_NAME_ATTR : name})

			headers = {CONST_HEADER_APP_KEY: token}

			request = urllib2.Request(url, data=data, headers=headers)
			request.get_method = lambda: method
			response = urllib2.urlopen(request)
			return response.read()
		except Exception as e:
		    logging.exception("Error while create component.")
		    return None			

    # TODO implement
	@staticmethod
	def get_intents(endpoint):
		pass

    # TODO implement
	@staticmethod
	def get_intent(endpoint):
		pass

    # TODO implement
	@staticmethod
	def delete_intent(endpoint):
		pass

	@staticmethod
	def create_intent(endpoint, name, message, status, visible, componentId, componentStatus, token):
		logger.debug("Creating intent in %s." % (endpoint))
		try:
			method = CONST_POST_METHOD
			url = "%s%s" % (endpoint, CONST_SUFIX_INTENT_URL)
			
			datas = {CONST_NAME_ATTR : name, CONST_MESSAGE_ATTR: message, 
				CONST_STATUS_ATTR: status, CONST_VISIBLE_ATTR: visible}

			if componentId is not None and componentStatus is not None:
				datas.update({CONST_COMPONENT_ID_ATTR: componentId, CONST_COMPONENT_STATUS_ATTR: componentStatus})	

			data = urllib.urlencode(datas)

			headers = {CONST_HEADER_APP_KEY: token}

			request = urllib2.Request(url, data=data, headers=headers)
			request.get_method = lambda: method
			response = urllib2.urlopen(request)
			return response.read()
		except Exception as e:
		    logging.exception("Error while create intent.")
		    return None

	# TODO implement
	@staticmethod
	def get_metrics(endpoint):
		pass

	# TODO implement
	@staticmethod
	def get_metric(endpoint):
		pass

	# TODO implement
	@staticmethod
	def delete_metric(endpoint, token):
		pass

	# TODO implement
	@staticmethod
	def create_metric(endpoint, token):
		logger.debug("Creating metric in %s." % (endpoint))
		try:
			pass
		except Exception as e:
		    logging.exception("Error while create metric.")
		    return None			

	# TODO implement
	@staticmethod
	def create_metric_ponint(endpoint, token):
		logger.debug("Creating metric point in %s." % (endpoint))
		try:
			pass
		except Exception as e:
		    logging.exception("Error while create metric point.")
		    return None			
