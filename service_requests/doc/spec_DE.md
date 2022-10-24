<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: service_requests  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/service_requests/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eine Entität vom Typ ServiceRequest ist eine akzeptable Open 311-Dienstanfrage. Eine solche Entität umfasst alle von Open 311 bei POST Service Request und GET Service Request definierten Eigenschaften.**  
Version: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `agency_responsible[string]`: Bitte beachten Sie, dass dies semantisch äquivalent zur Eigenschaft provider (Untereigenschaft name) von schema.org ist  . Model: [http://schema.org/provider](http://schema.org/provider)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `device_id[*]`: Die eindeutige Geräte-ID des Geräts, das die Anfrage stellt. Dies wird in der Regel nur für mobile Geräte verwendet  . Model: [https://schema.org/URL](https://schema.org/URL)- `email[string]`: E-Mail Adresse des Eigentümers.  - `expected_datetime[string]`: Das Datum und die Uhrzeit, zu der die Dienstanforderung voraussichtlich erfüllt werden kann. Dies kann auf der Grundlage einer dienstleistungsspezifischen Service-Level-Vereinbarung erfolgen  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `first_name[string]`: Vornamen. In den USA der erste Name einer Person.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `jurisdiction_id[string]`: Die eindeutige ID des Rechtsträgers des Dienstes (d. h. der Stadt).  - `last_name[string]`: Familienname. In den USA der Nachname einer Person.  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `media_url[string]`: Eine URL zu Medien, die mit der Anfrage verbunden sind, z. B. ein Bild  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: Der Name dieses Artikels.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `phone[string]`: Die Rufnummer.  . Model: [https://schema.org/Text](https://schema.org/Text)- `requested_datetime[string]`: Das Datum und die Uhrzeit, zu der die Serviceanfrage gestellt wurde  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `service_code[string]`: Der eindeutige Bezeichner für den Typ der Dienstanfrage.  - `service_name[string]`: Der von Menschen lesbare Name des Dienstanfragetyps.  - `service_notice[string]`: Informationen über die Maßnahmen, die zur Erledigung des Ersuchens oder zur Behebung der gemeldeten Informationen erwartet werden.  - `service_request_id[string]`: Die eindeutige ID der erstellten Dienstanfrage.  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `status[string]`: Ermöglicht die Suche nach Anfragen, die einen bestimmten Status haben. Standardmäßig sind dies alle Status; kann mehrfach angegeben werden, durch Komma getrennt. Enum:'offen, geschlossen'  - `status_notes[string]`: Erklärung, warum der Status in den aktuellen Zustand geändert wurde, oder mehr Details zum aktuellen Status als mit dem Status allein vermittelt werden.  - `type[string]`: NGSI-Entitätstyp. Es muss service_requests sein. Enum:'service_requests'  - `updated_datetime[string]`: Das Datum und die Uhrzeit, zu der die Dienstanfrage zuletzt geändert wurde. Bei Anfragen mit status=closed ist dies das Datum, an dem die Anfrage geschlossen wurde  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Eine Entität vom Typ `ServiceRequest` ist eine akzeptable Open 311-Dienstanfrage. Eine solche Entität umfasst alle von Open 311 unter [POST Service Request] (http://wiki.open311.org/GeoReport_v2/#post-service-request) und [GET Service Request] (http://wiki.open311.org/GeoReport_v2/#get-service-request) definierten Eigenschaften. Unter Verwendung dieses Datenmodells und einer FIWARE NGSI Version 2 Implementierung ist es einfach, einen Dienst zu implementieren, der mit den Open 311 Spezifikationen konform ist.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
service_requests:    
  description: 'An entity of type ServiceRequest is an acceptable Open 311 service request. Such entity encompasses all the properties defined by Open 311 at POST Service Request and GET Service Request.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    agency_responsible:    
      description: 'Please note that this is semantically equivalent to the provider property (name subproperty) of schema.org'    
      type: string    
      x-ngsi:    
        model: http://schema.org/provider    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    email:    
      description: 'Email address of owner.'    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    expected_datetime:    
      description: 'The date and time when the service request can be expected to be fulfilled. This may be based on a service-specific service level agreement'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    first_name:    
      description: 'Given name. In the U.S., the first name of a Person.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &service_requests_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    jurisdiction_id:    
      description: 'The unique ID of the legal entity of the service (i.e. city).'    
      type: string    
      x-ngsi:    
        type: Property    
    last_name:    
      description: 'Family name. In the U.S., the last name of a Person.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
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
      x-ngsi:    
        type: Geoproperty    
    media_url:    
      description: 'A URL to media associated with the request, eg an image'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *service_requests_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    phone:    
      description: 'The telephone number.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    requested_datetime:    
      description: 'The date and time when the service request was made'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    service_code:    
      description: 'The unique identifier for the service request type.'    
      type: string    
      x-ngsi:    
        type: Property    
    service_name:    
      description: 'The human readable name of the service request type.'    
      type: string    
      x-ngsi:    
        type: Property    
    service_notice:    
      description: 'Information about the action expected to fulfill the request or otherwise address the information reported.'    
      type: string    
      x-ngsi:    
        type: Property    
    service_request_id:    
      description: 'The unique ID of the service request created.'    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Allows one to search for requests which have a specific status. This defaults to all statuses; can be declared multiple times, comma delimited. Enum:''open, closed'''    
      enum:    
        - closed    
        - open    
      type: string    
      x-ngsi:    
        type: Property    
    status_notes:    
      description: 'Explanation of why status was changed to current state or more details on current status than conveyed with status alone.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be service_requests. Enum:''service_requests'''    
      enum:    
        - service_requests    
      type: string    
      x-ngsi:    
        type: Property    
    updated_datetime:    
      description: 'The date and time when the service request was last modified. For requests with status=closed, this will be the date the request was closed'    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/service_requests/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.IssueTracking/service_requests/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### service_requests NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine service_requests im JSON-LD Format als key-values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "service-request:638344",  
  "type": "Open311ServiceRequest",  
  "service_request_id": "638344",  
  "status": "closed",  
  "status_notes": "Duplicate request.",  
  "service_name": "Aceras",  
  "service_code": "234",  
  "description": "Acera en mal estado con bordillo partido en dos",  
  "agency_responsible": "Ayuntamiento de Ciudad",  
  "requested_datetime": "2010-04-14T06:37:38-08:00",  
  "updated_datetime": "2010-04-14T06:37:38-08:00",  
  "expected_datetime": "2010-04-15T06:37:38-08:00",  
  "address_string": "Calle San Juan Bautista, 2",  
  "attributes": [  
    {  
      "code": "ISSUE_TYPE",  
      "values": [  
        {  
          "key": 1,  
          "name": "Bordillo"  
        }  
      ]  
    }  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ]  
  },  
  "media_url": "http://exaple.org/media/638344.jpg"  
}  
```  
</details>  
#### service_requests NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine service_requests im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "service-request:638344",  
  "type": "Open311ServiceRequest",  
  "status": {  
    "type": "Text",  
    "value": "closed"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Acera en mal estado con bordillo partido en dos"  
  },  
  "service_code": {  
    "type": "Text",  
    "value": "234"  
  },  
  "status_notes": {  
    "type": "Text",  
    "value": "Duplicate request."  
  },  
  "service_name": {  
    "type": "Text",  
    "value": "Aceras"  
  },  
  "service_request_id": {  
    "type": "Text",  
    "value": "638344"  
  },  
  "updated_datetime": {  
    "type": "DateTime",  
    "value": "2010-04-14T06:37:38-08:00"  
  },  
  "address_string": {  
    "type": "Text",  
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
      "coordinates": [  
        -3.164485591715449,  
        40.62785133667262  
      ]  
    }  
  },  
  "attributes": {  
    "type": "Text",  
    "value": [  
      {  
        "code": "ISSUE_TYPE",  
        "values": [  
          {  
            "key": 1,  
            "name": "Bordillo"  
          }  
        ]  
      }  
    ]  
  },  
  "expected_datetime": {  
    "type": "DateTime",  
    "value": "2010-04-15T06:37:38-08:00"  
  },  
  "agency_responsible": {  
    "type": "Text",  
    "value": "Ayuntamiento de Ciudad"  
  },  
  "media_url": {  
    "type": "Text",  
    "value": "http://exaple.org/media/638344.jpg"  
  }  
}  
```  
</details>  
#### service_requests NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine service_requests im JSON-LD Format als key-values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "service-request:638344",  
    "type": "Open311ServiceRequest",  
    "address_string": "Calle San Juan Bautista, 2",  
    "agency_responsible": "Ayuntamiento de Ciudad",  
    "attributes": [  
        {  
            "code": "ISSUE_TYPE",  
            "values": [  
                {  
                    "key": 1,  
                    "name": "Bordillo"  
                }  
            ]  
        }  
    ],  
    "description": "Acera en mal estado con bordillo partido en dos",  
    "expected_datetime": "2010-04-15T06:37:38-08:00",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -3.164485591715449,  
            40.62785133667262  
        ]  
    },  
    "media_url": "http://exaple.org/media/638344.jpg",  
    "requested_datetime": "2010-04-14T06:37:38-08:00",  
    "service_code": "234",  
    "service_name": "Aceras",  
    "service_request_id": "638344",  
    "status": "closed",  
    "status_notes": "Duplicate request.",  
    "updated_datetime": "2010-04-14T06:37:38-08:00",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.IssueTracking/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### service_requests NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine service_requests im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Open311ServiceRequest:service-request:638344",  
    "type": "Open311ServiceRequest",  
    "address_string": {  
        "type": "Property",  
        "value": "Calle San Juan Bautista, 2"  
    },  
    "agency_responsible": {  
        "type": "Property",  
        "value": "Ayuntamiento de Ciudad"  
    },  
    "attributes": {  
        "type": "Property",  
        "value": [  
            {  
                "code": "ISSUE_TYPE",  
                "values": [  
                    {  
                        "key": 1,  
                        "name": "Bordillo"  
                    }  
                ]  
            }  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "Acera en mal estado con bordillo partido en dos"  
    },  
    "expected_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-15T06:37:38-08:00Z"  
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
    "media_url": {  
        "type": "Property",  
        "value": "http://exaple.org/media/638344.jpg"  
    },  
    "requested_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-14T06:37:38-08:00"  
        }  
    },  
    "service_code": {  
        "type": "Property",  
        "value": "234"  
    },  
    "service_name": {  
        "type": "Property",  
        "value": "Aceras"  
    },  
    "service_request_id": {  
        "type": "Property",  
        "value": "638344"  
    },  
    "status": {  
        "type": "Property",  
        "value": "closed"  
    },  
    "status_notes": {  
        "type": "Property",  
        "value": "Duplicate request."  
    },  
    "updated_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-14T06:37:38-08:00"  
        }  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.IssueTracking/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
