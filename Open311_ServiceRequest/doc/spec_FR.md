Entité : Open311_ServiceRequest  
===============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceRequest/LICENSE.md)  
Description globale : **Une entité de type ServiceRequest est une demande de service Open 311 acceptable. Une telle entité englobe toutes les propriétés définies par l'Open 311 à POST Service Request et GET Service Request.**  

## Liste des biens  

- `address`: L'adresse postale.  - `agency_responsible`: Veuillez noter que ceci est sémantiquement équivalent à la propriété du fournisseur (nom de la sous-propriété) de schema.org  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `device_id`: L'identifiant unique de l'appareil qui soumet la demande. Il n'est généralement utilisé que pour les appareils mobiles  - `email`: Adresse électronique du propriétaire.  - `expected_datetime`: Date et heure auxquelles la demande de service devrait être satisfaite. Cela peut être basé sur un accord de niveau de service spécifique au service  - `first_name`: Prénom. Aux États-Unis, le prénom d'une personne.  - `id`: Identifiant unique de l'entité  - `jurisdiction_id`: L'identifiant unique de l'entité juridique du service (c'est-à-dire la ville).  - `last_name`: Nom de famille. Aux États-Unis, le nom de famille d'une personne.  - `location`:   - `media_url`: Une URL vers le média associé à la demande, par exemple une image  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `phone`: Prénom. Le numéro de téléphone.  - `requested_datetime`: La date et l'heure auxquelles la demande de service a été faite  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `service_code`: L'identifiant unique pour le type de demande de service.  - `service_name`: Le nom lisible par l'homme du type de demande de service.  - `service_notice`: Des informations sur l'action prévue pour répondre à la demande ou pour traiter les informations communiquées.  - `service_request_id`: L'identifiant unique de la demande de service créée.  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `status`: Permet de rechercher les demandes qui ont un statut spécifique. Par défaut, tous les statuts sont pris en compte ; il est possible de les déclarer plusieurs fois, en les délimitant par des virgules. Enum : "ouvert, fermé".  - `status_notes`: Explication de la raison pour laquelle le statut a été modifié en état actuel ou plus de détails sur l'état actuel que ceux transmis avec le statut seul.  - `type`: Type d'entité NGSI. Il doit s'agir d'Open311ServiceRequest  - `updated_datetime`: La date et l'heure de la dernière modification de la demande de service. Pour les demandes avec status=closed, ce sera la date à laquelle la demande a été clôturée    
Propriétés requises  
- `id`  - `type`    
Une entité de type "ServiceRequest" est une demande de service Open 311 acceptable. Cette entité englobe toutes les propriétés définies par l'Open 311 sur [POST Service Request] (http://wiki.open311.org/GeoReport_v2/#post-service-request) et [GET Service Request] (http://wiki.open311.org/GeoReport_v2/#get-service-request). En utilisant ce modèle de données et une implémentation FIWARE NGSI version 2, il est facile de mettre en œuvre un service conforme aux spécifications de l'Open 311.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Open311_ServiceRequest NGSI V2 key-values Exemple  
Voici un exemple de demande de service Open311 au format JSON en tant que valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### Open311_ServiceRequest NGSI V2 normalisé Exemple  
Voici un exemple de demande de service Open311_ServiceRequest au format JSON tel que normalisé. Ce format est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Open311_ServiceRequest NGSI-LD exemple de valeurs clés  
Voici un exemple de demande de service Open311 au format JSON-LD en tant que valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### Open311_ServiceRequest NGSI-LD normalisé Exemple  
Voici un exemple de demande de service Open311_ServiceRequest au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
