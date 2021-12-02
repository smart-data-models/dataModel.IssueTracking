Entità: IssueReporting  
======================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/IssueReporting/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Un modello di dati per i problemi dei cittadini, le segnalazioni e i feedback.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `category`: Il nome della categoria corrispondente al problema che è stato segnalato.  - `categoryCode`: Identificatore unico per la categoria corrispondente al problema segnalato.  - `comments`: Commenti degli utenti corrispondenti a questa osservazione.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `departmentId`: ID o codice unico associato al dipartimento che è associato al servizio o alla questione corrispondente a questa osservazione.  - `description`: Una descrizione di questo articolo  - `id`: Identificatore unico dell'entità  - `landmark`: Un elemento fisico distintivo sulla terra che segna una località o un luogo.  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `mediaURL`: URL che fornisce ulteriori informazioni di qualsiasi immagine(i) o media della denuncia o del luogo.  - `name`: Il nome di questo articolo.  - `observationDateTime`: Ultima ora di osservazione riportata.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `reportId`: ID unico assegnato per il problema o la relazione o il feedback o la transazione corrispondente a questa osservazione.  - `resolutionStatus`: Stato del problema che è stato segnalato in termini di risoluzione o delle azioni intraprese su di esso. Potrebbe essere Open, Assigned, InProgress, Unassigned, Closed  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `subCategory`: Il nome della sottocategoria corrispondente al problema che è stato segnalato.  - `subCategoryCode`: Identificatore unico per la sottocategoria corrispondente al problema segnalato.  - `title`: Il titolo assegnato alla questione, al rapporto o al feedback corrispondente a questa osservazione.  - `titleCode`: Il codice assegnato al titolo corrispondente a questa osservazione.  - `type`: Tipo di entità NGSI. Deve essere IssueReporting  - `wardId`: ID del reparto dell'entità corrispondente a questa osservazione.    
Proprietà richieste  
- `id`  - `type`    
La segnalazione delle questioni è adattata dal sistema di segnalazione IUDX per l'oggetto dataModel.IssueTracking.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
IssueReporting:    
  description: 'A Data Model for citizen issues, reports and feedbacks.'    
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
    category:    
      description: 'The category name corresponding to the issue that has been reported.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    categoryCode:    
      description: 'Unique identifier for the category corresponding to the issue reported.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    comments:    
      description: 'User comments corresponding to this observation.'    
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
    departmentId:    
      description: 'Unique ID or code associated with the department which is associated with the service or the issue corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &issuereporting_-_properties_-_owner_-_items_-_anyof    
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
    landmark:    
      description: 'A physical distinguishing feature on land that marks a locality or a place.'    
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
    mediaURL:    
      description: 'URL providing further information of any image(s) or media of the complaint or place.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observationDateTime:    
      description: 'Last reported time of observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *issuereporting_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    reportId:    
      description: 'Unique ID assigned for the issue or report or feedback or transaction corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    resolutionStatus:    
      description: 'Status of the issue that was reported in terms of resolution or the actions taken on it. Could be Open, Assigned, InProgress, Unassigned, Closed'    
      enum:    
        - Assigned    
        - Closed.    
        - InProgress    
        - Open    
        - Unassigned    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    subCategory:    
      description: 'The sub-category name corresponding to the issue that has been reported.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    subCategoryCode:    
      description: 'Unique identifier for the sub-category corresponding to the issue reported.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    title:    
      description: 'The title assigned to the issue, report or feedback corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    titleCode:    
      description: 'The code assigned to the title corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be IssueReporting'    
      enum:    
        - IssueReporting    
      type: string    
      x-ngsi:    
        type: Property    
    wardId:    
      description: 'Ward ID of the entity corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/IssueReporting/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.IssueTracking/IssueReporting/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### IssueReporting NGSI-v2 key-values Esempio  
Ecco un esempio di un IssueReporting in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi-ld:xYBR:0102",  
    "type": "IssueReporting",  
    "comments": "Road not in proper condition",  
    "wardId": "4",  
    "departmentId": "12",  
    "title": "Road maintenance",  
    "subCategoryCode": "RM",  
    "titleCode": "RDM",  
    "subCategory": "Road Repair",  
    "reportId": "21645",  
    "categoryCode": "112",  
    "category": "Maintenance",  
    "landmark": "Near St.Andrews Church",  
    "observationDateTime": "2021-03-11T15:51:02+05:30",  
    "mediaURL": "https://imgur.com",  
    "resolutionStatus": "Assigned"  
}  
```  
#### IssueReporting NGSI-v2 normalizzato Esempio  
Ecco un esempio di un IssueReporting in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:xYBR:0102",  
  "type": "IssueReporting",  
  "comments": {  
    "type": "Text",  
    "value": "Road not in proper condition"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": "4"  
  },  
  "departmentId": {  
    "type": "Text",  
    "value": "12"  
  },  
  "title": {  
    "type": "Text",  
    "value": "Road maintenance"  
  },  
  "subCategoryCode": {  
    "type": "Text",  
    "value": "RM"  
  },  
  "titleCode": {  
    "type": "Text",  
    "value": "RDM"  
  },  
  "subCategory": {  
    "type": "Text",  
    "value": "Road Repair"  
  },  
  "reportId": {  
    "type": "Text",  
    "value": "21645"  
  },  
  "categoryCode": {  
    "type": "Text",  
    "value": "112"  
  },  
  "category": {  
    "type": "Text",  
    "value": "Maintenance"  
  },  
  "landmark": {  
    "type": "Text",  
    "value": "Near St.Andrews Church"  
  },  
  "observationDateTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "mediaURL": {  
    "type": "URL",  
    "value": "https://imgur.com"  
  },  
  "resolutionStatus": {  
    "type": "Text",  
    "value": "Assigned"  
  }  
}  
```  
#### IssueReporting NGSI-LD key-values Esempio  
Ecco un esempio di un IssueReporting in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:xYBR:0102",  
  "type": "IssueReporting",  
  "comments": "Road not in proper condition",  
  "wardId": "4",  
  "departmentId": "12",  
  "title": "Road maintenance",  
  "subCategoryCode": "RM",  
  "titleCode": "RDM",  
  "subCategory": "Road Repair",  
  "reportId": "21645",  
  "categoryCode": "112",  
  "category": "Maintenance",  
  "landmark": "Near St.Andrews Church",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "mediaURL": "https://imgur.com",  
  "resolutionStatus": "Assigned",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "iudx:IssueReporting"  
  ]  
}  
```  
#### IssueReporting NGSI-LD normalizzato Esempio  
Ecco un esempio di un IssueReporting in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi-ld:xYBR:0102",  
    "type": "IssueReporting",  
    "comments": {  
        "type": "Property",  
        "value": "Road not in proper condition"  
    },  
    "wardId": {  
        "type": "Property",  
        "value": "4"  
    },  
    "departmentId": {  
        "type": "Property",  
        "value": "12"  
    },  
    "title": {  
        "type": "Property",  
        "value": "Road maintenance"  
    },  
    "subCategoryCode": {  
        "type": "Property",  
        "value": "RM"  
    },  
    "titleCode": {  
        "type": "Property",  
        "value": "RDM"  
    },  
    "subCategory": {  
        "type": "Property",  
        "value": "Road Repair"  
    },  
    "reportId": {  
        "type": "Property",  
        "value": "21645"  
    },  
    "categoryCode": {  
        "type": "Property",  
        "value": "112"  
    },  
    "category": {  
        "type": "Property",  
        "value": "Maintenance"  
    },  
    "landmark": {  
        "type": "Property",  
        "value": "Near St.Andrews Church"  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "mediaURL": {  
        "type": "Property",  
        "value": "https://imgur.com"  
    },  
    "resolutionStatus": {  
        "type": "Property",  
        "value": "Assigned"  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",   
        "iudx:IssueReporting"  
    ]  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza