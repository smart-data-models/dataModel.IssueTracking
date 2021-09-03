Entidad: Open311_ServiceType  
============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceType/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Según Open311 una entidad de tipo ServiceType es un tipo de solicitud de servicio 311 aceptable. Un tipo de solicitud puede ser único para la ciudad/jurisdicción.**  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `attributes`: Según la estructura [Service Definition](http://wiki.open311.org/GeoReport_v2/#get-service-definition) definida por Open 311.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `effectiveSince`: La fecha de creación del tipo de servicio. Esta fecha puede ser diferente de la fecha de creación de la entidad  - `group`: Una categoría para agrupar este tipo de servicio. Esto proporciona una manera de agrupar varios tipos de solicitudes de servicio bajo una categoría como el saneamiento  - `id`: Identificador único de la entidad  - `jurisdiction_id`: El ID único de la entidad legal del servicio (es decir, la ciudad).  - `keywords`: Una lista de etiquetas o palabras clave separadas por comas para ayudar a los usuarios a identificar el tipo de solicitud. Puede proporcionar sinónimos de service_name y group.  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: El nombre de este artículo.  - `open311:metadata`: Este campo no es estrictamente necesario ya que la entidad propuesta abarca también la definición de atributos. Si se define, su valor debe ser `true` si la propiedad `attributes` está definida y su valor de matriz no está vacío. En caso contrario, debe ser igual a `false`.  - `open311:type`: en tiempo real: El ID de la solicitud de servicio se devolverá inmediatamente después de que se envíe la solicitud de servicio: Se devolverá un token inmediatamente después de enviar la solicitud de servicio. Este token puede utilizarse posteriormente para devolver el ID de la solicitud de servicio. blackbox: No se devolverá ningún ID de solicitud de servicio después de enviar la solicitud de servicio. Enum:'tiempo real, lote, caja negra'.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `provider`: Proveedor del servicio  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `service_code`: El identificador único para el tipo de solicitud de servicio.  - `service_name`: El nombre legible del tipo de solicitud de servicio.  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `type`: Tipo de entidad NGSI. Tiene que ser Open311ServiceType    
Propiedades requeridas  
- `id`  - `type`    
Según [Open311](http://wiki.open311.org/GeoReport_v2/#get-service-list) una entidad de tipo `ServiceType` es un tipo de solicitud de servicio 311 aceptable. Un tipo de solicitud puede ser único para la ciudad/jurisdicción. Tenga en cuenta que este modelo de datos no ha sido armonizado al estilo. Hemos decidido mantener los mismos nombres de propiedades y la misma estructura, aunque creemos firmemente que se puede aprovechar el modelo Open311.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Open311_ServiceType:    
  description: 'As per Open311 an entity of type ServiceType is an acceptable 311 service request type. A request type can be unique to the city/jurisdiction.'    
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
    attributes:    
      description: "As per the [Service Definition](http://wiki.open311.org/GeoReport_v2/#get-service-definition) structure defined by Open 311."    
      items:    
        anyOf:    
          - type: string    
          - type: object    
          - type: array    
          - type: boolean    
          - type: number    
      type: array    
      x-ngsi:    
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
    effectiveSince:    
      description: 'The date on which the service type was created. This date might be different than the entity creation date'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    group:    
      description: 'A category to group this service type within. This provides a way to group several service request types under one category such as sanitation'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    jurisdiction_id:    
      description: 'The unique ID of the legal entity of the service (i.e. city).'    
      type: string    
      x-ngsi:    
        type: Property    
    keywords:    
      description: 'A comma separated list of tags or keywords to help users identify the request type. This can provide synonyms of the service_name and group.'    
      type: string    
      x-ngsi:    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    open311:metadata:    
      description: 'This field is not strictly needed as the proposed entity encompasses the attribute definition as well. If defined, its value must be `true` if the `attributes` property is defined and its array value is not empty. Otherwise it must be equal to `false`'    
      type: boolean    
      x-ngsi:    
        type: Property    
    open311:type:    
      description: 'realtime: The service request ID will be returned immediately after the service request is submitted. batch: A token will be returned immediately after the service request is submitted. This token can then be later used to return the service request ID. blackbox: No service request ID will be returned after the service request is submitted. Enum:''realtime, batch, blackbox''. '    
      enum:    
        - batch    
        - blackbox    
        - realtime    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *open311_servicetype_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    provider:    
      description: 'Provider of the service'    
      type: string    
      x-ngsi:    
        model: http://schema.org/provider    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Open311ServiceType'    
      enum:    
        - Open311ServiceType    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### Open311_ServiceType NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Open311_ServiceType NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "o311:servicetype-guadalajara-sidewalks",  
  "type": "Open311ServiceType",  
  "group": {  
    "type": "Text",  
    "value": "street"  
  },  
  "description": {  
    "type": "Text",  
    "value": "When a sidewalk is broken or dirty allows citizens to request a fix"  
  },  
  "service_code": {  
    "type": "Text",  
    "value": "234"  
  },  
  "service_name": {  
    "type": "Text",  
    "value": "Aceras"  
  },  
  "open311:type": {  
    "type": "Text",  
    "value": "realtime"  
  },  
  "jurisdiction_id": {  
    "type": "URL",  
    "value": "www.smartguadalajara.com"  
  },  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "2007-01-01T12:00:00Z"  
  },  
  "keywords": {  
    "type": "Text",  
    "value": "street,sidewalk, cleaning, repair"  
  },  
  "attributes": {  
    "type": "StructuredValue",  
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
#### Open311_ServiceType NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### Open311_ServiceType NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
