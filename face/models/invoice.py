# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

from .response import Response, ResponseSchema

# Load the default status codes
import face.codes as codes

"""
FACe Invoice models and schemas

It defines the "factura" response content and defines an extended Response with the "factura" integrated:
- InvoiceResponse and InvoiceSchema defines the resultado.factura
- Invoice and InvoiceSchema extends the base Response to integrate the "factura" component
"""

"""
Generic InvoiceState to integrate Tramitacion and Anulacion Invoice states
"""
class InvoiceState(object):
    def __init__(self, **kwargs):
        self.codigo = kwargs.get('codigo', None)
        self.descripcion = kwargs.get('descripcion', None)
        self.motivo = kwargs.get('motivo', None)

    def __getitem__(self, item):
        return self.__dict__[item]

class InvoiceStateSchema(Schema):
    codigo = fields.String(validate=codes.status.validator)
    descripcion = fields.String(allow_none=True)
    motivo = fields.String(allow_none=True)

    @post_load
    def create_tramitacion(self, data):
        """
        Return a Tramitacion instance to deserialize the TramitacionSchema
        """
        return InvoiceState(**data)



class InvoiceResponse(object):
    def __init__(self, **kwargs):
        self.numeroRegistro = kwargs.get('numeroRegistro', None)
        self.organoGestor = kwargs.get('organoGestor', None)
        self.unidadTramitadora = kwargs.get('unidadTramitadora', None)
        self.oficinaContable = kwargs.get('oficinaContable', None)
        self.identificadorEmisor = kwargs.get('identificadorEmisor', None)
        self.numeroFactura = kwargs.get('numeroFactura', None)
        self.serieFactura = kwargs.get('serieFactura', None)
        self.fechaRecepcion = kwargs.get('fechaRecepcion', None)

        # needed for consultarFactura
        self.tramitacion = kwargs.get('tramitacion', None)
        self.anulacion = kwargs.get('anulacion', None)

    def __getitem__(self, item):
        return self.__dict__[item]

class InvoiceResponseSchema(Schema):
    numeroRegistro = fields.Integer(allow_none=True)
    organoGestor = fields.String(allow_none=True)
    unidadTramitadora = fields.String(allow_none=True)
    oficinaContable = fields.String(allow_none=True)
    identificadorEmisor = fields.String(allow_none=True)
    numeroFactura = fields.String(allow_none=True)
    serieFactura = fields.String(allow_none=True)
    fechaRecepcion = fields.String(allow_none=True)

    # needed for consultarFactura
    tramitacion = fields.Nested(InvoiceStateSchema, many=False, allow_none=True)
    anulacion = fields.Nested(InvoiceStateSchema, many=False, allow_none=True)

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
