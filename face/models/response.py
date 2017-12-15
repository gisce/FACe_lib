# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

class Resultado(object):
    def __init__(self, codigo, descripcion, codigoSeguimiento):
        self.codigo = codigo
        self.descripcion = descripcion
        self.codigoSeguimiento = codigoSeguimiento


class ResultadoSchema(Schema):
    codigo = fields.Integer()
    descripcion = fields.String()
    codigoSeguimiento = fields.String(allow_none=True)

    @post_load
    def create_resultado(self, data):
        """
        Return a Resultado instance while deserializing ResultadoSchema
        """
        return Resultado(**data)


class Response(object):
    def __init__(self, resultado):
        self.resultado = resultado

class ResponseSchema(Schema):
    resultado = fields.Nested(ResultadoSchema, many=False)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Response(**data)
