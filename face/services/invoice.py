# -*- coding: utf-8 -*-
from .service import SOAP_Service
from ..models import InvoiceSchema, StatusesSchema
import base64
import os.path

class Invoice(SOAP_Service):
    """
    Integrate all invoice-related methods
    """
    def __init__(self, service, email):
        super(Invoice, self).__init__(service)
        self.email = email

    def fetch(self, invoice):
        """
        Fetch an invoice state using their registry number

        It list the state of an already sended invoice.
        """
        assert type(invoice) in [int, str], "Invoice must be the registry number of the sended invoice."
        call_result = self.serialize(self.service.consultarFactura(numeroRegistro=str(invoice)))
        schema = InvoiceSchema()
        return schema.load(call_result)

    def send(self, invoice, attachments=None):
        """
        Send an invoice with optional attachments and return the delivery result

        It prepares the payload wanted for the `enviarFactura` webservice with a base64 invoice and their filename
        """
        assert type(invoice) == str, "Invoice must be the filename of the invoice to deliver"
        the_invoice = {
            "correo": self.email,
            "factura": {
                "factura": base64.b64encode(open(invoice).read()),
                "nombre": os.path.basename(invoice),
                "mime": "application/xml",
            }
        }
        if attachments:
            the_invoice['anexos'] = attachments

        call_result = self.serialize(self.service.enviarFactura(the_invoice))
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

        call_result = self.serialize(self.service.anularFactura(**the_invoice))
        schema = InvoiceSchema()
        return schema.load(call_result)

    def list_states(self):
        """
        List invoice states

        It list all available invoice states. There are two flows:
        - ordinary flow: it describes the lifecycle of the invoice
        - cancelation flow: it describes the cancelation / anulation flow
        """

        call_result = self.serialize(self.service.consultarEstados())
        schema = StatusesSchema()
        return schema.load(call_result)
