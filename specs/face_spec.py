# -*- coding: utf-8 -*-
from face import FACe, models

OUR_CERT = "certs/our_cert.pem"
TEST_INVOICE = 'specs/factura-prueba-v1-2-0.xsig'


models_by_base_field = {
    "resultado": models.Result,
    "factura": {
        "response": models.invoice.Invoice,
        "content": models.invoice.InvoiceResponse,
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

        # Validate the response
        assert isinstance(response, expected_response_model), "The response must be a `{}` instance".format(response, expected_response_model)

        # Validate the internal component of this response
        component = response[model]
        assert isinstance(component, expected_content_model), "The data '{}' must be a `{}` instance".format(component, models_by_base_field[model])

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
            """
            with it('must work'):
                ""
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
                call = self.face.list_nifs()

                # Validate the response
                response = call.data
                validate_response(response)

                # Validate the nifs

            """

            with it('action send invoice must work'):
                the_invoice = TEST_INVOICE
                call = self.face.send_invoice(invoice=the_invoice)

                # Validate the response
                response = call.data
                validate_response(response, model="factura")

                print (response)
                print (response.resultado.codigo)
                print (response.factura.numeroFactura)

                # Validate the result of the send

            """
            with it('action cancel invoice must work'):
                the_invoice = TEST_INVOICE
                call = self.face.send_invoice(invoice=the_invoice)

                response = call.data
                validate_response(response)

                print (response)
                the_invoice_to_cancel = response

                # Validate the result of the send
            """
