# -*- coding: utf-8 -*-
from .service import SOAP_Service
from ..models import ResponseSchema

class NIF(SOAP_Service):
    """
    Integrate all NIF-related methods
    """

    def list(self):
        """
        List NIFs method.

        Return all the available NIFs
        """
        call_result = self.serialize(self.service.consultarNIFs())

        schema = ResponseSchema()
        return schema.load(call_result)
