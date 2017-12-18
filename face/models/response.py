# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

"""
FACe Result

Integrates the code, a description and a tracking code
"""

class Result(object):
    def __init__(self, codigo, descripcion, codigoSeguimiento):
        self.codigo = codigo
        self.descripcion = descripcion
        self.codigoSeguimiento = codigoSeguimiento


class ResultSchema(Schema):
    codigo = fields.Integer()
    descripcion = fields.String()
    codigoSeguimiento = fields.String(allow_none=True)

    @post_load
    def create_resultado(self, data):
        """
        Return a Result instance while deserializing ResultSchema
        """
        return Result(**data)


"""
FACe Response

By default, a response ever contain a Response and an instance of the requested service
"""

class Response(object):
    def __init__(self, resultado):
        self.resultado = resultado

    def __getitem__(self, item):
        return self.__dict__[item]


class ResponseSchema(Schema):
    resultado = fields.Nested(ResultSchema, many=False)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Response(**data)
