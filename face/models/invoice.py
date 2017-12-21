# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

from .response import Response, ResponseSchema

"""
FACe Invoice models and schemas

It defines the "factura" response content and defines an extended Response with the "factura" integrated:
- InvoiceResponse and InvoiceSchema defines the resultado.factura
- Invoice and InvoiceSchema extends the base Response to integrate the "factura" component
"""


"""
Tramitacion, introduced by consultarFactura response as a part of "Factura" response
"""
class Tramitacion(object):
    def __init__(self, **kwargs):
        self.codigo_estado = kwargs.get('codigo_estado', None)
        self.descripcion_estado = kwargs.get('descripcion_estado', None)
        self.motivo_estado = kwargs.get('motivo_estado', None)

class TramitacionSchema(Schema):
    codigo_estado = fields.String(allow_none=True)
    descripcion_estado = fields.String(allow_none=True)
    motivo_estado = fields.String(allow_none=True)

    @post_load
    def create_tramitacion(self, data):
        """
        Return a Tramitacion instance to deserialize the TramitacionSchema
        """
        return Tramitacion(**data)





class InvoiceResponse(object):
    def __init__(self, **kwargs):
        self.numeroRegistro = kwargs.get('numeroRegistro', None)
        self.organoGestor = kwargs.get('organoGestor')
        self.unidadTramitadora = kwargs.get('unidadTramitadora', None)
        self.oficinaContable = kwargs.get('oficinaContable', None)
        self.identificadorEmisor = kwargs.get('identificadorEmisor', None)
        self.numeroFactura = kwargs.get('numeroFactura', None)
        self.serieFactura = kwargs.get('serieFactura', None)
        self.fechaRecepcion = kwargs.get('fechaRecepcion', None)


class InvoiceResponseSchema(Schema):
    numeroRegistro = fields.Integer(allow_none=True)
    organoGestor = fields.String()
    unidadTramitadora = fields.String(allow_none=True)
    oficinaContable = fields.String(allow_none=True)
    identificadorEmisor = fields.String(allow_none=True)
    numeroFactura = fields.String(allow_none=True)
    serieFactura = fields.String(allow_none=True)
    fechaRecepcion = fields.String(allow_none=True)

    @post_load
    def create_resultado(self, data):
        """
        Return a Result instance while deserializing ResultSchema
        """
        return InvoiceResponse(**data)



class Invoice(Response):
    def __init__(self, resultado, factura):
        super(Invoice, self).__init__(resultado=resultado)
        self.factura = factura

class InvoiceSchema(ResponseSchema):
    factura = fields.Nested(InvoiceResponseSchema, many=False)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Invoice(**data)
