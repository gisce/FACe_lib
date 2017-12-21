# -*- coding: utf-8 -*-
from .service import SOAP_Service
from ..models import InvoiceSchema, StatusesSchema
import base64
import os.path

class Invoice(SOAP_Service):
    """
    Integrate all invoice-related methods
    """
    def send(self, invoice):
        """
        Send an invoice and return the delivery result

        It prepares the payload wanted for the `enviarFactura` webservice with a base64 invoice and their filename
        """
        assert type(invoice) == str, "Invoice must the the filename of the invoice to deliver"
        the_invoice = {
            "correo": "devel@gisce.net",
            "factura": {
                "factura": base64.b64encode(open(invoice).read()),
                "nombre": os.path.basename(invoice),
                "mime": "application/xml",
            }
        }
        call_result = self.serialize_response(self.service.enviarFactura(the_invoice))
        schema = InvoiceSchema()
        return schema.load(call_result)

    def cancel(self, invoice, reason):
        """
        Cancel an invoice and return the result

        It uses the invoice registry number (the one reached at the send process) and the cancelation reason.
        """
        assert type(invoice) == str, "Invoice registry number must be an string"
        assert type(reason) == str, "The reason must be an string"

        the_invoice = {
            "numeroRegistro": invoice,
            "motivo": reason,
        }

        call_result = serialize_object(self.service.anularFactura(**the_invoice))
        schema = InvoiceSchema()
        return schema.load(call_result)

    def list_states(self):
        """
        List invoice states

        It list all available invoice states. There are two flows:
        - ordinary flow: it describes the lifecycle of the invoice
        - cancelation flow: it describes the cancelation / anulation flow
        """

        call_result = serialize_object(self.service.consultarEstados())

        schema = StatusesSchema()
        return schema.load(call_result)
