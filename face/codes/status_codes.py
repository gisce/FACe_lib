# -*- coding: utf-8 -*-
from marshmallow import ValidationError

"""
FACe available status
"""

def validator(code):
    """
    Status code validator
    """
    if code==None:
        raise ValidationError("Code can't be empty")

    if str(code) not in STATUS_CODES:
        raise ValidationError("Code '{}' is unknown".format(code))


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


    # Anulation status
    "4100": {
        "nombre": "No solicitada anulación",
        "description": "No solicitada anulación",
        "error": False,
        "scope": "tramitacion",
    },
    "4200": {
        "nombre": "Solicitada anulación",
        "description": "Solicitada anulación",
        "error": False,
        "scope": "tramitacion",
    },
    "4300": {
        "nombre": "Aceptada anulación",
        "description": "Aceptada anulación",
        "error": False,
        "scope": "tramitacion",
    },
    "4400": {
        "nombre": "Solicitud de anulación",
        "description": "Rechazada anulación",
        "error": True,
        "scope": "tramitacion",
    },
}
