# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

from .response import Response, ResponseSchema

"""
FACe Invoice models and schemas

It defines the "factura" response content and defines an extended Response with the "factura" integrated:
- InvoiceResponse and InvoiceSchema defines the resultado.factura
- Invoice and InvoiceSchema extends the base Response to integrate the "factura" component
"""

class InvoiceResponse(object):
    def __init__(self, numeroRegistro, organoGestor, unidadTramitadora, oficinaContable, identificadorEmisor, numeroFactura, serieFactura, fechaRecepcion):
        self.numeroRegistro = numeroRegistro
        self.organoGestor = organoGestor
        self.unidadTramitadora = unidadTramitadora
        self.oficinaContable = oficinaContable
        self.identificadorEmisor = identificadorEmisor
        self.numeroFactura = numeroFactura
        self.serieFactura = serieFactura
        self.fechaRecepcion = fechaRecepcion


class InvoiceResponseSchema(Schema):
    numeroRegistro = fields.Integer()
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
        super(Invoice, self).__init__(resultado)
        self.factura = factura

class InvoiceSchema(ResponseSchema):
    factura = fields.Nested(InvoiceResponseSchema, many=False)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Invoice(**data)
