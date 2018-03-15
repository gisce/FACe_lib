# FACe lib

It provides a FACe interface to simplify the interaction with the FACe's WS


## How to install

Just install it using pip:

``` 
$ pip install FACe_lib
``` 

## Usage

Initialize the face interface passing the desired *PEM* certificate and an email
to receive notifications from FACe servers:

```
from face.face import FACe

our_certificate = 'path_to/cert.pem'

face = FACe(certificate=our_certificate, email='example@example.com')
```

Call the requested service (see all available methods), ie:

```
result = face.nifs.list()
```

## Integrated FACe services
- [Invoices](#invoices)
    - [x] [Fetch Invoice](#fetch-invoice)
    - [x] [Send Invoice](#send-invoice)
    - [x] [Cancel Invoice](#cancel-invoice)
    - [x] [List Invoice Status](#list-invoice-states)
- [Administration](#Administration)
    - [x] [List administrations](#list-administrations)
- [NIFs](#NIFs)
    - [x] [List NIFs](#list-nifs)


### Invoices
#### Fetch Invoice
```
result = face.invoices.fetch(invoice="213091309123")
print (result.errors)
print (result.data)
```

#### Send Invoice
```
result = face.invoices.send(invoice="an_invoice.xsig")
print (result.errors)
print (result.data)
```

#### Cancel Invoice
```
result = face.invoices.send(invoice="213091309123", reason="Mistake at generation process")
print (result.errors)
print (result.data)

```
#### List Invoice States
```
result = face.invoices.list_states(invoice="213091309123")
print (result.errors)
print (result.data)
```


### Administrations
#### List Administrations
```
result = face.administrations.list()
print (result.errors)
print (result.data)
```

### NIFs
#### List NIFs
```
result = face.nifs.list()
print (result.errors)
print (result.data)
```

