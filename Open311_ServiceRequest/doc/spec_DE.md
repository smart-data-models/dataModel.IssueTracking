Entität: Open311_ServiceRequest  
===============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceRequest/LICENSE.md)  
Globale Beschreibung: **Eine Entität vom Typ ServiceRequest ist eine akzeptable Open 311-Serviceanfrage. Eine solche Entität umfasst alle von Open 311 bei POST Service Request und GET Service Request definierten Eigenschaften.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift.  - `agency_responsible`: Bitte beachten Sie, dass dies semantisch äquivalent zur Provider-Eigenschaft (Untereigenschaft name) von schema.org ist  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `device_id`: Die eindeutige Geräte-ID des Geräts, das die Anfrage übermittelt. Dies wird normalerweise nur für mobile Geräte verwendet  - `email`: E-Mail Adresse des Eigentümers.  - `expected_datetime`: Das Datum und die Uhrzeit, zu der die Erfüllung der Service-Anforderung erwartet werden kann. Dies kann auf einer dienstspezifischen Service-Level-Vereinbarung beruhen  - `first_name`: Vornamen. In den USA der Vorname einer Person.  - `id`: Eindeutiger Bezeichner der Entität  - `jurisdiction_id`: Die eindeutige ID der juristischen Person des Dienstes (d. h. der Stadt).  - `last_name`: Familienname. In den USA der Nachname einer Person.  - `location`:   - `media_url`: Eine URL zu Medien, die mit der Anfrage verbunden sind, z. B. ein Bild  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `phone`: Vornamen. Die Rufnummer.  - `requested_datetime`: Das Datum und die Uhrzeit, zu der die Serviceanfrage gestellt wurde  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `service_code`: Der eindeutige Bezeichner für den Dienstanforderungstyp.  - `service_name`: Der menschenlesbare Name des Dienstanforderungstyps.  - `service_notice`: Informationen über die erwartete Aktion zur Erfüllung der Anfrage oder zur anderweitigen Behebung der gemeldeten Informationen.  - `service_request_id`: Die eindeutige ID der erstellten Dienstanforderung.  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `status`: Ermöglicht die Suche nach Anfragen, die einen bestimmten Status haben. Standardmäßig sind dies alle Status; kann mehrfach deklariert werden, kommagetrennt. Enum:'offen, geschlossen'  - `status_notes`: Erklärung, warum der Status in den aktuellen Zustand geändert wurde oder mehr Details zum aktuellen Status, als mit dem Status allein vermittelt werden.  - `type`: NGSI Entity-Typ. Es muss Open311ServiceRequest sein  - `updated_datetime`: Das Datum und die Uhrzeit, zu der die Serviceanfrage zuletzt geändert wurde. Bei Anfragen mit status=closed ist dies das Datum, an dem die Anfrage geschlossen wurde    
Erforderliche Eigenschaften  
- `id`  - `type`    
Eine Entität vom Typ `ServiceRequest` ist eine akzeptable Open 311-Service-Anfrage. Eine solche Entität umfasst alle von Open 311 unter [POST Service Request] (http://wiki.open311.org/GeoReport_v2/#post-service-request) und [GET Service Request] (http://wiki.open311.org/GeoReport_v2/#get-service-request) definierten Eigenschaften. Unter Verwendung dieses Datenmodells und einer FIWARE NGSI Version 2 Implementierung ist es einfach, einen Service zu implementieren, der den Open 311 Spezifikationen entspricht.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### Open311_ServiceRequest NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceRequest im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### Open311_ServiceRequest NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceRequest im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
    "value": "234"  
  },  
  "status_notes": {  
    "value": "Duplicate request."  
  },  
  "service_name": {  
    "value": "Aceras"  
  },  
  "service_request_id": {  
    "value": "638344"  
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
#### Open311_ServiceRequest NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceRequest im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
    "value": "234"  
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
    "value": "638344"  
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
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Open311_ServiceRequest NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceRequest im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "address_string": "Calle San Juan Bautista, 2",  
  "agency_responsible": "Ayuntamiento de Ciudad",  
  "attributes": {  
    "ISSUE_TYPE": [  
      "Bordillo"  
    ]  
  },  
  "description": "Acera en mal estado con bordillo partido en dos",  
  "expected_datetime": {  
    "@type": "DateTime",  
    "@value": "2010-04-15T06:37:38-08:00Z"  
  },  
  "id": "urn:ngsi-ld:Open311ServiceRequest:service-request:638344",  
  "location": {  
    "coordinates": [  
      -3.164485591715449,  
      40.62785133667262  
    ],  
    "type": "Point"  
  },  
  "media_url": "http://exaple.org/media/638344.jpg",  
  "requested_datetime": {  
    "@type": "DateTime",  
    "@value": "2010-04-14T06:37:38-08:00"  
  },  
  "service_code": "234",  
  "service_name": "Aceras",  
  "service_request_id": "638344",  
  "status": "closed",  
  "status_notes": "Duplicate request.",  
  "type": "Open311ServiceRequest",  
  "updated_datetime": {  
    "@type": "DateTime",  
    "@value": "2010-04-14T06:37:38-08:00"  
  }  
}  
```  
