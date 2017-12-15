# -*- coding: utf-8 -*-
from FACe_signer import FACe_signer
import zeep
import os.path

# FACe environments
FACE_ENVS = {
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl",
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
}

class FACe(object):
    """
    FACe object

    Prepare an interface to reach FACe webservices
    """
    def __init__(self, **kwargs):
        """
        Initializes a FACe instance using Zeep with FACe signature plugin using the requested certificate.
        """
        assert "certificate" in kwargs and type(kwargs['certificate']) == str, "The certificate filename for requests signing must be defined"
        assert os.path.isfile(kwargs['certificate']), "Provided certificate do not exist (or not enought permissions to read it)"
        self.certificate = kwargs['certificate']

        # Handle debug, df "False"
        self.debug = False
        if 'debug' in kwargs:
            assert type(kwargs['debug']) == bool, "debug argument must be a boolean"
            self.debug = kwargs['debug']

        # Handle environment, df "prod"
        self.environment = "prod"
        if 'environment' in kwargs:
            assert type(kwargs['environment']) == str, "environment argument must be an string"
            assert kwargs['environment'] in FACE_ENVS.keys(), "Provided environment '{}' not recognized in defined FACE_ENVS {}".format(kwargs['environment'], str(FACE_ENVS.keys()))
            self.environment = kwargs['environment']


        # initialize a ZEEP client with the desired FACe envs
        self.client = zeep.Client(
            FACE_ENVS[self.environment],
            plugins=[FACe_signer(self.certificate, debug=self.debug)]
        )

    def list_nifs(self):
        self.client.service.consultarNIFs()
