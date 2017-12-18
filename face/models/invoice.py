# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

"""
FACe Invoice Response

Integrates the code, a description and a tracking code
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
