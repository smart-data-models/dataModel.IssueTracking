Entity: Open311_ServiceRequest  
==============================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **An entity of type ServiceRequest is an acceptable Open 311 service request. Such entity encompasses all the properties defined by Open 311 at POST Service Request and GET Service Request.**  

## List of properties  

- `address`: The mailing address.  - `agency_responsible`: Please note that this is semantically equivalent to the provider property (name subproperty) of schema.org  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `device_id`: The unique device ID of the device submitting the request. This is usually only used for mobile devices  - `email`: Email address of owner.  - `expected_datetime`: The date and time when the service request can be expected to be fulfilled. This may be based on a service-specific service level agreement  - `first_name`: Given name. In the U.S., the first name of a Person.  - `id`: Unique identifier of the entity  - `jurisdiction_id`: The unique ID of the legal entity of the service (i.e. city).  - `last_name`: Family name. In the U.S., the last name of a Person.  - `location`:   - `media_url`: A URL to media associated with the request, eg an image  - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `phone`: Given name. The telephone number.  - `requested_datetime`: The date and time when the service request was made  - `seeAlso`: list of uri pointing to additional resources about the item  - `service_code`: The unique identifier for the service request type.  - `service_name`: The human readable name of the service request type.  - `service_notice`: Information about the action expected to fulfill the request or otherwise address the information reported.  - `service_request_id`: The unique ID of the service request created.  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `status`: Allows one to search for requests which have a specific status. This defaults to all statuses; can be declared multiple times, comma delimited. Enum:'open, closed'  - `status_notes`: Explanation of why status was changed to current state or more details on current status than conveyed with status alone.  - `type`: NGSI Entity type. It has to be Open311ServiceRequest  - `updated_datetime`: The date and time when the service request was last modified. For requests with status=closed, this will be the date the request was closed    
Required properties  
- `id`  - `type`    
An entity of type `ServiceRequest` is an acceptable Open 311 service request. Such entity encompasses all the properties defined by Open 311 at [POST Service Request](http://wiki.open311.org/GeoReport_v2/#post-service-request) and [GET Service Request](http://wiki.open311.org/GeoReport_v2/#get-service-request). Using this data model and a FIWARE NGSI version 2 implementation it is straightforward to implement a service compliant with the Open 311 specifications.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Open311_ServiceRequest:    
  description: 'An entity of type ServiceRequest is an acceptable Open 311 service request. Such entity encompasses all the properties defined by Open 311 at POST Service Request and GET Service Request.'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/Text'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/Text'''    
          type: string    
        areaServed:    
          description: 'Property. The geographic area where a service or offered item is provided. Model:''https://schema.org/Text'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, Spain. Model:''https://schema.org/Text'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/Text'''    
          type: string    
      type: Property    
    agency_responsible:    
      description: 'Please note that this is semantically equivalent to the provider property (name subproperty) of schema.org'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/provider    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    device_id:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'The unique device ID of the device submitting the request. This is usually only used for mobile devices'    
      type: Relationship    
      x-ngsi:    
        model: https://schema.org/URL    
    email:    
      description: 'Email address of owner.'    
      format: idn-email    
      type: Property    
    expected_datetime:    
      description: 'The date and time when the service request can be expected to be fulfilled. This may be based on a service-specific service level agreement'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    first_name:    
      description: 'Given name. In the U.S., the first name of a Person.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    id:    
      anyOf: &open311_servicerequest_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    jurisdiction_id:    
      description: 'The unique ID of the legal entity of the service (i.e. city).'    
      type: Property    
    last_name:    
      description: 'Family name. In the U.S., the last name of a Person.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      title: 'GeoJSON Geometry'    
    media_url:    
      description: 'A URL to media associated with the request, eg an image'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *open311_servicerequest_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    phone:    
      description: 'Given name. The telephone number.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    requested_datetime:    
      description: 'The date and time when the service request was made'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    service_code:    
      description: 'The unique identifier for the service request type.'    
      type: Property    
    service_name:    
      description: 'The human readable name of the service request type.'    
      type: Property    
    service_notice:    
      description: 'Information about the action expected to fulfill the request or otherwise address the information reported.'    
      type: Property    
    service_request_id:    
      description: 'The unique ID of the service request created.'    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    status:    
      description: 'Allows one to search for requests which have a specific status. This defaults to all statuses; can be declared multiple times, comma delimited. Enum:''open, closed'''    
      enum:    
        - closed    
        - open    
      type: Property    
    status_notes:    
      description: 'Explanation of why status was changed to current state or more details on current status than conveyed with status alone.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Open311ServiceRequest'    
      enum:    
        - Open311ServiceRequest    
      type: Property    
    updated_datetime:    
      description: 'The date and time when the service request was last modified. For requests with status=closed, this will be the date the request was closed'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Example payloads    
#### Open311_ServiceRequest NGSI V2 key-values Example    
Here is an example of a Open311_ServiceRequest in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "service-request:638344",  
  "type": "Open311ServiceRequest",  
  "service_request_id": 638344,  
  "status": "closed",  
  "status_notes": "Duplicate request.",  
  "service_name": "Aceras",  
  "service_code": 234,  
  "description": "Acera en mal estado con bordillo partido en dos",  
  "agency_responsible": "Ayuntamiento de Ciudad",  
  "requested_datetime": "2010-04-14T06:37:38-08:00",  
  "updated_datetime": "2010-04-14T06:37:38-08:00",  
  "expected_datetime": "2010-04-15T06:37:38-08:00",  
  "address_string": "Calle San Juan Bautista, 2",  
  "attributes": {  
    "ISSUE_TYPE": ["Bordillo"]  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [-3.164485591715449, 40.62785133667262]  
  },  
  "media_url": "http://exaple.org/media/638344.jpg"  
}  
```  
#### Open311_ServiceRequest NGSI V2 normalized Example    
Here is an example of a Open311_ServiceRequest in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "service-request:638344",  
  "type": "Open311ServiceRequest",  
  "status": {  
    "value": "closed"  
  },  
  "description": {  
    "value": "Acera en mal estado con bordillo partido en dos"  
  },  
  "service_code": {  
    "value": 234  
  },  
  "status_notes": {  
    "value": "Duplicate request."  
  },  
  "service_name": {  
    "value": "Aceras"  
  },  
  "service_request_id": {  
    "value": 638344  
  },  
  "updated_datetime": {  
    "type": "DateTime",  
    "value": "2010-04-14T06:37:38-08:00"  
  },  
  "address_string": {  
    "value": "Calle San Juan Bautista, 2"  
  },  
  "requested_datetime": {  
    "type": "DateTime",  
    "value": "2010-04-14T06:37:38-08:00"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [-3.164485591715449, 40.62785133667262]  
    }  
  },  
  "attributes": {  
    "value": {  
      "ISSUE_TYPE": ["Bordillo"]  
    }  
  },  
  "expected_datetime": {  
    "type": "DateTime",  
    "value": "2010-04-15T06:37:38-08:00"  
  },  
  "agency_responsible": {  
    "value": "Ayuntamiento de Ciudad"  
  },  
  "media_url": {  
    "value": "http://exaple.org/media/638344.jpg"  
  }  
}  
```  
#### Open311_ServiceRequest NGSI-LD key-values Example    
Here is an example of a Open311_ServiceRequest in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "address_string": "Calle San Juan Bautista, 2",  
 "agency_responsible": "Ayuntamiento de Ciudad",  
 "attributes": {"ISSUE_TYPE": ["Bordillo"]},  
 "description": "Acera en mal estado con bordillo partido en dos",  
 "expected_datetime": {"@type": "DateTime",  
                       "@value": "2010-04-15T06:37:38-08:00Z"},  
 "id": "urn:ngsi-ld:Open311ServiceRequest:service-request:638344",  
 "location": {"coordinates": [-3.164485591715449, 40.62785133667262],  
              "type": "Point"},  
 "media_url": "http://exaple.org/media/638344.jpg",  
 "requested_datetime": {"@type": "DateTime",  
                        "@value": "2010-04-14T06:37:38-08:00"},  
 "service_code": 234,  
 "service_name": "Aceras",  
 "service_request_id": 638344,  
 "status": "closed",  
 "status_notes": "Duplicate request.",  
 "type": "Open311ServiceRequest",  
 "updated_datetime": {"@type": "DateTime",  
                      "@value": "2010-04-14T06:37:38-08:00"}}  
```  
#### Open311_ServiceRequest NGSI-LD normalized Example    
Here is an example of a Open311_ServiceRequest in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:Open311ServiceRequest:service-request:638344",  
    "type": "Open311ServiceRequest",  
    "status": {  
        "type": "Property",  
        "value": "closed"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Acera en mal estado con bordillo partido en dos"  
    },  
    "service_code": {  
        "type": "Property",  
        "value": 234  
    },  
    "status_notes": {  
        "type": "Property",  
        "value": "Duplicate request."  
    },  
    "service_name": {  
        "type": "Property",  
        "value": "Aceras"  
    },  
    "service_request_id": {  
        "type": "Property",  
        "value": 638344  
    },  
    "updated_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-14T06:37:38-08:00"  
        }  
    },  
    "address_string": {  
        "type": "Property",  
        "value": "Calle San Juan Bautista, 2"  
    },  
    "requested_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-14T06:37:38-08:00"  
        }  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -3.164485591715449,  
                40.62785133667262  
            ]  
        }  
    },  
    "attributes": {  
        "type": "Property",  
        "value": {  
            "ISSUE_TYPE": [  
                "Bordillo"  
            ]  
        }  
    },  
    "expected_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-15T06:37:38-08:00Z"  
        }  
    },  
    "agency_responsible": {  
        "type": "Property",  
        "value": "Ayuntamiento de Ciudad"  
    },  
    "media_url": {  
        "type": "Property",  
        "value": "http://exaple.org/media/638344.jpg"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
