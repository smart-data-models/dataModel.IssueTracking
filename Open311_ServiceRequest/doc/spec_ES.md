Entidad: Open311_ServiceRequest  
===============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceRequest/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Una entidad de tipo ServiceRequest es una solicitud de servicio de Open 311 aceptable. Dicha entidad engloba todas las propiedades definidas por Open 311 en POST Service Request y GET Service Request.**  

## Lista de propiedades  

- `address`: La dirección postal  - `agency_responsible`: Tenga en cuenta que esto es semánticamente equivalente a la propiedad provider (subpropiedad name) de schema.org  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `device_id`: El ID de dispositivo único del dispositivo que envía la solicitud. Normalmente sólo se utiliza para los dispositivos móviles  - `email`: Dirección de correo electrónico del propietario.  - `expected_datetime`: La fecha y la hora en que se puede esperar que se cumpla la solicitud de servicio. Esto puede basarse en un acuerdo de nivel de servicio específico.  - `first_name`: Nombre de pila. En Estados Unidos, el nombre de pila de una persona.  - `id`: Identificador único de la entidad  - `jurisdiction_id`: El ID único de la entidad legal del servicio (es decir, la ciudad).  - `last_name`: Apellido. En Estados Unidos, el apellido de una persona.  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `media_url`: Una URL del medio asociado a la solicitud, por ejemplo, una imagen  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `phone`: El número de teléfono.  - `requested_datetime`: La fecha y la hora en que se realizó la solicitud de servicio  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `service_code`: El identificador único para el tipo de solicitud de servicio.  - `service_name`: El nombre legible del tipo de solicitud de servicio.  - `service_notice`: Información sobre la acción que se espera para satisfacer la solicitud o abordar de otro modo la información comunicada.  - `service_request_id`: El ID único de la solicitud de servicio creada.  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `status`: Permite buscar solicitudes que tengan un estado específico. Por defecto, todos los estados; puede declararse varias veces, delimitado por comas. Enum:'abierto, cerrado'  - `status_notes`: Explicación de por qué se ha cambiado el estado a la situación actual o más detalles sobre el estado actual que los transmitidos sólo con el estado.  - `type`: Tipo de entidad NGSI. Tiene que ser Open311ServiceRequest  - `updated_datetime`: La fecha y hora en que la solicitud de servicio fue modificada por última vez. Para las solicitudes con status=cerrado, será la fecha en que se cerró la solicitud    
Propiedades requeridas  
- `id`  - `type`    
Una entidad de tipo `ServiceRequest` es una solicitud de servicio de Open 311 aceptable. Dicha entidad abarca todas las propiedades definidas por Open 311 en [POST Service Request](http://wiki.open311.org/GeoReport_v2/#post-service-request) y [GET Service Request](http://wiki.open311.org/GeoReport_v2/#get-service-request). Utilizando este modelo de datos y una implementación de FIWARE NGSI versión 2 es sencillo implementar un servicio que cumpla con las especificaciones de Open 311.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
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
      type: Geoproperty    
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
      description: 'The telephone number.'    
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
            format: uri    
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
## Ejemplo de carga útil  
#### Open311_ServiceRequest NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una Open311_ServiceRequest en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Open311_ServiceRequest NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de una Open311_ServiceRequest en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Open311_ServiceRequest NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una Open311_ServiceRequest en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Open311_ServiceRequest NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de una Open311_ServiceRequest en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
