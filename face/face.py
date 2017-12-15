# -*- coding: utf-8 -*-
from FACe_signer import FACe_signer
import zeep

# FACe environments
FACE_ENVS = {
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl",
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
}

class FACe(object):
    def __init__(self, **kwargs):
        assert "certificate" in kwargs, "The certificate for requests signing must be defined"
        self.certificate = kwargs['certificate']

        # initialize a ZEEP client with the desired FACe envs
        self.client = zeep.Client(
            FACE_ENVS['staging'],
            plugins=[FACe_signer(self.certificate, debug=True)]
        )

    def list_nifs(self):
        self.client.service.consultarNIFs()
