# -*- coding: utf-8 -*-
from marshmallow import fields, Schema, post_load

# Load the default result codes
import face.codes as codes


"""
FACe Result

Integrates the code, a description and a tracking code
"""
class Result(object):
    def __init__(self, codigo, descripcion, codigoSeguimiento):
        self.codigo = codigo
        self.descripcion = descripcion
        self.codigoSeguimiento = codigoSeguimiento
        self.error = not self.is_good_code

    def __getitem__(self, item):
        return self.__dict__[item]

    @property
    def is_performed(self):
        """
        Review if the Result was performed or not
        """
        return True if self.codigo != None else False

    @property
    def is_good_code(self):
        """
        Review if the Result is OK or KO based on FACe's result codes
        """
        return True if self.is_performed and str(self.codigo) in codes.result.RESULT_CODES['ok'] else False

class ResultSchema(Schema):
    codigo = fields.Integer(validate=codes.result.validator)
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

    @property
    def is_ok(self):
        """
        Clarify if a response includes an OK result code
        """
        return not self.resultado.error


class ResponseSchema(Schema):
    resultado = fields.Nested(ResultSchema, many=False)

    @post_load
    def create_response(self, data):
        """
        Return a Response instance while deserializing ResponseSchema
        """
        return Response(**data)
