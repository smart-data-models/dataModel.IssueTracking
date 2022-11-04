Entität: IssueReporting  
=======================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/IssueReporting/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Ein Datenmodell für Bürgerfragen, Berichte und Rückmeldungen**.  
Version: 0.0.1  

## Liste der Eigenschaften  

- `address`: Die Postanschrift  - `alternateName`: Ein alternativer Name für diesen Artikel  - `areaServed`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  - `category`: Der Name der Kategorie, die dem gemeldeten Problem entspricht.  - `categoryCode`: Eindeutige Kennung für die Kategorie, die dem gemeldeten Problem entspricht.  - `comments`: Entsprechende Nutzerkommentare zu dieser Beobachtung.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `departmentId`: Eindeutige ID oder Code der Abteilung, die mit der dieser Beobachtung entsprechenden Dienstleistung oder dem Problem in Verbindung steht.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `landmark`: Ein physisches Unterscheidungsmerkmal an Land, das einen Ort oder eine Stelle kennzeichnet.  - `location`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `mediaURL`: URL mit weiteren Informationen zu Bild(ern) oder Medien der Beschwerde oder des Ortes.  - `name`: Der Name dieses Artikels.  - `observationDateTime`: Letzter gemeldeter Zeitpunkt der Beobachtung.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `reportId`: Eindeutige ID, die dem Problem, dem Bericht, dem Feedback oder der Transaktion zugewiesen wurde, die dieser Beobachtung entspricht.  - `resolutionStatus`: Status des gemeldeten Problems in Bezug auf die Lösung oder die ergriffenen Maßnahmen. Kann offen, zugewiesen, in Bearbeitung, nicht zugewiesen oder geschlossen sein.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `subCategory`: Der Name der Unterkategorie, die dem gemeldeten Problem entspricht.  - `subCategoryCode`: Eindeutige Kennung für die Unterkategorie, die dem gemeldeten Problem entspricht.  - `title`: Der Titel, der dem Problem, dem Bericht oder dem Feedback zu dieser Beobachtung zugewiesen wurde.  - `titleCode`: Der dem Titel zugewiesene Code, der dieser Beobachtung entspricht.  - `type`: NGSI-Entitätstyp. Es muss IssueReporting sein  - `wardId`: Stations-ID der Einrichtung, die dieser Beobachtung entspricht.    
Erforderliche Eigenschaften  
- `id`  - `type`    
Das Issue-Reporting ist an das IUDX-Berichtssystem für das Thema dataModel.IssueTracking angepasst.  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
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
  version: 0.0.1    
```  
</details>    
## Beispiel-Nutzlasten  
#### IssueReporting NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein IssueReporting im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### IssueReporting NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein IssueReporting im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### IssueReporting NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein IssueReporting im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### IssueReporting NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein IssueReporting im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10](https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht