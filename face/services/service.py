# -*- coding: utf-8 -*-
from zeep.helpers import serialize_object

class SOAP_Service(object):
    """
    Base SOAP Service to bootstrap a service
    """
    def __init__(self, service):
        self.service = service

    def serialize(self, response):
        return serialize_object(response)
