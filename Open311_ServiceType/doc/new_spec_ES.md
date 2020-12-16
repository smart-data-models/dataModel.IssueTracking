Entidad: Open311_ServiceType  
============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceType/LICENSE.md)  
Descripción global: **Según Open311 una entidad de tipo ServiceType es un tipo de solicitud de servicio 311 aceptable. Un tipo de solicitud puede ser único para la ciudad/jurisdicción.**  

## Lista de propiedades  

- `address`: La dirección postal.  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `attributes`: Según la estructura de [Definición del servicio](http://wiki.open311.org/GeoReport_v2/#get-service-definition) definida por Open 311.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `effectiveSince`: La fecha en la que se creó el tipo de servicio. Esta fecha podría ser diferente a la fecha de creación de la entidad  - `group`: Una categoría para agrupar este tipo de servicio dentro. Esto proporciona una manera de agrupar varios tipos de solicitud de servicio en una categoría como el saneamiento  - `id`: Identificador único de la entidad  - `jurisdiction_id`: La identificación única de la entidad legal del servicio (es decir, la ciudad).  - `keywords`: Una lista separada por comas de etiquetas o palabras clave para ayudar a los usuarios a identificar el tipo de solicitud. Esto puede proporcionar sinónimos del nombre_de_servicio y del grupo.  - `location`:   - `name`: El nombre de este artículo.  - `open311:metadata`: Este campo no es estrictamente necesario, ya que la entidad propuesta abarca también la definición de atributos. Si está definido, su valor debe ser "verdadero" si la propiedad "atributos" está definida y su valor de matriz no está vacío. De lo contrario debe ser igual a "falso".  - `open311:type`: en tiempo real: La identificación de la solicitud de servicio será devuelta inmediatamente después de que la solicitud de servicio sea presentada. lote: Se devolverá una ficha inmediatamente después de que se presente la solicitud de servicio. Esta ficha se puede utilizar más tarde para devolver el ID de la solicitud de servicio. caja negra: No se devolverá ninguna identificación de solicitud de servicio después de que se haya enviado la solicitud de servicio. Enum:'realtime, batch, blackbox'.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `provider`: Proveedor del servicio  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `service_code`: El identificador único para el tipo de solicitud de servicio.  - `service_name`: El nombre legible para los humanos del tipo de solicitud de servicio.  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `type`: Tipo de entidad NGSI. Tiene que ser Open311ServiceType    
Propiedades requeridas  
- `id`  - `type`    
Según [Open311](http://wiki.open311.org/GeoReport_v2/#get-service-list) una entidad de tipo "ServiceType" es un tipo de solicitud de servicio 311 aceptable. Un tipo de solicitud puede ser único para la ciudad/jurisdicción. Por favor, tenga en cuenta que este modelo de datos no ha sido armonizado en su estilo. Hemos decidido mantener los mismos nombres de propiedades y estructura, aunque creemos firmemente que el modelo Open311 puede ser aprovechado.  
## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
        type: string    
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
## Ejemplo de cargas útiles  
#### Open311_ServiceType NGSI V2 valores clave Ejemplo  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON como valores clave. Esto es compatible con NGSI V2 cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "o311:servicetype-guadalajara-sidewalks",  
  "type": "Open311ServiceType",  
  "dateCreated": "2007-01-01T12:00:00Z",  
  "jurisdiction_id": "www.smartguadalajara.com",  
  "open311:type": "realtime",  
  "service_code": 234,  
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
#### Open311_ServiceType NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "value": 234  
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
#### Open311_ServiceType NGSI-LD key-values Example  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "attributes": [{"code": "ISSUE_TYPE",  
                 "datatype": "singlevaluelist",  
                 "datatype_description": "",  
                 "description": "What is the identified problem at the "  
                                "sidewalk?",  
                 "order": 1,  
                 "required": True,  
                 "values": [{"key": 123, "name": "Bump"},  
                            {"key": 124, "name": "Dirty"}],  
                 "variable": True}],  
 "createdAt": "2007-01-01T12:00:00Z",  
 "description": "When a sidewalk is broken or dirty allows citizens to request "  
                "a fix",  
 "group": "street",  
 "id": "urn:ngsi-ld:Open311ServiceType:o311:servicetype-guadalajara-sidewalks",  
 "jurisdiction_id": "www.smartguadalajara.com",  
 "keywords": "street,sidewalk, cleaning, repair",  
 "open311:type": "realtime",  
 "service_code": 234,  
 "service_name": "Aceras",  
 "type": "Open311ServiceType"}  
```  
#### Open311_ServiceType NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un Open311_ServiceType en formato JSON-LD normalizado. Es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
        "value": 234  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
