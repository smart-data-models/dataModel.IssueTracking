Entité : Open311_ServiceType  
============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/Open311_ServiceType/LICENSE.md)  
Description globale : **Selon l'Open311, une entité de type ServiceType est un type de demande de service 311 acceptable. Un type de demande peut être unique à la ville/juridiction.**  

## Liste des biens  

- `address`: L'adresse postale.  - `alternateName`: Un autre nom pour cet article  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `attributes`: Conformément à la structure [Définition du service] (http://wiki.open311.org/GeoReport_v2/#get-service-definition) définie par l'Open 311.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `effectiveSince`: La date à laquelle le type de service a été créé. Cette date peut être différente de la date de création de l'entité  - `group`: Une catégorie dans laquelle ce type de service peut être regroupé. Cela permet de regrouper plusieurs types de demandes de service sous une seule catégorie, comme par exemple l'assainissement  - `id`: Identifiant unique de l'entité  - `jurisdiction_id`: L'identifiant unique de l'entité juridique du service (c'est-à-dire la ville).  - `keywords`: Une liste de balises ou de mots-clés séparés par des virgules pour aider les utilisateurs à identifier le type de demande. Cela peut fournir des synonymes du nom_du_service et du groupe.  - `location`:   - `name`: Le nom de cet article.  - `open311:metadata`: Ce champ n'est pas strictement nécessaire car l'entité proposée englobe également la définition de l'attribut. S'il est défini, sa valeur doit être "true" si la propriété "attributs" est définie et que sa valeur de tableau n'est pas vide. Sinon, elle doit être égale à "faux".  - `open311:type`: en temps réel : Le numéro d'identification de la demande de service sera renvoyé immédiatement après la soumission de la demande de service. lot : Un jeton sera renvoyé immédiatement après la soumission de la demande de service. Ce jeton peut ensuite être utilisé ultérieurement pour renvoyer l'ID de la demande de service. blackbox : Aucun numéro d'identification de demande de service ne sera renvoyé après la soumission de la demande de service. Enum : "realtime, batch, blackbox".  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `provider`: Fournisseur du service  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `service_code`: L'identifiant unique pour le type de demande de service.  - `service_name`: Le nom lisible par l'homme du type de demande de service.  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `type`: Type d'entité NGSI. Il doit être de type Open311ServiceType    
Propriétés requises  
- `id`  - `type`    
Conformément à [Open311] (http://wiki.open311.org/GeoReport_v2/#get-service-list), une entité de type "ServiceType" est un type de demande de service 311 acceptable. Un type de demande peut être unique à la ville/juridiction. Veuillez noter que ce modèle de données n'a pas été harmonisé. Nous avons décidé de conserver les mêmes noms de propriétés et la même structure, bien que nous soyons convaincus que le modèle Open311 peut être exploité.  
## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Open311_ServiceType NGSI V2 Exemple de valeurs clés  
Voici un exemple d'un Open311_ServiceType au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### Open311_ServiceType NGSI V2 normalisé Exemple  
Voici un exemple d'un Open311_ServiceType au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### Exemple de valeurs clés Open311_ServiceType NGSI-LD  
Voici un exemple d'un Open311_ServiceType au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
#### Open311_ServiceType NGSI-LD normalisé Exemple  
Voici un exemple d'un Open311_ServiceType au format JSON-LD tel que normalisé. Il est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
