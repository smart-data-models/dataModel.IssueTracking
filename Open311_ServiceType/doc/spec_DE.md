Entität: Open311_ServiceType  
============================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceType/LICENSE.md)  
Globale Beschreibung: **Gemäß Open311 ist eine Entität vom Typ ServiceType ein akzeptabler 311-Service-Anfrage-Typ. Ein Anfragetyp kann für die Stadt/Gerichtsbarkeit eindeutig sein.**  

## Liste der Eigenschaften  

- `address`: Die Postanschrift.  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `attributes`: Gemäß der von Open 311 definierten [Service Definition](http://wiki.open311.org/GeoReport_v2/#get-service-definition) Struktur.  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `effectiveSince`: Das Datum, an dem der Diensttyp erstellt wurde. Dieses Datum kann sich vom Erstellungsdatum der Entität unterscheiden  - `group`: Eine Kategorie, in der dieser Diensttyp gruppiert wird. Dies bietet eine Möglichkeit, mehrere Serviceanforderungstypen unter einer Kategorie zu gruppieren, wie z. B. Sanitär  - `id`: Eindeutiger Bezeichner der Entität  - `jurisdiction_id`: Die eindeutige ID der juristischen Person des Dienstes (d. h. der Stadt).  - `keywords`: Eine durch Kommata getrennte Liste von Tags oder Schlüsselwörtern, die Benutzern helfen, den Anfragetyp zu identifizieren. Dies kann Synonyme des service_name und der Gruppe liefern.  - `location`:   - `name`: Der Name dieses Elements.  - `open311:metadata`: Dieses Feld ist nicht unbedingt erforderlich, da die vorgeschlagene Entität auch die Attributdefinition umfasst. Wenn es definiert ist, muss sein Wert `true` sein, wenn die Eigenschaft `attributes` definiert ist und sein Array-Wert nicht leer ist. Andernfalls muss es gleich `false` sein.  - `open311:type`: realtime: Die ID der Dienstanforderung wird sofort nach dem Senden der Dienstanforderung zurückgegeben. batch: Ein Token wird sofort nach dem Absenden der Dienstanforderung zurückgegeben. Dieses Token kann dann später verwendet werden, um die Dienstanforderungs-ID zurückzugeben. blackbox: Es wird keine Service Request ID zurückgegeben, nachdem die Service Request übermittelt wurde. Enum:'realtime, batch, blackbox'.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `provider`: Anbieter des Dienstes  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `service_code`: Der eindeutige Bezeichner für den Dienstanforderungstyp.  - `service_name`: Der menschenlesbare Name des Dienstanforderungstyps.  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI Entity-Typ. Es muss Open311ServiceType sein    
Erforderliche Eigenschaften  
- `id`  - `type`    
Gemäß [Open311] (http://wiki.open311.org/GeoReport_v2/#get-service-list) ist eine Entität des Typs `ServiceType` ein akzeptabler 311-Dienstanforderungstyp. Ein Anfragetyp kann für die Stadt/Gerichtsbarkeit eindeutig sein. Bitte beachten Sie, dass dieses Datenmodell nicht stilistisch harmonisiert wurde. Wir haben uns entschieden, die gleichen Eigenschaftsnamen und die gleiche Struktur beizubehalten, obwohl wir fest davon überzeugt sind, dass das Open311-Modell genutzt werden kann.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Open311_ServiceType:    
  description: 'As per Open311 an entity of type ServiceType is an acceptable 311 service request type. A request type can be unique to the city/jurisdiction.'    
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
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    attributes:    
      description: "As per the [Service Definition](http://wiki.open311.org/GeoReport_v2/#get-service-definition) structure defined by Open 311."    
      items:    
        anyOf:    
          - type: string    
          - type: object    
          - type: array    
          - type: boolean    
          - type: number    
      type: Property    
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
    effectiveSince:    
      description: 'The date on which the service type was created. This date might be different than the entity creation date'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: http://schema.org/DateTime    
    group:    
      description: 'A category to group this service type within. This provides a way to group several service request types under one category such as sanitation'    
      type: Property    
    id:    
      anyOf: &open311_servicetype_-_properties_-_owner_-_items_-_anyof    
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
    keywords:    
      description: 'A comma separated list of tags or keywords to help users identify the request type. This can provide synonyms of the service_name and group.'    
      type: Property    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    open311:metadata:    
      description: 'This field is not strictly needed as the proposed entity encompasses the attribute definition as well. If defined, its value must be `true` if the `attributes` property is defined and its array value is not empty. Otherwise it must be equal to `false`'    
      type: Property    
    open311:type:    
      description: 'realtime: The service request ID will be returned immediately after the service request is submitted. batch: A token will be returned immediately after the service request is submitted. This token can then be later used to return the service request ID. blackbox: No service request ID will be returned after the service request is submitted. Enum:''realtime, batch, blackbox''. '    
      enum:    
        - batch    
        - blackbox    
        - realtime    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *open311_servicetype_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    provider:    
      description: 'Provider of the service'    
      type: Property    
      x-ngsi:    
        model: http://schema.org/provider    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Open311ServiceType'    
      enum:    
        - Open311ServiceType    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### Open311_ServiceType NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceType im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "o311:servicetype-guadalajara-sidewalks",  
  "type": "Open311ServiceType",  
  "dateCreated": "2007-01-01T12:00:00Z",  
  "jurisdiction_id": "www.smartguadalajara.com",  
  "open311:type": "realtime",  
  "service_code": "234",  
  "service_name": "Aceras",  
  "description": "When a sidewalk is broken or dirty allows citizens to request a fix",  
  "keywords": "street,sidewalk, cleaning, repair",  
  "group": "street",  
  "attributes": [  
    {  
      "variable": true,  
      "code": "ISSUE_TYPE",  
      "datatype": "singlevaluelist",  
      "required": true,  
      "datatype_description": "",  
      "order": 1,  
      "description": "What is the identified problem at the sidewalk?",  
      "values": [  
        {  
          "key": 123,  
          "name": "Bump"  
        },  
        {  
          "key": 124,  
          "name": "Dirty"  
        }  
      ]  
    }  
  ]  
}  
```  
#### Open311_ServiceType NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceType im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "o311:servicetype-guadalajara-sidewalks",  
  "type": "Open311ServiceType",  
  "group": {  
    "value": "street"  
  },  
  "description": {  
    "value": "When a sidewalk is broken or dirty allows citizens to request a fix"  
  },  
  "service_code": {  
    "value": "234"  
  },  
  "service_name": {  
    "value": "Aceras"  
  },  
  "open311:type": {  
    "value": "realtime"  
  },  
  "jurisdiction_id": {  
    "value": "www.smartguadalajara.com"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2007-01-01T12:00:00Z"  
  },  
  "keywords": {  
    "value": "street,sidewalk, cleaning, repair"  
  },  
  "attributes": {  
    "value": [  
      {  
        "code": "ISSUE_TYPE",  
        "description": "What is the identified problem at the sidewalk?",  
        "datatype": "singlevaluelist",  
        "required": true,  
        "values": [  
          {  
            "name": "Bump",  
            "key": 123  
          },  
          {  
            "name": "Dirty",  
            "key": 124  
          }  
        ],  
        "variable": true,  
        "order": 1,  
        "datatype_description": ""  
      }  
    ]  
  }  
}  
```  
#### Open311_ServiceType NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceType im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:Open311ServiceType:o311:servicetype-guadalajara-sidewalks",  
  "type": "Open311ServiceType",  
  "createdAt": "2007-01-01T12:00:00Z",  
  "group": {  
    "type": "Property",  
    "value": "street"  
  },  
  "description": {  
    "type": "Property",  
    "value": "When a sidewalk is broken or dirty allows citizens to request a fix"  
  },  
  "service_code": {  
    "type": "Property",  
    "value": "234"  
  },  
  "service_name": {  
    "type": "Property",  
    "value": "Aceras"  
  },  
  "open311:type": {  
    "type": "Property",  
    "value": "realtime"  
  },  
  "jurisdiction_id": {  
    "type": "Property",  
    "value": "www.smartguadalajara.com"  
  },  
  "keywords": {  
    "type": "Property",  
    "value": "street,sidewalk, cleaning, repair"  
  },  
  "attributes": {  
    "type": "Property",  
    "value": [  
      {  
        "code": "ISSUE_TYPE",  
        "description": "What is the identified problem at the sidewalk?",  
        "datatype": "singlevaluelist",  
        "required": true,  
        "values": [  
          {  
            "name": "Bump",  
            "key": 123  
          },  
          {  
            "name": "Dirty",  
            "key": 124  
          }  
        ],  
        "variable": true,  
        "order": 1,  
        "datatype_description": ""  
      }  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Open311_ServiceType NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen Open311_ServiceType im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
  "attributes": [  
    {  
      "code": "ISSUE_TYPE",  
      "datatype": "singlevaluelist",  
      "datatype_description": "",  
      "description": "What is the identified problem at the sidewalk?",  
      "order": 1,  
      "required": true,  
      "values": [  
        {  
          "key": 123,  
          "name": "Bump"  
        },  
        {  
          "key": 124,  
          "name": "Dirty"  
        }  
      ],  
      "variable": true  
    }  
  ],  
  "createdAt": "2007-01-01T12:00:00Z",  
  "description": "When a sidewalk is broken or dirty allows citizens to request a fix",  
  "group": "street",  
  "id": "urn:ngsi-ld:Open311ServiceType:o311:servicetype-guadalajara-sidewalks",  
  "jurisdiction_id": "www.smartguadalajara.com",  
  "keywords": "street,sidewalk, cleaning, repair",  
  "open311:type": "realtime",  
  "service_code": "234",  
  "service_name": "Aceras",  
  "type": "Open311ServiceType"  
}  
```  
