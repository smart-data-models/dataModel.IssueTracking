from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    EmailStr,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Datatype(Enum):
    string = 'string'
    number = 'number'
    datetime = 'datetime'
    singlevaluelist = 'singlevaluelist'
    multivaluelist = 'multivaluelist'


class Value(BaseModel):
    key: Optional[float] = None
    name: Optional[str] = None


class Attribute(BaseModel):
    code: Optional[str] = None
    datatype: Optional[Datatype] = None
    datatype_description: Optional[str] = None
    description: Optional[str] = None
    order: Optional[confloat(ge=1.0)] = None
    required: Optional[bool] = None
    values: Optional[List[Value]] = None
    variable: Optional[bool] = None


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Status(Enum):
    closed = 'closed'
    open = 'open'


class Type6(Enum):
    service_requests = 'service_requests'


class ServiceRequests(BaseModel):
    account_id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='The unique ID for the user account of the person submitting the request',
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    address_string: Optional[str] = Field(
        None,
        description='Human entered address or description of location. This is required if no lat/long or address_id are provided. This should be written from most specific to most general geographic unit, eg address number or cross streets, street name, neighborhood/district, city/town/village, county, postal code',
    )
    agency_responsible: Optional[str] = Field(
        None,
        description='Please note that this is semantically equivalent to the provider property (name subproperty) of schema.org',
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    attributes: Optional[List[Attribute]] = Field(
        None, description='Variable attributes of the request response'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    device_id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='The unique device ID of the device submitting the request. This is usually only used for mobile devices',
    )
    email: Optional[EmailStr] = Field(None, description='Email address of owner')
    expected_datetime: Optional[str] = Field(
        None,
        description='The date and time when the service request can be expected to be fulfilled. This may be based on a service-specific service level agreement',
    )
    first_name: Optional[str] = Field(
        None, description='Given name. In the U.S., the first name of a Person'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    jurisdiction_id: Optional[str] = Field(
        None, description='The unique ID of the legal entity of the service (i.e. city)'
    )
    last_name: Optional[str] = Field(
        None, description='Family name. In the U.S., the last name of a Person'
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    media_url: Optional[str] = Field(
        None, description='A URL to media associated with the request, eg an image'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    phone: Optional[str] = Field(None, description='The telephone number')
    requested_datetime: Optional[str] = Field(
        None, description='The date and time when the service request was made'
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    service_code: Optional[str] = Field(
        None, description='The unique identifier for the service request type'
    )
    service_name: Optional[str] = Field(
        None, description='The human readable name of the service request type'
    )
    service_notice: Optional[str] = Field(
        None,
        description='Information about the action expected to fulfill the request or otherwise address the information reported',
    )
    service_request_id: Optional[str] = Field(
        None, description='The unique ID of the service request created'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    status: Optional[Status] = Field(
        None,
        description="Allows one to search for requests which have a specific status. This defaults to all statuses; can be declared multiple times, comma delimited. Enum:'open, closed'",
    )
    status_notes: Optional[str] = Field(
        None,
        description='Explanation of why status was changed to current state or more details on current status than conveyed with status alone',
    )
    type: Optional[Type6] = Field(
        None,
        description="NGSI Entity type. It has to be service_requests. Enum:'service_requests'",
    )
    updated_datetime: Optional[str] = Field(
        None,
        description='The date and time when the service request was last modified. For requests with status=closed, this will be the date the request was closed',
    )
