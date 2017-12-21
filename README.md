# FACe lib

It provides a FACe interface to simplify the interaction with the FACe's WS

## Usage

Initialize the face interface passing the desired *PEM* certificate:

```
from face import FACe

our_certificate = 'path_to/cert.pem'

face = FACe(certificate=our_certificate)
```

Call the requested service (see all available methods), ie:

```
result = face.nifs.list()
```

## Integrated FACe services
- [x] [List NIFs](#list-nifs)
- [x] [Send Invoice](#send-invoice)

### List NIFs
```
result = face.nifs.list()
print (result.errors)
print (result.data)
```


### Send Invoice
```
result = face.invoices.send(invoice="an_invoice.xsig")
print (result.errors)
print (result.data)
```
