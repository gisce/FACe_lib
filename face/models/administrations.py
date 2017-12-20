# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

from .response import Response, ResponseSchema

"""
FACe Invoice models and schemas

It defines the "factura" response content and defines an extended Response with the "factura" integrated:
- InvoiceResponse and InvoiceSchema defines the resultado.factura
- Invoice and InvoiceSchema extends the base Response to integrate the "factura" component
"""

class Administration(object):
    def __init__(self, **kwargs):
        self.codigo = kwargs.get('codigo', None)
        self.nombre = kwargs.get('nombre', None)

    def __getitem__(self, item):
        return self.__dict__[item]

class AdministrationSchema(Schema):
    codigo = fields.String()
    nombre = fields.String()

    @post_load
    def create_resultado(self, data):
        """
        Return an Administration instance for deserializing ResultSchema
        """
        return Administration(**data)



"""
Dummy nested model and schema desired to handle the non-sense "administracion" list inside the SOAP response
"""
class AdministrationsList(object):
    def __init__(self, **kwargs):
        self.administracion = kwargs.get('administracion', None)

    def __getitem__(self, item):
        return self.__dict__[item]

class AdministrationsListSchema(Schema):
    administracion = fields.List(fields.Nested(AdministrationSchema))

    @post_load
    def create_resultado(self, data):
        """
        Return an AdministrationResponse instance for deserializing ResultSchema
        """
        return AdministrationsList  (**data)



class Administrations(Response):
    def __init__(self, resultado, administraciones):
        super(Administrations, self).__init__(resultado=resultado)
        self.administraciones = administraciones

class AdministrationsSchema(ResponseSchema):
    administraciones = fields.Nested(AdministrationsListSchema)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Administrations(**data)
