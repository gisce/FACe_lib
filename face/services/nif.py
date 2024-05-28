# -*- coding: utf-8 -*-
from .service import SOAP_Service
from ..models import ResponseSchema

class NIF(SOAP_Service):
    """
    Integrate all NIF-related methods
    """

    def __init__(self, service, result_obj=False):
        super(NIF, self).__init__(service)
        self.result_obj = result_obj

    def list(self):
        """
        List NIFs method.

        Return all the available NIFs
        """
        call_result = self.serialize(self.service.consultarNIFs())

        schema = ResponseSchema()
        if self.result_obj:
            return schema.load(call_result)
        else:
            return call_result
