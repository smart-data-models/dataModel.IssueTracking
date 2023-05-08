<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体: 服务_请求  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/service_requests/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**一个ServiceRequest类型的实体是一个可接受的Open 311服务请求。这种实体包含了Open 311在POST服务请求和GET服务请求中定义的所有属性**。  
版本：0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `agency_responsible[string]`: 请注意，这在语义上等同于schema.org的提供者属性（name subproperty）。  . Model: [http://schema.org/provider](http://schema.org/provider)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `device_id[*]`: 提交请求的设备的唯一设备ID。这通常只用于移动设备  . Model: [https://schema.org/URL](https://schema.org/URL)- `email[string]`: 业主的电子邮件地址。  - `expected_datetime[string]`: 服务请求可望得到满足的日期和时间。这可能是基于特定服务的服务水平协议。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `first_name[string]`: 名字。在美国，一个人的名字。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `jurisdiction_id[string]`: 服务的法律实体（即城市）的唯一ID。  - `last_name[string]`: 姓氏。在美国，一个人的姓氏。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `media_url[string]`: 与请求有关的媒体的URL，如图片。  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `phone[string]`: 的电话号码。  . Model: [https://schema.org/Text](https://schema.org/Text)- `requested_datetime[string]`: 提出服务请求的日期和时间  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `service_code[string]`: 服务请求类型的唯一标识符。  - `service_name[string]`: 服务请求类型的人可读名称。  - `service_notice[string]`: 关于为满足请求或以其他方式处理所报告信息的预期行动的信息。  - `service_request_id[string]`: 创建的服务请求的唯一ID。  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `status[string]`: 允许人们搜索具有特定状态的请求。默认为所有状态；可以多次声明，以逗号分隔。Enum:'open, closed  - `status_notes[string]`: 解释为什么状态被改变为当前状态，或对当前状态的更多细节进行解释，而不是只用状态来传达。  - `type[string]`: NGSI 实体类型。它必须是 service_requests。Enum:'service_requests'（服务请求）。  - `updated_datetime[string]`: 服务请求最后被修改的日期和时间。对于status=closed的请求，这将是该请求被关闭的日期。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
一个`服务请求'类型的实体是一个可接受的Open 311服务请求。这种实体包含了Open 311在[POST服务请求](http://wiki.open311.org/GeoReport_v2/#post-service-request)和[GET服务请求](http://wiki.open311.org/GeoReport_v2/#get-service-request)中定义的所有属性。使用这个数据模型和FIWARE NGSI第二版的实现，可以直接实现符合Open 311规范的服务。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
service_requests:    
  description: An entity of type ServiceRequest is an acceptable Open 311 service request. Such entity encompasses all the properties defined by Open 311 at POST Service Request and GET Service Request.    
  properties:    
    address:    
      description: The mailing address    
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
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government.'    
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
        streetNr:    
          description: Number identifying a specific property on a public street.    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    agency_responsible:    
      description: 'Property. Please note that this is semantically equivalent to the provider property (name subproperty) of schema.org. Model:''http://schema.org/provider'''    
      type: string    
      x-ngsi:    
        model: http://schema.org/provider    
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
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity.    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    device_id:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: 'Relationship. The unique device ID of the device submitting the request. This is usually only used for mobile devices. Model:''https://schema.org/URL'''    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    email:    
      description: Email address of owner.    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    expected_datetime:    
      description: 'Property. The date and time when the service request can be expected to be fulfilled. This may be based on a service-specific service level agreement. Model:''https://schema.org/DateTime'''    
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
      anyOf: &service_requests_-_properties_-_owner_-_items_-_anyof    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    jurisdiction_id:    
      description: Property. The unique ID of the legal entity of the service (i.e. city).    
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
        - description: GeoProperty. Geojson reference to the item. Point    
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
        - description: GeoProperty. Geojson reference to the item. LineString    
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
        - description: GeoProperty. Geojson reference to the item. Polygon    
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
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
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
    media_url:    
      description: 'Property. A URL to media associated with the request, eg an image. Model:''https://schema.org/URL'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: The name of this item.    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf: *service_requests_-_properties_-_owner_-_items_-_anyof    
        description: Property. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    phone:    
      description: The telephone number.    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    requested_datetime:    
      description: 'Property. The date and time when the service request was made. Model:''https://schema.org/DateTime'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
    service_code:    
      description: Property. The unique identifier for the service request type.    
      type: string    
      x-ngsi:    
        type: Property    
    service_name:    
      description: Property. The human readable name of the service request type.    
      type: string    
      x-ngsi:    
        type: Property    
    service_notice:    
      description: Property. Information about the action expected to fulfill the request or otherwise address the information reported.    
      type: string    
      x-ngsi:    
        type: Property    
    service_request_id:    
      description: Property. The unique ID of the service request created.    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Property. Allows one to search for requests which have a specific status. This defaults to all statuses; can be declared multiple times, comma delimited. Enum:''open, closed'''    
      enum:    
        - closed    
        - open    
      type: string    
      x-ngsi:    
        type: Property    
    status_notes:    
      description: Property. Explanation of why status was changed to current state or more details on current status than conveyed with status alone.    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'Property. NGSI Entity type. It has to be service_requests. Enum:''service_requests'''    
      enum:    
        - service_requests    
      type: string    
      x-ngsi:    
        type: Property    
    updated_datetime:    
      description: 'Property. The date and time when the service request was last modified. For requests with status=closed, this will be the date the request was closed. Model:''https://schema.org/DateTime'''    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/service_requests/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.IssueTracking/service_requests/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### service_requests NGSI-v2 key-values 示例  
下面是一个以JSON-LD格式作为key-values的service_requests的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### service_requests NGSI-v2 normalized 示例  
下面是一个规范化的JSON-LD格式的service_requests的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### service_requests NGSI-LD key-values 示例  
下面是一个以JSON-LD格式作为key-values的service_requests的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "service-request:638344",  
    "type": "Open311ServiceRequest",  
    "address_string": "Calle San Juan Bautista, 2",  
    "agency_responsible": "Ayuntamiento de Ciudad",  
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
    "description": "Acera en mal estado con bordillo partido en dos",  
    "expected_datetime": "2010-04-15T06:37:38-08:00",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -3.164485591715449,  
            40.62785133667262  
        ]  
    },  
    "media_url": "http://exaple.org/media/638344.jpg",  
    "requested_datetime": "2010-04-14T06:37:38-08:00",  
    "service_code": "234",  
    "service_name": "Aceras",  
    "service_request_id": "638344",  
    "status": "closed",  
    "status_notes": "Duplicate request.",  
    "updated_datetime": "2010-04-14T06:37:38-08:00",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.IssueTracking/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### service_requests NGSI-LD规范化示例  
下面是一个规范化的JSON-LD格式的service_requests的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Open311ServiceRequest:service-request:638344",  
    "type": "Open311ServiceRequest",  
    "address_string": {  
        "type": "Property",  
        "value": "Calle San Juan Bautista, 2"  
    },  
    "agency_responsible": {  
        "type": "Property",  
        "value": "Ayuntamiento de Ciudad"  
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
    "description": {  
        "type": "Property",  
        "value": "Acera en mal estado con bordillo partido en dos"  
    },  
    "expected_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-15T06:37:38-08:00Z"  
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
    "media_url": {  
        "type": "Property",  
        "value": "http://exaple.org/media/638344.jpg"  
    },  
    "requested_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-14T06:37:38-08:00"  
        }  
    },  
    "service_code": {  
        "type": "Property",  
        "value": "234"  
    },  
    "service_name": {  
        "type": "Property",  
        "value": "Aceras"  
    },  
    "service_request_id": {  
        "type": "Property",  
        "value": "638344"  
    },  
    "status": {  
        "type": "Property",  
        "value": "closed"  
    },  
    "status_notes": {  
        "type": "Property",  
        "value": "Duplicate request."  
    },  
    "updated_datetime": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2010-04-14T06:37:38-08:00"  
        }  
    },  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.IssueTracking/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
