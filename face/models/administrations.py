# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

from .response import Response, ResponseSchema

"""
FACe Invoice models and schemas

It defines the "factura" response content and defines an extended Response with the "factura" integrated:
- InvoiceResponse and InvoiceSchema defines the resultado.factura
- Invoice and InvoiceSchema extends the base Response to integrate the "factura" component
"""

class AdministrationsResponse(object):
    def __init__(self, **kwargs):
        self.administraciones = kwargs.get('organoGestor')

class AdministrationsResponseSchema(Schema):
    administraciones = fields.Dict()

    @post_load
    def create_resultado(self, data):
        """
        Return an AdministrationsResponse instance for deserializing ResultSchema
        """
        return AdministrationsResponse(**data)



class Administrations(Response):
    def __init__(self, resultado, administraciones):
        super(Administrations, self).__init__(resultado=resultado)
        self.administraciones = administraciones

class AdministrationsSchema(ResponseSchema):
    administraciones = fields.Nested(AdministrationSchema, many=False)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Administrations(**data)
