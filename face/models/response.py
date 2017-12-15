# -*- coding: utf-8 -*-
from marshmallow import fields, Schema

class ResultadoSchema(Schema):
    codigo = fields.Integer()
    descripcion = fields.String()
    codigoSeguimiento = fields.String()

class ResponseSchema(Schema):
    resultado = fields.Nested(ResultadoSchema, many=False)

class Response(object):
    pass
