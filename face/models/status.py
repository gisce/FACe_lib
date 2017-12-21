# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

from .response import Response, ResponseSchema


STATUS_CODES = {
    # "Tramitación" status
    "1200": {
        "nombre": "Registrada",
        "description": "La factura ha sido registrada en el registro electrónico REC",
        "error": False,
        "scope": "tramitacion",
    },
    "1300": {
        "nombre": "Registrada en RCF",
        "description": "La factura ha sido registrada en el RCF",
        "error": False,
        "scope": "tramitacion",
    },
    "2400": {
        "nombre": "Contabilizada la obligación de pago",
        "description": "La factura ha sido reconocida con obligación de pago",
        "error": False,
        "scope": "tramitacion",
    },
    "2500": {
        "nombre": "Pagada",
        "description": "Factura pagada",
        "error": False,
        "scope": "tramitacion",
    },
    "2600": {
        "nombre": "Rechazada",
        "description": "La Unidad rechaza la factura",
        "error": True,
        "scope": "tramitacion",
    },
    "3100": {
        "nombre": "Anulada",
        "description": "La Unidad aprueba la propuesta de anulación",
        "error": False,
        "scope": "tramitacion",
    },

}




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
    codigo = fields.String()
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
