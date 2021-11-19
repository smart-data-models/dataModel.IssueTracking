Entità: Open311_ServiceRequest  
==============================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceRequest/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un'entità di tipo ServiceRequest è una richiesta di servizio Open 311 accettabile. Tale entità comprende tutte le proprietà definite da Open 311 a POST Service Request e GET Service Request.**  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `agency_responsible`: Si noti che questo è semanticamente equivalente alla proprietà provider (name subproperty) di schema.org  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `device_id`: L'ID unico del dispositivo che invia la richiesta. Questo è di solito usato solo per i dispositivi mobili  - `email`: Indirizzo e-mail del proprietario.  - `expected_datetime`: La data e l'ora in cui ci si può aspettare che la richiesta di servizio sia soddisfatta. Questo può essere basato su un accordo sul livello di servizio specifico  - `first_name`: Nome di battesimo. Negli Stati Uniti, il nome di una persona.  - `id`: Identificatore unico dell'entità  - `jurisdiction_id`: L'ID unico dell'entità legale del servizio (cioè la città).  - `last_name`: Nome di famiglia. Negli Stati Uniti, il cognome di una persona.  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `media_url`: Un URL ai media associati alla richiesta, ad esempio un'immagine  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `phone`: Il numero di telefono.  - `requested_datetime`: La data e l'ora in cui è stata fatta la richiesta di servizio  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `service_code`: L'identificatore unico per il tipo di richiesta di servizio.  - `service_name`: Il nome leggibile all'uomo del tipo di richiesta di servizio.  - `service_notice`: Informazioni sull'azione prevista per soddisfare la richiesta o altrimenti affrontare le informazioni riportate.  - `service_request_id`: L'ID unico della richiesta di servizio creata.  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio pienamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `status`: Permette di cercare le richieste che hanno uno stato specifico. Questo è il valore predefinito per tutti gli stati; può essere dichiarato più volte, delimitato da virgole. Enum:'aperto, chiuso'.  - `status_notes`: Spiegazione del perché lo stato è stato cambiato allo stato attuale o maggiori dettagli sullo stato attuale rispetto a quelli trasmessi con il solo stato.  - `type`: Tipo di entità NGSI. Deve essere Open311ServiceRequest  - `updated_datetime`: La data e l'ora in cui la richiesta di servizio è stata modificata per l'ultima volta. Per le richieste con status=closed, questa sarà la data in cui la richiesta è stata chiusa    
Proprietà richieste  
- `id`  - `type`    
Un'entità di tipo `ServiceRequest` è una richiesta di servizio Open 311 accettabile. Tale entità comprende tutte le proprietà definite da Open 311 in [POST Service Request](http://wiki.open311.org/GeoReport_v2/#post-service-request) e [GET Service Request](http://wiki.open311.org/GeoReport_v2/#get-service-request). Usando questo modello di dati e un'implementazione FIWARE NGSI versione 2 è semplice implementare un servizio conforme alle specifiche di Open 311.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Open311_ServiceRequest:    
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
        anyOf: *open311_servicerequest_-_properties_-_owner_-_items_-_anyof    
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
      description: 'NGSI Entity type. It has to be Open311ServiceRequest'    
      enum:    
        - Open311ServiceRequest    
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
  x-license-url: https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/Open311_ServiceRequest/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.IssueTracking/Open311_ServiceRequest/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
## Esempio di payloads  
#### Open311_ServiceRequest NGSI-v2 valori chiave Esempio  
Ecco un esempio di una Open311_ServiceRequest in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### Open311_ServiceRequest NGSI-v2 normalizzato Esempio  
Ecco un esempio di una Open311_ServiceRequest in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Open311_ServiceRequest NGSI-LD valori-chiave Esempio  
Ecco un esempio di una Open311_ServiceRequest in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
  "media_url": "http://exaple.org/media/638344.jpg",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### Open311_ServiceRequest NGSI-LD normalizzato Esempio  
Ecco un esempio di una Open311_ServiceRequest in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
