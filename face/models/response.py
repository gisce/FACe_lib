# -*- coding: utf-8 -*-
from marshmallow import fields, Schema

class Resultado(object):
    def __init__(self, codigo, descripcion, codigoSeguimiento):
        self.codigo = codigo
        self.descripcion = descripcion
        self.codigoSeguimiento = codigoSeguimiento

class ResultadoSchema(Schema):
    codigo = fields.Integer()
    descripcion = fields.String()
    codigoSeguimiento = fields.String()

class ResponseSchema(Schema):
    resultado = fields.Nested(ResultadoSchema, many=False)

class Response(object):
    pass
