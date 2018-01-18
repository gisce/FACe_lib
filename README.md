# FACe lib

It provides a FACe interface to simplify the interaction with the FACe's WS

## Usage

Initialize the face interface passing the desired *PEM* certificate and an email
to receive notifications from FACe servers:

```
from face import FACe

our_certificate = 'path_to/cert.pem'

face = FACe(certificate=our_certificate, email='example@example.com')
```

Call the requested service (see all available methods), ie:

```
result = face.list_nifs()
```

## Integrated FACe services
- [x] [List NIFs](#list-nifs)
- [x] [Send Invoice](#send-invoice)

### List NIFs
```
result = face.list_nifs()
print (result.errors)
print (result.data)
```


### Send Invoice
```
result = face.send_invoice(invoice="an_invoice.xsig")
print (result.errors)
print (result.data)
```
