from face import FACe

OUR_CERT = "certs/our_cert.pem"

with description('A new'):
    with before.each:
        self.config = {
            'certificate': OUR_CERT,
        }
        self.face = FACe(**self.config)

    with context('FACe instance'):
        with it('must be initialized properly'):
            face = FACe(**self.config)

        with it('action list nifs must work'):
            self.face.list_nifs()
