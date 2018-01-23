# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

from .response import Response, ResponseSchema

# Load the default status codes
import face.codes as codes

"""
FACe Status models and schemas
"""

class Status(object):
    def __init__(self, **kwargs):
        self.codigo = kwargs.get('codigo', None)
        self.descripcion = kwargs.get('descripcion', None)
        self.nombre = kwargs.get('nombre', None)

    def __getitem__(self, item):
        return self.__dict__[item]

class StatusSchema(Schema):
    codigo = fields.String(validate=codes.status.validator)
    descripcion = fields.String()
    nombre = fields.String()

    @post_load
    def create_resultado(self, data):
        """
        Return an Status instance desired to deserialize StatusSchema
        """
        return Status(**data)



"""
Dummy nested model and schema desired to handle the non-sense "estado" list inside the SOAP response
"""
class StatusList(object):
    def __init__(self, **kwargs):
        self.estado = kwargs.get('estado', None)

    def __getitem__(self, item):
        return self.__dict__[item]

class StatusListSchema(Schema):
    estado = fields.List(fields.Nested(StatusSchema))

    @post_load
    def create_resultado(self, data):
        """
        Return an StatusList instance for deserializing StatusListSchema
        """
        return StatusList(**data)



class Statuses(Response):
    def __init__(self, resultado, estados):
        super(Statuses, self).__init__(resultado=resultado)
        self.estados = estados

class StatusesSchema(ResponseSchema):
    estados = fields.Nested(StatusListSchema)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Statuses(**data)
