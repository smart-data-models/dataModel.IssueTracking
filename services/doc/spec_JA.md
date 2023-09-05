<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ：サービス  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/services/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバル記述：グローバル記述： **As per Open311 as an entity of type services is an acceptable 311 service request type.リクエストタイプは、都市/管轄に固有であることができます。  
バージョン: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `attributes[array]`: Open 311で定義された[Service Definition](http://wiki.open311.org/GeoReport_v2/#get-service-definition)構造に従って。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `effectiveSince[date-time]`: サービスタイプが作成された日付。この日付はエンティティの作成日と異なる場合があります。  . Model: [http://schema.org/DateTime](http://schema.org/DateTime)- `group[string]`: このサービスタイプをグループ化するカテゴリー。これは、複数のサービス要求タイプを衛生などの1つのカテゴリにグループ化する方法を提供します。  - `id[*]`: エンティティの一意識別子  - `jurisdiction_id[string]`: サービスの法人（例：市）の固有ID  - `keywords[string]`: ユーザーがリクエストタイプを識別するためのタグまたはキーワードのカンマ区切りリスト。これはservice_nameとgroupの同義語になります。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `open311:metadata[boolean]`: 提案されたエンティティは属性定義も包含するため、このフィールドは厳密には必要ない。定義されている場合、`attributes` プロパティが定義されていて、その配列の値が空でなければ `true` でなければならない。そうでない場合は `false` となる。  - `open311:type[string]`: リアルタイム：サービスリクエストIDは、サービスリクエスト送信直後に返されます：サービスリクエストが送信された直後にトークンが返されます。このトークンは後でサービスリクエストIDを返すために使用できます：サービスリクエストが送信された後、サービスリクエストIDは返されません。Enum:'リアルタイム, バッチ, ブラックボックス'.  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `provider[string]`: サービス提供者  . Model: [http://schema.org/provider](http://schema.org/provider)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `service_code[string]`: サービス要求タイプの一意な識別子  - `service_name[string]`: サービス要求タイプの人間が読める名前  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSIエンティティタイプ。サービスでなければならない。Enum:'サービス'  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Open311](http://wiki.open311.org/GeoReport_v2/#get-service-list)にあるように、`ServiceType`型のエンティティは、311サービスのリクエストタイプとして受け入れられる。リクエストタイプは都市/管轄区域に固有である。このデータモデルはスタイルが統一されていないことに注意してください。私たちは、Open311モデルを活用できると強く信じていますが、同じプロパティ名と構造を維持することにしました。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
services:    
  description: As per Open311 an entity of type services is an acceptable 311 service request type. A request type can be unique to the city/jurisdiction.    
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
    attributes:    
      description: "As per the [Service Definition](http://wiki.open311.org/GeoReport_v2/#get-service-definition) structure defined by Open 311"    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    effectiveSince:    
      description: The date on which the service type was created. This date might be different than the entity creation date    
      format: date-time    
      type: string    
      x-ngsi:    
        model: http://schema.org/DateTime    
        type: Property    
    group:    
      description: A category to group this service type within. This provides a way to group several service request types under one category such as sanitation    
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
    jurisdiction_id:    
      description: The unique ID of the legal entity of the service (i.e. city)    
      type: string    
      x-ngsi:    
        type: Property    
    keywords:    
      description: A comma separated list of tags or keywords to help users identify the request type. This can provide synonyms of the service_name and group    
      type: string    
      x-ngsi:    
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
    name:    
      description: The name of this item    
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
    provider:    
      description: Provider of the service    
      type: string    
      x-ngsi:    
        model: http://schema.org/provider    
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
      description: The unique identifier for the service request type    
      type: string    
      x-ngsi:    
        type: Property    
    service_name:    
      description: The human readable name of the service request type    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be services. Enum:''services'''    
      enum:    
        - services    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/services/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.IssueTracking/services/schema.json    
  x-model-tags: ""    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### サービス NGSI-v2 キー値の例  
以下は、JSON-LD形式でkey-valuesとしてサービスを提供する例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### サービス NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のサービスの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### サービス NGSI-LD キー値 例  
以下はJSON-LD形式でkey-valuesとしてサービスを提供する例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Open311ServiceType:o311:servicetype-guadalajara-sidewalks",  
    "type": "Open311ServiceType",  
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
    "jurisdiction_id": "www.smartguadalajara.com",  
    "keywords": "street,sidewalk, cleaning, repair",  
    "open311:type": "realtime",  
    "service_code": "234",  
    "service_name": "Aceras",  
    "@context": [  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.IssueTracking/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### サービス NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のサービスの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Open311ServiceType:o311:servicetype-guadalajara-sidewalks",  
    "type": "Open311ServiceType",  
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
    "createdAt": "2007-01-01T12:00:00Z",  
    "description": {  
        "type": "Property",  
        "value": "When a sidewalk is broken or dirty allows citizens to request a fix"  
    },  
    "group": {  
        "type": "Property",  
        "value": "street"  
    },  
    "jurisdiction_id": {  
        "type": "Property",  
        "value": "www.smartguadalajara.com"  
    },  
    "keywords": {  
        "type": "Property",  
        "value": "street,sidewalk, cleaning, repair"  
    },  
    "open311:type": {  
        "type": "Property",  
        "value": "realtime"  
    },  
    "service_code": {  
        "type": "Property",  
        "value": "234"  
    },  
    "service_name": {  
        "type": "Property",  
        "value": "Aceras"  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
