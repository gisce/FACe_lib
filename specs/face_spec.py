# -*- coding: utf-8 -*-
from face import FACe, models

OUR_CERT = "certs/our_cert.pem"
TEST_INVOICE = 'specs/factura-prueba-v1-2-0.xsig'


models_by_base_field = {
    "invoice": {
        "field": "factura",
        "response": models.invoice.Invoice,
        "content": models.invoice.InvoiceResponse,
    },


    # Administrations schema
    "administrations": {
        "field": "administraciones",
        "response": models.administrations.Administrations,
        "content": models.administrations.AdministrationsList,
    },
    "administrations_list": {
        "field": "administracion",
        "response": models.administrations.AdministrationsList,
        "content": list,
    },
    "administration": {
        "field": 0,
        "response": list,
        "content": models.administrations.Administration,
    },
    "administration_code": {
        "field": 'codigo',
        "response": models.administrations.Administration,
        "content": unicode,
    },
    "administration_name": {
        "field": 'nombre',
        "response": models.administrations.Administration,
        "content": unicode,
    },


    # Statuses schema
    "statuses": {
        "field": "estados",
        "response": models.status.Statuses,
        "content": models.status.StatusList,
    },
    "statuses_list": {
        "field": "estado",
        "response": models.status.StatusList,
        "content": list,
    },
    "status": {
        "field": 0,
        "response": list,
        "content": models.status.Status,
    },
    "status_code": {
        "field": 'codigo',
        "response": models.status.Status,
        "content": unicode,
    },
    "status_name": {
        "field": 'nombre',
        "response": models.status.Status,
        "content": unicode,
    },
    "status_description": {
        "field": 'descripcion',
        "response": models.status.Status,
        "content": unicode,
    },
}

def validate_response(response, model=None):
    """
    Auxiliar method to validate responses

    It asserts:
    - the type of the response
    - the type of the result of the response
    - the status of a result (codigo=0 and descripcion="Correcto")
    """

    # Test provided model
    if model:
        expected_response_model = models_by_base_field[model]["response"]
        expected_content_model = models_by_base_field[model]["content"]
        expected_field = models_by_base_field[model]["field"]

        # Validate the response
        assert isinstance(response, expected_response_model), "The response must be a `{}` instance".format(type(response), expected_response_model)

        # Validate the internal component of this response
        component = response[expected_field]
        assert isinstance(component, expected_content_model), "The data '{}' must be a `{}` instance".format(type(component), models_by_base_field[model])

    # Test default Response
    else:
        assert isinstance(response, models.Response), "The response must be a `Response` instance"

        # Validate the result of the response
        result = response.resultado
        assert isinstance(result, models.Result), "The result must be a `Result` instance"
        assert result.descripcion == "Correcto", "Result description '{}' must be 'Correcto'".format(result.descripcion)
        assert result.codigo == 0, "Result codigo '{}' must be '0'".format(result.codigo)


with description('A new'):
    with before.each:
        self.config = {
            'certificate': OUR_CERT,
            'environment': "staging",
        }
        self.face = FACe(**self.config)

    with context('FACe instance'):
        with context('initialization'):
            with it('must work'):
                face = FACe(**self.config)

                config = dict(self.config)
                config['certificate'] = 'fake-path/fake-cert.pem'
                excepts = False
                try:
                    face = FACe(**config)
                except:
                    excepts = True
                assert excepts, "FACe init with an incorrect debug mode must not work"


            with it('must handle debug mode'):
                config = dict(self.config)
                config['debug'] = True
                face = FACe(**config)
                assert face.debug == config['debug']

                config = dict(self.config)
                config['debug'] = "WRONG-DEBUG"
                excepts = False
                try:
                    face = FACe(**config)
                except:
                    excepts = True
                assert excepts, "FACe init with an incorrect debug mode must not work"


            with it('must handle environment definition'):
                config = dict(self.config)
                config['environment'] = "prod"
                face = FACe(**config)
                assert face.environment == config['environment']

                config = dict(self.config)
                config['environment'] = "WRONG-ENV"
                excepts = False
                try:
                    face = FACe(**config)
                except:
                    excepts = True
                assert excepts, "FACe init with an incorrect env must not work"


            with it('action list nifs must work'):
                call = self.face.nifs.list()

                # Validate the response
                response = call.data
                validate_response(response)

                # Validate the nifs


            with it('action send invoice must work'):
                the_invoice = TEST_INVOICE
                call = self.face.invoices.send(invoice=the_invoice)

                # Validate the response
                response = call.data
                validate_response(response, model="invoice")
                assert response.is_ok, "Cancel a valid invoice must work"


            with it('action cancel invoice must work'):
                # Send a dummy invoice, just to fetch their invoice id
                the_invoice = TEST_INVOICE
                call = self.face.invoices.send(invoice=the_invoice)
                response = call.data
                validate_response(response, model="invoice")

                # Fetch the invoice number and cancel it
                invoice_number = response.factura.numeroRegistro
                call = self.face.invoices.cancel(invoice=str(invoice_number), reason="Incorrect submission")

                response = call.data
                validate_response(response, model="invoice")
                assert response.is_ok, "Cancel a valid invoice must work"

                # Test that an invalid invoice_number do not works
                invoice_number = "invalidFixNumber"
                call = self.face.invoices.cancel(invoice=str(invoice_number), reason="Incorrect submission")

                response = call.data
                validate_response(response, model="invoice")
                assert not response.is_ok, "Cancel an invalid invoice must not work"


            with it('action list administrations must work'):
                call = self.face.administrations.list()

                # Validate the response
                response = call.data
                assert response.is_ok, "List administrations must work"

                validate_response(response, model="administrations")
                validate_response(response['administraciones'], model="administrations_list")
                validate_response(response['administraciones']['administracion'], model="administration")
                validate_response(response['administraciones']['administracion'][0], model="administration_code")
                validate_response(response['administraciones']['administracion'][0], model="administration_name")


            with it('action list invoice states must work'):
                call = self.face.invoices.list_states()

                # Validate the response
                response = call.data
                assert response.is_ok, "List invoices states must work"

                validate_response(response, model="statuses")
                validate_response(response['estados'], model="statuses_list")
                validate_response(response['estados']['estado'], model="status")
                validate_response(response['estados']['estado'][0], model="status_code")
                validate_response(response['estados']['estado'][0], model="status_name")
                validate_response(response['estados']['estado'][0], model="status_description")

            """

            with it('action list invoice states must work'):
                call = self.face.invoices.list_states()

                # Validate the response
                response = call.data
                assert response.is_ok, "List invoices states must work"

                validate_response(response, model="statuses")
                validate_response(response['estados'], model="statuses_list")
                validate_response(response['estados']['estado'], model="status")
                validate_response(response['estados']['estado'][0], model="status_code")
                validate_response(response['estados']['estado'][0], model="status_name")
                validate_response(response['estados']['estado'][0], model="status_description")


            """
