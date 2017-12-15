# -*- coding: utf-8 -*-
from face import FACe, models

OUR_CERT = "certs/our_cert.pem"
TEST_INVOICE = 'specs/factura-prueba-v1-2-0.xsig'

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
                call = self.face.list_nifs()

                # Validate the response
                response = call.data
                assert isinstance(response, models.Response), "The response must be a `Response` instance"

                # Validate the result of the response
                result = response.resultado
                assert isinstance(result, models.Result), "The result must be a `Result` instance"


            with it('action send invoice must work'):
                the_invoice = TEST_INVOICE
                call = self.face.send_invoice(invoice=the_invoice)

                # Validate the response
                response = call.data
                assert isinstance(response, models.Response), "The response must be a `Response` instance"

                # Validate the result of the response
                result = response.resultado
                assert isinstance(result, models.Result), "The result must be a `Result` instance"
