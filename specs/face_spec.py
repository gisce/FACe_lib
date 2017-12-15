from face import FACe

OUR_CERT = "certs/our_cert.pem"

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
                #self.face.list_nifs()
                pass
