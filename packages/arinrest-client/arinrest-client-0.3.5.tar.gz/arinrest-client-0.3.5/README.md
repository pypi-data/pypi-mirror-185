# ARINREST LIB

The purpose of this package is to manage and query resources hosted by ARIN.
ARIN has 3 different services that you can query and manage records on. 

- whois, only the RDAP interface is supported by this library
- IRR, This still needs to be implemented 
- RPKI, The reason I start this library os to manage ROA objects hosted in
  ARINs repository.

## Usage
The entry point into this library is the `ArinRest` class. The class only takes
an API Key from ARIN to instantiate.

```python
from arinrest import ArinRest
from arinrest.rpki import ROA

arinclient = ArinRest('your-api-key-here')

# arinclient.rdap() creates a rdap session with ARIN
whois_client = arinclient.rdap()

# You can manage resources in the IRR and RPKI endpoints so currently the classes
# require an API key to instantiate them.

# create an rpki session with signing capabilities, private key required
rpki_client = arin.rpki("/path/to/private/key")

# add a ROA to the queue to be submitted as well as signing it.
rpki_client.add_roa(roa: ROA)

# submit the ROA to ARIN
rpki_clinet.submit_roas()

```
## TODO
Break out the rpki client and the ROA object into 2 separate classes.

 ~~- ROA object will have getters and setters for the attributes with validation~~
  ~~of values.~~

- rpki client will have the connection and url's needed to submit and fetch
  information about ROAs.

- ARIN may have created certificate with the wrong public key in it that is
  used to identify the resources we have the right to manage. 

  - Certificate creation ticket ARIN-20221019-X541735
    - The public key in this ticket is the same as the stored key in pwdb
    - I have used the key pair to sign a message and verify the signature
      locally
    - The public key in the ticket does not match the public key in the
      x.509 certificate.
    - When submitting an ROA request it complains about a bad Public Key.

    ```xml
        <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <error xmlns="http://www.arin.net/regrws/core/v1">
            <additionalInfo/><code>E_ENTITY_VALIDATION</code>
            <components>
                <component>
                    <message>The public key you entered is invalid.</message>
                    <name>signedRoaRequest</name>
                </component>
            </components>
            <message>Payload entity failed to validate; see component messages for details.</message>
        </error>
    ```



## Resources
Manually signed ROA: Implemented in Python
[ARIN Manually signed ROA](https://www.arin.net/resources/manage/rpki/roa_request/#manually-sign)

RSA Signing with cryptography python lib
[RSA](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#signing)
