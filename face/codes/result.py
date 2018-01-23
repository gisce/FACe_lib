# -*- coding: utf-8 -*-
from marshmallow import ValidationError

"""
FACe available result codes
"""

def validator(code):
    """
    Result code validator
    """
    if code==None:
        raise ValidationError("Code can't be empty")

    if str(code) not in RESULT_CODES:
        raise ValidationError("Code '{}' is unknown".format(code))


RESULT_CODES = {
    "0": {
        "description": "El proceso terminó correctamente",
        "error": False,
        "scope": "base",
    },

    # SOAP Security errors
    "100": {
        "description": "La firma de la petición SOAP no es válida",
        "error": True,
        "scope": "soap-security",
    },
    "101": {
        "description": "La petición SOAP viene vacía",
        "error": True,
        "scope": "soap-security",
    },
    "102": {
        "description": "La petición SOAP no está bien construida: no se encuentra el SOAP Envelope",
        "error": True,
        "scope": "soap-security",
    },
    "103": {
        "description": "La petición SOAP no está bien construida: no se encuentra el SOAP Body",
        "error": True,
        "scope": "soap-security",
    },
    "104": {
        "description": "La petición SOAP no está bien construida: no se encuentra el SOAP Header",
        "error": True,
        "scope": "soap-security",
    },
    "106": {
        "description": "El certificado usado en la firma soap esta en una lista de bloqueo o es de pruebas",
        "error": True,
        "scope": "soap-security",
    },



    # Afirma verification errors
    "200": {
        "description": "Afirma no ha podido obtener información del certificado",
        "error": True,
        "scope": "afirma-verification",
    },
    "201": {
        "description": "No se ha podido procesar la solicitud con Afirma",
        "error": True,
        "scope": "afirma-verification",
    },



    # Invoice management errors
    "300": {
        "description": "El certificado electrónico no está dado de alta en FACe. Para la presentación automatizada de facturas es necesario registrarse previamente en https://face.gob.es/es/proveedores",
        "error": True,
        "scope": "invoice",
    },
    "301": {
        "description": "No puede consultar el estado de la factura, la factura ha sido presentada por otro sistema proveedor",
        "error": True,
        "scope": "invoice",
    },
    "302": {
        "description": "Debe especificarse un motivo de anulación",
        "error": True,
        "scope": "invoice",
    },
    "303": {
        "description": "No existe factura con el número de registro especificado",
        "error": True,
        "scope": "invoice",
    },
    "304": {
        "description": "La factura ya tiene aceptada su anulación",
        "error": True,
        "scope": "invoice",
    },
    "305": {
        "description": "La factura fue rechazada, no se permite solicitar anulación",
        "error": True,
        "scope": "invoice",
    },
    "306": {
        "description": "La factura fue pagada, no se permite solicitar anulación",
        "error": True,
        "scope": "invoice",
    },
    "307": {
        "description": "La factura ya tiene solicitada su anulación",
        "error": True,
        "scope": "invoice",
    },
    "308": {
        "description": "No tiene permisos para solicitar la anulación de esta factura",
        "error": True,
        "scope": "invoice",
    },
    "309": {
        "description": "Se ha excedido el número de facturas permitidas a enviar en el método",
        "error": True,
        "scope": "invoice",
    },
    "310": {
        "description": "Algún parámetro obligatorio aparece vacío",
        "error": True,
        "scope": "invoice",
    },
    "311": {
        "description": "El MIME de la factura es incorrecto",
        "error": True,
        "scope": "invoice",
    },
    "312": {
        "description": "Se ha encontrado un MIME de anexo incorrecto",
        "error": True,
        "scope": "invoice",
    },
    "313": {
        "description": "Es obligatorio el número de registro",
        "error": True,
        "scope": "invoice",
    },
    "314": {
        "description": "No se ha encontrado la solicitud de procesamiento de facturas offline",
        "error": True,
        "scope": "invoice",
    },
    "315": {
        "description": "El sistema de gestión de proveedor no puede consultar la solicitud de procesamiento de facturas offline",
        "error": True,
        "scope": "invoice",
    },
    "316": {
        "description": "La factura ha sido presentada por el portal web, no puede consultar el estado de la factura por servicios web",
        "error": True,
        "scope": "invoice",
    },
    "317": {
        "description": "No se ha podido consultar el estado de la factura, por favor inténtelo más tarde",
        "error": True,
        "scope": "invoice",
    },
    "401": {
        "description": "No se pudo validar la factura",
        "error": True,
        "scope": "invoice",
    },
    "402": {
        "description": "No se pudo guardar la factura",
        "error": True,
        "scope": "invoice",
    },
    "403": {
        "description": "No se ha podido registrar la factura en el Registro Electrónico Común (REC), inténtelo más tarde",
        "error": True,
        "scope": "invoice",
    },
    "404": {
        "description": "Error al cambiar el estado de la factura",
        "error": True,
        "scope": "invoice",
    },
    "405": {
        "description": "No existe el código de estado $status$",
        "error": True,
        "scope": "invoice",
    },
    "406": {
        "description": "La única transición posible es a $status$",
        "error": True,
        "scope": "invoice",
    },
    "407": {
        "description": "Transición no disponible COD: $cod_estado_actual$ => COD: $cod_estado_siguiente$",
        "error": True,
        "scope": "invoice",
    },
    "408": {
        "description": "Formato de la factura es incorrecto",
        "error": True,
        "scope": "invoice",
    },
    "409": {
        "description": "No existe o inactiva el Órgano Gestor asociado al código $OG$",
        "error": True,
        "scope": "invoice",
    },
    "410": {
        "description": "No existe o inactiva la Unidad Tramitadora asociado al código $UT$",
        "error": True,
        "scope": "invoice",
    },
    "411": {
        "description": "No existe o inactiva la Oficina Contable asociado al código $OC$",
        "error": True,
        "scope": "invoice",
    },
    "412": {
        "description": "La Unidad Tramitadora, Órgano Gestor u Oficina contable especificados no están relacionados",
        "error": True,
        "scope": "invoice",
    },
    "413": {
        "description": "La Unidad Tramitadora, Órgano Gestor o Oficina contable especificados no tienen activa la relación y no acepta facturas",
        "error": True,
        "scope": "invoice",
    },
    "414": {
        "description": "Ya existe una factura con número $numero$$registro$",
        "error": True,
        "scope": "invoice",
    },
    "415": {
        "description": "Ya existe una factura con serie $serie$, número $numero$ y fecha de expedición $fecha_exp$$registro$",
        "error": True,
        "scope": "invoice",
    },
    "416": {
        "description": "El número de centros administrativos es incorrecto",
        "error": True,
        "scope": "invoice",
    },
    "417": {
        "description": "No se ha encontrado código en $centro_administrativo$",
        "error": True,
        "scope": "invoice",
    },
    "418": {
        "description": "No se han especificado correctamente el Pagador, Receptor o Fiscal",
        "error": True,
        "scope": "invoice",
    },
    "419": {
        "description": "Sólo se aceptan facturas de modalidad individual",
        "error": True,
        "scope": "invoice",
    },
    "420": {
        "description": "Número de facturas permitidas 1, no se aceptan lotes",
        "error": True,
        "scope": "invoice",
    },
    "421": {
        "description": "El tipo de $emisor-receptor-tercero$ es incorrecto, especificación incorrecta para persona $juridica-fisica$",
        "error": True,
        "scope": "invoice",
    },
    "422": {
        "description": "El tipo de emisor para factura de Terceros es incorrecto",
        "error": True,
        "scope": "invoice",
    },
    "423": {
        "description": "No se ha especificado el nombre o apellido de la persona física",
        "error": True,
        "scope": "invoice",
    },
    "424": {
        "description": "No se ha especificado la razón social de la persona jurídica",
        "error": True,
        "scope": "invoice",
    },
    "425": {
        "description": "El número de facturas es incorrecto",
        "error": True,
        "scope": "invoice",
    },
    "426": {
        "description": "Para pago por $tipo_pago$ es obligatorio incluir el IBAN",
        "error": True,
        "scope": "invoice",
    },
    "427": {
        "description": "Debe indicarse tipo de persona (Física o Jurídica)",
        "error": True,
        "scope": "invoice",
    },
    "428": {
        "description": "La firma de la factura es incorrecta",
        "error": True,
        "scope": "invoice",
    },
    "429": {
        "description": "La factura no se encuentra en el sistema",
        "error": True,
        "scope": "invoice",
    },
    "430": {
        "description": "Formato de la factura es incorrecto, no se pudo determinar la versión de la factura",
        "error": True,
        "scope": "invoice",
    },
    "431": {
        "description": "Se encontró un error de formato fecha en la factura, por favor revise la factura",
        "error": True,
        "scope": "invoice",
    },
    "432": {
        "description": "La factura ha sido firmada por un certificado de clase $clase_certificado$, esta clase no está admitida para firma de facturas",
        "error": True,
        "scope": "invoice",
    },
    "433": {
        "description": "Se ha excedido en el número de anexos",
        "error": True,
        "scope": "invoice",
    },
    "434": {
        "description": "La factura ha sido firmada por un certificado con información incompleta. FACe requiere información del CIF y nombre o razón social para admitirlo.",
        "error": True,
        "scope": "invoice",
    },
    "435": {
        "description": "La operación no admite este estado",
        "error": True,
        "scope": "invoice",
    },
    "437": {
        "description": "No se admiten facturas con extensiones para la Oficina Contable $codigo_dir$",
        "error": True,
        "scope": "invoice",
    },
    "438": {
        "description": "La entrega de la factura ha sido firmada por un certificado de clase $clase_certificado$, esta clase no está admitida para firma de entrega de facturas",
        "error": True,
        "scope": "invoice",
    },
    "439": {
        "description": "La factura ha sido firmada por un certificado no admitido para la firma de factura",
        "error": True,
        "scope": "invoice",
    },
    "440": {
        "description": "La política de firma no es correcta",
        "error": True,
        "scope": "invoice",
    },
    "441": {
        "description": "No se permiten unidades de prueba en este entorno",
        "error": True,
        "scope": "invoice",
    },
    "442": {
        "description": "El certificado usado en la firma de la factura esta en una lista de bloqueo o es de pruebas",
        "error": True,
        "scope": "invoice",
    },
    "443": {
        "description": "La factura rectificativa con formato incorrecto $detail$",
        "error": True,
        "scope": "invoice",
    },
    "444": {
        "description": "El emisor en la factura tiene el mismo identificador que el cesionario",
        "error": True,
        "scope": "invoice",
    },
    "445": {
        "description": "El número de factura es obligatorio",
        "error": True,
        "scope": "invoice",
    },
    "446": {
        "description": "La descripción de las líneas de la factura es obligatoria",
        "error": True,
        "scope": "invoice",
    },
    "447": {
        "description": "El DNI del emisor es incorrecto",
        "error": True,
        "scope": "invoice",
    },
    "900": {
        "description": "Se ha excedido del límite de caracteres $extra$",
        "error": True,
        "scope": "invoice",
    },



    ## Other errors
    "001": {
        "description": "Mensaje genérico (El proceso finalizó con error. El error no ha sido determinado, pudo deberse a problemas de comunicacion con otras plataformas, problemas de datos, etc.)",
        "error": True,
        "scope": "other",
    },
}


# Add good results
RESULT_CODES.update({'ok': [ code for code in RESULT_CODES if RESULT_CODES[code]['error'] == False ]})

# Add error results
RESULT_CODES.update({'ko': [ code for code in RESULT_CODES if code != "ok" and RESULT_CODES[code]['error'] == True ]})
