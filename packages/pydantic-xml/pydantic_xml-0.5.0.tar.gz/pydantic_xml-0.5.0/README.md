[![Downloads][download-badge]][download-url]
[![License][licence-badge]][licence-url]
[![Python Versions][python-version-badge]][python-version-url]
[![Test Status][test-badge]][test-url]
[![Test Coverage][test-cov-badge]][test-cov-url]

[download-badge]: https://static.pepy.tech/personalized-badge/pydantic-xml?period=month&units=international_system&left_color=grey&right_color=orange&left_text=Downloads/month
[download-url]: https://pepy.tech/project/pydantic-xml
[licence-badge]: https://img.shields.io/badge/license-Unlicense-blue.svg
[licence-url]: https://github.com/dapper91/pydantic-xml/blob/master/LICENSE
[python-version-badge]: https://img.shields.io/pypi/pyversions/pydantic-xml.svg
[python-version-url]: https://pypi.org/project/pydantic-xml
[test-badge]: https://github.com/dapper91/pydantic-xml/actions/workflows/test.yml/badge.svg?branch=master
[test-url]: https://github.com/dapper91/pydantic-xml/actions/workflows/test.yml
[test-cov-badge]: https://codecov.io/gh/dapper91/pydantic-xml/branch/master/graph/badge.svg
[test-cov-url]: https://codecov.io/gh/dapper91/pydantic-xml

# pydantic-xml

pydantic xml extension


## Installation

```commandline
pip install pydantic-xml[lxml]
```

* **lxml** - use `lxml` instead of standard `xml.etree.ElementTree` library

## Quickstart

`pydantic-xml` is a pydantic extension implementing model xml serialization/deserialization.
It is closely integrated with `pydantic` which means it supports most of the `pydantic` features.

All xml serializable/deserializable models should be inherited from `BaseXmlModel` base class.
`BaseXmlModel` implements method `to_xml` to serialize an object to an xml string and `from_xml` to deserialize it.
Model field data could be extracted from xml attribute, element or text. Field data location is derived
using the following rules:

* fields of primitive types (`int`, `float`, `str`, `datetime`, ...) are extracted from element text by default.
  To alter the default behaviour the field should be marked as `attr` or `element`.

```python
class Company(BaseXmlModel):
    trade_name: str = attr(name='trade-name') # extracted from the 'trade-name' attribute
    website: HttpUrl = element() # extracted from the 'website' element text
    description: str # extracted from the root element text
```

```xml
<Company trade-name="SpaceX">
    company description text
    <website>https://www.spacex.com</website>
</Company>
```

* fields of model types are extracted from an element.

```python
class Headquarters(BaseXmlModel):
    country: str = element()
    state: str = element()
    city: str = element()


class Company(BaseXmlModel):
    headquarters: Headquarters
```

```xml
<Company>
    <headquarters>
        <country>US</country>
        <state>California</state>
        <city>Hawthorne</city>
    </headquarters>
</Company>
```

* fields of mapping types are extracted from the current element attributes (by default)
  or from a nested element attributes if the field is marked as `element`.

```python
class Company(BaseXmlModel):
    company_attributes: Dict[str, str]
    founder_attributes: Dict[str, str] = element(tag='Founder')
```

```xml
<Company trade-name="SpaceX" type="Private">
    <Founder name="Elon" surname="Musk"/>
</Company>
```

* fields of collection types (`list`, `tuple`, `set`, ...) are extracted from multiple elements with the same name.

```python
class Product(BaseXmlModel):
    status: Literal['running', 'development'] = attr()
    launched: Optional[int] = attr()
    title: str


class Company(BaseXmlModel):
    products: List[Product] = element(tag='product')
```

```xml
<Company>
    <product status="running" launched="2013">Several launch vehicles</product>
    <product status="running" launched="2019">Starlink</product>
    <product status="development">Starship</product>
</Company>
```

* wrapped fields are extracted from a sub-element located at the provided path.

```python
class Social(BaseXmlModel):
    type: str = attr()
    url: str


class Company(BaseXmlModel):
    socials: List[Social] = wrapped('contacts/socials', element(tag='social'))
```

```xml
<Company>
    <contacts>
        <socials>
            <social type="linkedin">https://www.linkedin.com/company/spacex</social>
            <social type="twitter">https://twitter.com/spacex</social>
            <social type="youtube">https://www.youtube.com/spacex</social>
        </socials>
    </contacts>
</Company>
```

The following example illustrates all previously described rules in conjunction with some `pydantic` feature:

*company.xml:*

```xml
<Company trade-name="SpaceX" type="Private" xmlns:pd="http://www.test.com/prod">
    <Founder name="Elon" surname="Musk"/>
    <Founded>2002-03-14</Founded>
    <Employees>12000</Employees>
    <WebSite>https://www.spacex.com</WebSite>

    <Industries>
        <Industry>space</Industry>
        <Industry>communications</Industry>
    </Industries>

    <key-people>
        <person position="CEO" name="Elon Musk"/>
        <person position="CTO" name="Elon Musk"/>
        <person position="COO" name="Gwynne Shotwell"/>
    </key-people>

    <hq:headquarters xmlns:hq="http://www.test.com/hq">
        <hq:country>US</hq:country>
        <hq:state>California</hq:state>
        <hq:city>Hawthorne</hq:city>
    </hq:headquarters>

    <co:contacts xmlns:co="http://www.test.com/contact" >
        <co:socials>
            <co:social co:type="linkedin">https://www.linkedin.com/company/spacex</co:social>
            <co:social co:type="twitter">https://twitter.com/spacex</co:social>
            <co:social co:type="youtube">https://www.youtube.com/spacex</co:social>
        </co:socials>
    </co:contacts>

    <pd:product pd:status="running" pd:launched="2013">Several launch vehicles</pd:product>
    <pd:product pd:status="running" pd:launched="2019">Starlink</pd:product>
    <pd:product pd:status="development">Starship</pd:product>
</Company>
```

*main.py:*

```python
from datetime import date
from enum import Enum
from typing import Dict, List, Optional, Set, Literal, Tuple

import pydantic as pd
from pydantic import conint, HttpUrl

from pydantic_xml import BaseXmlModel, attr, element, wrapped

NSMAP = {
    'co': 'http://www.test.com/contact',
    'hq': 'http://www.test.com/hq',
    'pd': 'http://www.test.com/prod',
}


class Headquarters(BaseXmlModel, ns='hq', nsmap=NSMAP):
    country: str = element()
    state: str = element()
    city: str = element()

    @pd.validator('country')
    def validate_country(cls, value: str) -> str:
        if len(value) > 2:
            raise ValueError('country must be of 2 characters')
        return value


class Industries(BaseXmlModel):
    __root__: Set[str] = element(tag='Industry')


class Social(BaseXmlModel, ns_attrs=True, ns='co', nsmap=NSMAP):
    type: str = attr()
    url: str


class Product(BaseXmlModel, ns_attrs=True, ns='pd', nsmap=NSMAP):
    status: Literal['running', 'development'] = attr()
    launched: Optional[int] = attr()
    title: str


class Person(BaseXmlModel):
    name: str = attr()


class CEO(Person):
    position: Literal['CEO'] = attr()


class CTO(Person):
    position: Literal['CTO'] = attr()


class COO(Person):
    position: Literal['COO'] = attr()


class Company(BaseXmlModel, tag='Company', nsmap=NSMAP):
    class CompanyType(str, Enum):
        PRIVATE = 'Private'
        PUBLIC = 'Public'

    trade_name: str = attr(name='trade-name')
    type: CompanyType = attr()
    employees: conint(gt=0) = element(tag='Employees')
    website: HttpUrl = element(tag='WebSite')

    founder: Dict[str, str] = element(tag='Founder')
    founded: Optional[date] = element(tag='Founded')
    industries: Industries = element(tag='Industries')

    key_people: Tuple[CEO, CTO, COO] = wrapped('key-people', element(tag='person'))
    headquarters: Headquarters
    socials: List[Social] = wrapped(
        'contacts/socials',
        element(tag='social', default_factory=list),
        ns='co',
        nsmap=NSMAP,
    )

    products: Tuple[Product, ...] = element(tag='product', ns='pd')


with open('company.xml') as file:
    document = file.read()

company = Company.from_xml(document)

print(company)

```

### Name resolution:

**TBD**


### Namespace resolution:

#### Default namespace

To parse xml documents with a declared default namespace add it to `nsmap`  with an empty key.
Look at the following example:

```xml
<headquarters xmlns="http://www.test.com/hq">
    <country>US</country>
    <state>California</state>
    <city>Hawthorne</city>
</headquarters>
```

```python
class Headquarters(BaseXmlModel, tag='headquarters', nsmap={'': 'http://www.test.com/hq'}):
    country: str = element()
    state: str = element()
    city: str = element()
```

**TBD**


### Generics:

`pydantic` library supports [generic-models](https://pydantic-docs.helpmanual.io/usage/models/#generic-models).
`pydantic-xml` supports it either. To declare one inherit your model from `BaseGenericXmlModel`,
the rest is the same as `pydantic` generic model declaration.

The following example illustrates it:

*request.xml:*

```xml
<request service-name="api-gateway"
         request-id="27765d90-f3ef-426f-be9d-8da2b405b4a9"
         timestamp="2019-06-12T12:21:34.123+00:00">
    <auth type="basic">
        <user>gw</user>
        <password>secret</password>
    </auth>
    <payload type="rpc">
        <method>crete_event</method>
        <param name="timestamp">1660892066.1952798</param>
        <param name="user">admin</param>
        <param name="method">POST</param>
        <param name="resource">https://api-gateway.test.com/api/v1/users</param>
    </payload>
</request>
```

*main.py:*

```python
import datetime as dt
from typing import Generic, Optional, Tuple, TypeVar

from pydantic import HttpUrl

import pydantic_xml as pxml


class BasicAuth(pxml.BaseXmlModel):
    type: str = pxml.attr()
    user: str = pxml.element()
    password: str = pxml.element()


AuthType = TypeVar('AuthType')
PayloadType = TypeVar('PayloadType')


class Request(pxml.BaseGenericXmlModel, Generic[AuthType, PayloadType], tag='request'):
    service_name: str = pxml.attr(name='service-name')
    request_id: str = pxml.attr(name='request-id')
    timestamp: dt.datetime = pxml.attr()

    auth: Optional[AuthType]

    payload: PayloadType


ParamsType = TypeVar('ParamsType')
ParamType = TypeVar('ParamType')


class Rpc(pxml.BaseGenericXmlModel, Generic[ParamsType]):
    class Param(pxml.BaseGenericXmlModel, Generic[ParamType]):
        name: str = pxml.attr()
        value: ParamType

    method: str = pxml.element()
    params: ParamsType = pxml.element(tag='param')


with open('request.xml') as file:
    xml = file.read()

request = Request[
    BasicAuth,
    Rpc[
        Tuple[
            Rpc.Param[float],
            Rpc.Param[str],
            Rpc.Param[str],
            Rpc.Param[HttpUrl]
        ]
    ]
].from_xml(xml)

print(request.json(indent=4))
```

*output:*

```json
{
    "service_name": "api-gateway",
    "request_id": "27765d90-f3ef-426f-be9d-8da2b405b4a9",
    "timestamp": "2019-06-12T12:21:34.123000+00:00",
    "auth": {
        "type": "basic",
        "user": "gw",
        "password": "secret"
    },
    "payload": {
        "method": "crete_event",
        "params": [
            {
                "name": "timestamp",
                "value": 1660892066.1952798
            },
            {
                "name": "user",
                "value": "admin"
            },
            {
                "name": "method",
                "value": "POST"
            },
            {
                "name": "resource",
                "value": "https://api-gateway.test.com/api/v1/users"
            }
        ]
    }
}
```


### Self-referencing models:

`pydantic` library supports [self-referencing models](https://pydantic-docs.helpmanual.io/usage/postponed_annotations/#self-referencing-models).
`pydantic-xml` supports it either.

*request.xml:*

```xml
<Directory Name="root" Mode="rwxr-xr-x">
    <Directory Name="etc" Mode="rwxr-xr-x">
        <File Name="passwd" Mode="-rw-r--r--"/>
        <File Name="hosts" Mode="-rw-r--r--"/>
        <Directory Name="ssh" Mode="rwxr-xr-x"/>
    </Directory>
    <Directory Name="bin" Mode="rwxr-xr-x"/>
    <Directory Name="usr" Mode="rwxr-xr-x">
        <Directory Name="bin" Mode="rwxr-xr-x"/>
    </Directory>
</Directory>
```

*main.py:*

```python
from typing import List, Optional

import pydantic_xml as pxml


class File(pxml.BaseXmlModel, tag="File"):
    name: str = pxml.attr(name='Name')
    mode: str = pxml.attr(name='Mode')


class Directory(pxml.BaseXmlModel, tag="Directory"):
    name: str = pxml.attr(name='Name')
    mode: str = pxml.attr(name='Mode')
    dirs: Optional[List['Directory']] = pxml.element(tag='Directory')
    files: Optional[List[File]] = pxml.element(tag='File', default_factory=list)


with open('request.xml') as file:
    xml = file.read()

root = Directory.from_xml(xml)
print(root.json(indent=4))

```

*output:*

```json
{
    "name": "root",
    "mode": "rwxr-xr-x",
    "dirs": [
        {
            "name": "etc",
            "mode": "rwxr-xr-x",
            "dirs": [
                {
                    "name": "ssh",
                    "mode": "rwxr-xr-x",
                    "dirs": [],
                    "files": []
                }
            ],
            "files": [
                {
                    "name": "passwd",
                    "mode": "-rw-r--r--"
                },
                {
                    "name": "hosts",
                    "mode": "-rw-r--r--"
                }
            ]
        },
        {
            "name": "bin",
            "mode": "rwxr-xr-x",
            "dirs": [],
            "files": []
        },
        {
            "name": "usr",
            "mode": "rwxr-xr-x",
            "dirs": [
                {
                    "name": "bin",
                    "mode": "rwxr-xr-x",
                    "dirs": [],
                    "files": []
                }
            ],
            "files": []
        }
    ],
    "files": []
}
```

### JSON

Since `pydantic` supports json serialization, `pydantic-xml` could be used as xml-to-json transcoder:

```python
...

with open('company.xml') as file:
    xml = file.read()

company = Company.from_xml(xml)

print(company.json(indent=4))
```

*output:*

```json
{
    "trade_name": "SpaceX",
    "type": "Private",
    "employees": 12000,
    "website": "https://www.spacex.com",
    "founder": {
        "name": "Elon",
        "surname": "Musk"
    },
    "founded": "2002-03-14",
    "industries": [
        "space",
        "communications"
    ],
    "key_people": [
        {
            "name": "Elon Musk",
            "position": "CEO"
        },
        {
            "name": "Elon Musk",
            "position": "CTO"
        },
        {
            "name": "Gwynne Shotwell",
            "position": "COO"
        }
    ],
    "headquarters": {
        "country": "US",
        "state": "California",
        "city": "Hawthorne"
    },
    "socials": [
        {
            "type": "linkedin",
            "url": "https://www.linkedin.com/company/spacex"
        },
        {
            "type": "twitter",
            "url": "https://twitter.com/spacex"
        },
        {
            "type": "youtube",
            "url": "https://www.youtube.com/spacex"
        }
    ],
    "products": [
        {
            "status": "running",
            "launched": 2013,
            "title": "Several launch vehicles"
        },
        {
            "status": "running",
            "launched": 2019,
            "title": "Starlink"
        },
        {
            "status": "development",
            "launched": null,
            "title": "Starship"
        }
    ]
}
```


### XML parser

`pydantic-xml` tries to use the fastest xml parser in your system. It uses `lxml` if it is installed
in your environment otherwise falls back to the standard library xml parser.


### Custom type serialization

Only several primitive standard type serialization are supported
(`str`, `int`, `float`, `Decimal`, `bool`, `datetime`, `date`, `time`).
To allow custom types serialization `BaseXmlModel.to_xml` method takes an optional encoder as an argument.
A custom one should be inherited from `XmlEncoder`.

The following example illustrate how to implement `bytes` type xml serialization:

*file1.txt:*

```text
hello world!!!
```

*file2.txt:*

```text
test
```

*main.py:*

```python
import base64
from typing import Any, List
from pydantic_xml import BaseXmlModel, XmlEncoder, attr, element


class CustomXmlEncoder(XmlEncoder):
    def encode(self, obj: Any) -> str:
        if isinstance(obj, bytes):
            return base64.b64encode(obj).decode()

        return super().encode(obj)


class File(BaseXmlModel):
    name: str = attr()
    content: bytes = element()


class Files(BaseXmlModel, tag='files'):
    __root__: List[File] = element(tag='file', default=[])


files = Files()
for filename in ['file1.txt', 'file2.txt']:
    with open(filename, 'rb') as f:
        content = f.read()

    files.__root__.append(File(name=filename, content=content))

xml = files.to_xml(encoder=CustomXmlEncoder(), pretty_print=True, encoding='UTF-8', standalone=True)
print(xml.decode())
```

*output:*

```xml
<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<files>
  <file name="file1.txt">
    <content>aGVsbG8gd29ybGQhISE=</content>
  </file>
  <file name="file2.txt">
    <content>dGVzdA==</content>
  </file>
</files>
```


### Data modeling

This section provides examples of the most common use-cases with xml and json outputs.

#### Primitive types:

```python
class Company(BaseXmlModel):
    class CompanyType(str, Enum):
        PRIVATE = 'Private'
        PUBLIC = 'Public'

    trade_name: str = attr(name='trade-name')
    type: CompanyType = attr()  # field name is used as an attribute name by default
    founded: Optional[date] = element(tag='Founded')
```

```xml
<Company trade-name="SpaceX" type="Private">
    <Founded>2002-03-14</Founded>
</Company>
```

```json
{
    "trade_name": "SpaceX",
    "type": "Private",
    "founded": "2002-03-14"
}
```
--------------------------------------------------------------------------------

```python
class Product(BaseXmlModel):
    status: Literal['running', 'development'] = attr()
    launched: Optional[int] = attr()
    title: str  # primitive types are extracted from the element text by default
```

```xml
<Product status="running" launched="2019">Starlink</Product>
```

```json
{
    "status": "running",
    "launched": 2019,
    "title": "Starlink"
}
```
--------------------------------------------------------------------------------


#### Sub-models:

```python
class Headquarters(BaseXmlModel):
    country: str = element()
    state: str = element()
    city: str = element()


class Product(BaseXmlModel):
    status: Literal['running', 'development'] = attr()
    launched: Optional[int] = attr()
    title: str


class Company(BaseXmlModel):
    headquarters: Headquarters  # models are extracted from the element by default
    products: Tuple[Product, ...] = element(tag='product')
```

```xml
<Company>
    <headquarters>
        <country>US</country>
        <state>California</state>
        <city>Hawthorne</city>
    </headquarters>

    <product status="running" launched="2013">Several launch vehicles</product>
    <product status="running" launched="2019">Starlink</product>
    <product status="development">Starship</product>
</Company>
```

```json
{
    "headquarters": {
        "country": "US",
        "state": "California",
        "city": "Hawthorne"
    },
    "products": [
        {
            "status": "running",
            "launched": 2013,
            "title": "Several launch vehicles"
        },
        {
            "status": "running",
            "launched": 2019,
            "title": "Starlink"
        },
        {
            "status": "development",
            "launched": null,
            "title": "Starship"
        }
    ]
}
```
--------------------------------------------------------------------------------

```python
class Founded(BaseXmlModel):
    __root__: datetime.date

class Company(BaseXmlModel):
    founded: Founded = element(tag='Founded')
```

```xml
<Company>
    <Founded>2002-03-14</Founded>
</Company>
```

```json
{
    "founded": "2002-03-14"
}
```
--------------------------------------------------------------------------------


#### Mappings:

```python
class Company(BaseXmlModel):
    founder: Dict[str, str] = element(tag='Founder')
```

```xml
<Company>
    <Founder name="Elon" surname="Musk"/>
</Company>
```

```json
{
    "founder": {
        "name": "Elon",
        "surname": "Musk"
    }
}
```
--------------------------------------------------------------------------------

```python
class Founder(BaseXmlModel):
    __root__: Dict[str, str]  # mappings are extracted from attributes by default
```

```xml
<Founder name="Elon" surname="Musk"/>
```

```json
{
    "name": "Elon",
    "surname": "Musk"
}
```
--------------------------------------------------------------------------------


#### Homogeneous collections:

```python
class Industries(BaseXmlModel):
    __root__: Set[str] = element(tag='industry')


class Social(BaseXmlModel):
    type: str = attr()
    url: str


class Product(BaseXmlModel):
    status: Literal['running', 'development'] = attr()
    launched: Optional[int] = attr()
    title: str


class Company(BaseXmlModel):
    industries: Industries = element()
    socials: List[Social] = element(tag='social', default_factory=list)
    products: Tuple[Product, ...] = element(tag='product')
```

```xml
<Company>
    <industries>
        <industry>space</industry>
        <industry>communications</industry>
    </industries>

    <social type="linkedin">https://www.linkedin.com/company/spacex</social>
    <social type="twitter">https://twitter.com/spacex</social>
    <social type="youtube">https://www.youtube.com/spacex</social>

    <product status="running" launched="2013">Several launch vehicles</product>
    <product status="running" launched="2019">Starlink</product>
    <product status="development">Starship</product>
</Company>
```

```json
{
    "industries": [
        "space",
        "communications"
    ],
    "socials": [
        {
            "type": "linkedin",
            "url": "https://www.linkedin.com/company/spacex"
        },
        {
            "type": "twitter",
            "url": "https://twitter.com/spacex"
        },
        {
            "type": "youtube",
            "url": "https://www.youtube.com/spacex"
        }
    ],
    "products": [
        {
            "status": "running",
            "launched": 2013,
            "title": "Several launch vehicles"
        },
        {
            "status": "running",
            "launched": 2019,
            "title": "Starlink"
        },
        {
            "status": "development",
            "launched": null,
            "title": "Starship"
        }
    ]
}
```
--------------------------------------------------------------------------------


#### Heterogeneous collections:

```python
class Person(BaseXmlModel):
    name: str = attr()


class CEO(Person):
    position: Literal['CEO'] = attr()


class CTO(Person):
    position: Literal['CTO'] = attr()


class COO(Person):
    position: Literal['COO'] = attr()


class Company(BaseXmlModel):
    key_people: Tuple[CEO, CTO, COO] = element(tag='person')
```

```xml
<Company>
    <person position="CEO" name="Elon Musk"/>
    <person position="CTO" name="Elon Musk"/>
    <person position="COO" name="Gwynne Shotwell"/>
</Company>
```

```json
{
    "key_people": [
        {
            "name": "Elon Musk",
            "position": "CEO"
        },
        {
            "name": "Elon Musk",
            "position": "CTO"
        },
        {
            "name": "Gwynne Shotwell",
            "position": "COO"
        }
    ]
}
```
--------------------------------------------------------------------------------


#### Wrapped entities:

```python
class Company(BaseXmlModel):
    hq_country: str = wrapped('headquarters/country')
    hq_state: str = wrapped('headquarters/state')
    hq_city: str = wrapped('headquarters/city')
```

```xml
<Company>
    <headquarters>
        <country>US</country>
        <state>California</state>
        <city>Hawthorne</city>
    </headquarters>
</Company>
```

```json
{
    "hq_country": "US",
    "hq_state": "California",
    "hq_city": "Hawthorne"
}
```
--------------------------------------------------------------------------------


```python
class Social(BaseXmlModel):
    type: str = attr()
    url: str


class Company(BaseXmlModel):
    socials: List[Social] = wrapped('contacts/socials', element(tag='social', default_factory=list))
```

```xml
<Company>
    <contacts>
        <socials>
            <social type="linkedin">https://www.linkedin.com/company/spacex</social>
            <social type="twitter">https://twitter.com/spacex</social>
            <social type="youtube">https://www.youtube.com/spacex</social>
        </socials>
    </contacts>
</Company>
```

```json
{
    "socials": [
        {
            "type": "linkedin",
            "url": "https://www.linkedin.com/company/spacex"
        },
        {
            "type": "twitter",
            "url": "https://twitter.com/spacex"
        },
        {
            "type": "youtube",
            "url": "https://www.youtube.com/spacex"
        }
    ]
}
```
--------------------------------------------------------------------------------

```python
class Company(BaseXmlModel):
    persons: List[Dict[str, str]] = wrapped('key-people', element(tag="person"))
```

```xml
<Company>
    <key-people>
        <person position="CEO" name="Elon Musk"/>
        <person position="CTO" name="Elon Musk"/>
        <person position="COO" name="Gwynne Shotwell"/>
    </key-people>
</Company>
```

```json
{
    "persons": [
        {
            "position": "CEO",
            "name": "Elon Musk"
        },
        {
            "position": "CTO",
            "name": "Elon Musk"
        },
        {
            "position": "COO",
            "name": "Gwynne Shotwell"
        }
    ]
}
```
--------------------------------------------------------------------------------
