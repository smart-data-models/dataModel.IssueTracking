<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: IssueReporting    
=======================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/IssueReporting/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Un modelo de datos para cuestiones, informes y comentarios de los ciudadanos.    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[string]`: El nombre de la categoría correspondiente al problema notificado  . Model: [https://schema.org/Text](https://schema.org/Text)- `categoryCode[string]`: Identificador único de la categoría correspondiente al problema notificado  . Model: [https://schema.org/Text](https://schema.org/Text)- `comments[string]`: Comentarios de los usuarios correspondientes a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `departmentId[string]`: ID único o código asociado con el departamento que está asociado con el servicio o el asunto correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `landmark[string]`: Rasgo físico distintivo de la tierra que marca una localidad o un lugar  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `mediaURL[uri]`: URL que proporcione más información de cualquier imagen o medios de comunicación de la denuncia o el lugar  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo  - `observationDateTime[date-time]`: Última hora de observación comunicada  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `reportId[string]`: ID único asignado a la incidencia o informe o comentario o transacción correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `resolutionStatus[string]`: Estado de la incidencia notificada en términos de resolución o de las acciones emprendidas al respecto. Puede ser Abierto, Asignado, En curso, Sin asignar, Cerrado.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `subCategory[string]`: El nombre de la subcategoría correspondiente al problema notificado  . Model: [https://schema.org/Text](https://schema.org/Text)- `subCategoryCode[string]`: Identificador único de la subcategoría correspondiente al problema notificado  . Model: [https://schema.org/Text](https://schema.org/Text)- `title[string]`: Título asignado al asunto, informe o comentario correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `titleCode[string]`: El código asignado al título correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI. Tiene que ser IssueReporting  - `wardId[string]`: Ward ID de la entidad correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Los informes de incidencias se adaptan del sistema de informes IUDX para el modelo de datos Subject.IssueTracking.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
IssueReporting:      
  description: 'A Data Model for citizen issues, reports and feedbacks.'      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    category:      
      description: The category name corresponding to the issue that has been reported      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    categoryCode:      
      description: Unique identifier for the category corresponding to the issue reported      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    comments:      
      description: User comments corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    departmentId:      
      description: Unique ID or code associated with the department which is associated with the service or the issue corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    landmark:      
      description: A physical distinguishing feature on land that marks a locality or a place      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    mediaURL:      
      description: URL providing further information of any image(s) or media of the complaint or place      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observationDateTime:      
      description: Last reported time of observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    reportId:      
      description: Unique ID assigned for the issue or report or feedback or transaction corresponding to this observation      
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
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    subCategory:      
      description: The sub-category name corresponding to the issue that has been reported      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    subCategoryCode:      
      description: Unique identifier for the sub-category corresponding to the issue reported      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    title:      
      description: 'The title assigned to the issue, report or feedback corresponding to this observation'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    titleCode:      
      description: The code assigned to the title corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI entity type. It has to be IssueReporting      
      enum:      
        - IssueReporting      
      type: string      
      x-ngsi:      
        type: Property      
    wardId:      
      description: Ward ID of the entity corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/IssueReporting/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.IssueTracking/IssueReporting/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### IssueReporting NGSI-v2 key-values Ejemplo    
Aquí hay un ejemplo de un IssueReporting en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
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
</details>    
#### IssueReporting NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de IssueReporting en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
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
    "type": "Text",  
    "value": "https://imgur.com"  
  },  
  "resolutionStatus": {  
    "type": "Text",  
    "value": "Assigned"  
  }  
}  
```  
</details>    
#### IssueReporting NGSI-LD key-values Ejemplo    
He aquí un ejemplo de IssueReporting en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:xYBR:0102",  
  "type": "IssueReporting",  
  "category": "Maintenance",  
  "categoryCode": "112",  
  "comments": "Road not in proper condition",  
  "departmentId": "12",  
  "landmark": "Near St.Andrews Church",  
  "mediaURL": "https://imgur.com",  
  "observationDateTime": "2021-03-11T15:51:02+05:30",  
  "reportId": "21645",  
  "resolutionStatus": "Assigned",  
  "subCategory": "Road Repair",  
  "subCategoryCode": "RM",  
  "title": "Road maintenance",  
  "titleCode": "RDM",  
  "wardId": "4",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.IssueTracking/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### IssueReporting NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de IssueReporting en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:xYBR:0102",  
    "type": "IssueReporting",  
    "category": {  
        "type": "Property",  
        "value": "Maintenance"  
    },  
    "categoryCode": {  
        "type": "Property",  
        "value": "112"  
    },  
    "comments": {  
        "type": "Property",  
        "value": "Road not in proper condition"  
    },  
    "departmentId": {  
        "type": "Property",  
        "value": "12"  
    },  
    "landmark": {  
        "type": "Property",  
        "value": "Near St.Andrews Church"  
    },  
    "mediaURL": {  
        "type": "Property",  
        "value": "https://imgur.com"  
    },  
    "observationDateTime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-03-11T15:51:02+05:30"  
        }  
    },  
    "reportId": {  
        "type": "Property",  
        "value": "21645"  
    },  
    "resolutionStatus": {  
        "type": "Property",  
        "value": "Assigned"  
    },  
    "subCategory": {  
        "type": "Property",  
        "value": "Road Repair"  
    },  
    "subCategoryCode": {  
        "type": "Property",  
        "value": "RM"  
    },  
    "title": {  
        "type": "Property",  
        "value": "Road maintenance"  
    },  
    "titleCode": {  
        "type": "Property",  
        "value": "RDM"  
    },  
    "wardId": {  
        "type": "Property",  
        "value": "4"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.IssueTracking/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
