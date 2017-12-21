# -*- coding: utf-8 -*-
from .service import SOAP_Service
from ..models import AdministrationsSchema

class Administration(SOAP_Service):
    """
    Integrate all NIF-related methods
    """

    def list(self):
        """
        List administrations

        It list all available administrations
        """

        call_result = self.serialize(self.service.consultarAdministraciones())

        schema = AdministrationsSchema()
        return schema.load(call_result)
