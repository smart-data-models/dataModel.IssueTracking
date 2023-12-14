<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ: service_requests  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.IssueTracking/blob/master/service_requests/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバル記述：**ServiceRequest型のエンティティは、受け入れ可能なOpen 311サービスリクエストである。このようなエンティティは、Open 311 が POST Service Request および GET Service Request で定義したすべてのプロパティを包含する**。  
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
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `agency_responsible[string]`: これは、schema.orgのプロバイダ・プロパティ（nameサブプロパティ）と意味的に同等であることに注意してください。  . Model: [http://schema.org/provider](http://schema.org/provider)- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `device_id[*]`: リクエストを送信するデバイスの一意なデバイスID。これは通常モバイルデバイスにのみ使用されます。  . Model: [https://schema.org/URL](https://schema.org/URL)- `email[idn-email]`: 所有者のEメールアドレス  - `expected_datetime[string]`: サービス要求が達成されると予想される日時。これは、サービス固有のサービスレベル契約に基づいている場合があります。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `first_name[string]`: ジブンネーム。米国では、人物のファーストネームは以下の通り。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意識別子  - `jurisdiction_id[string]`: サービスの法人（例：市）の固有ID  - `last_name[string]`: 姓。米国では、姓は「人」である。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `media_url[string]`: リクエストに関連するメディアのURL（例：画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `phone[string]`: 電話番号  . Model: [https://schema.org/Text](https://schema.org/Text)- `requested_datetime[string]`: サービスリクエストが行われた日時  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `service_code[string]`: サービス要求タイプの一意な識別子  - `service_name[string]`: サービス要求タイプの人間が読める名前  - `service_notice[string]`: 要請を満たすため、または報告された情報に対処するために期待される措置に関する情報  - `service_request_id[string]`: 作成されたサービスリクエストの固有ID  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `status[string]`: 特定のステータスを持つリクエストを検索できるようにします。カンマ区切りで複数回宣言することができます。列挙型:'オープン、クローズ  - `status_notes[string]`: ステータスが現在の状態に変更された理由の説明、またはステータスのみで伝えられるよりも詳細な現在のステータスの説明  - `type[string]`: NGSIエンティティタイプ。これは service_requests でなければならない。Enum:'サービスリクエスト'  - `updated_datetime[string]`: サービスリクエストが最後に変更された日時。status=closedのリクエストの場合、これはリクエストがクローズされた日付になります。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
ServiceRequest` 型のエンティティは、受け入れられる Open 311 サービスリクエストである。このようなエンティティは、[POST Service Request](http://wiki.open311.org/GeoReport_v2/#post-service-request)と[GET Service Request](http://wiki.open311.org/GeoReport_v2/#get-service-request)でOpen 311によって定義されたすべてのプロパティを包含する。このデータモデルとFIWARE NGSIバージョン2の実装を使用すれば、Open 311仕様に準拠したサービスを実装するのは簡単です。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
service_requests:    
  description: An entity of type ServiceRequest is an acceptable Open 311 service request. Such entity encompasses all the properties defined by Open 311 at POST Service Request and GET Service Request.    
  properties:    
    account_id:    
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
      description: The unique ID for the user account of the person submitting the request    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
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
    address_string:    
      description: 'Human entered address or description of location. This is required if no lat/long or address_id are provided. This should be written from most specific to most general geographic unit, eg address number or cross streets, street name, neighborhood/district, city/town/village, county, postal code'    
      type: string    
      x-ngsi:    
        type: Property    
    agency_responsible:    
      description: Please note that this is semantically equivalent to the provider property (name subproperty) of schema.org    
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
    attributes:    
      description: Variable attributes of the request response    
      items:    
        properties:    
          code:    
            type: string    
          datatype:    
            enum:    
              - string    
              - number    
              - datetime    
              - singlevaluelist    
              - multivaluelist    
            type: string    
          datatype_description:    
            type: string    
          description:    
            type: string    
          order:    
            minimum: 1    
            type: number    
          required:    
            type: boolean    
          values:    
            items:    
              properties:    
                key:    
                  type: number    
                name:    
                  type: string    
              type: object    
            type: array    
          variable:    
            type: boolean    
        type: object    
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
    device_id:    
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
      description: The unique device ID of the device submitting the request. This is usually only used for mobile devices    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Relationship    
    email:    
      description: Email address of owner    
      format: idn-email    
      type: string    
      x-ngsi:    
        type: Property    
    expected_datetime:    
      description: The date and time when the service request can be expected to be fulfilled. This may be based on a service-specific service level agreement    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    first_name:    
      description: 'Given name. In the U.S., the first name of a Person'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    last_name:    
      description: 'Family name. In the U.S., the last name of a Person'    
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
    media_url:    
      description: 'A URL to media associated with the request, eg an image'    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    name:    
      description: The name of this item    
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
    phone:    
      description: The telephone number    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    requested_datetime:    
      description: The date and time when the service request was made    
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
      description: The unique identifier for the service request type    
      type: string    
      x-ngsi:    
        type: Property    
    service_name:    
      description: The human readable name of the service request type    
      type: string    
      x-ngsi:    
        type: Property    
    service_notice:    
      description: Information about the action expected to fulfill the request or otherwise address the information reported    
      type: string    
      x-ngsi:    
        type: Property    
    service_request_id:    
      description: The unique ID of the service request created    
      type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
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
      description: Explanation of why status was changed to current state or more details on current status than conveyed with status alone    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be service_requests. Enum:''service_requests'''    
      enum:    
        - service_requests    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program'    
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
## ペイロードの例  
#### service_requests NGSI-v2 キー値の例  
以下は、JSON-LD形式のservice_requestsをkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "service-request:638344",  
  "type": "service_requests",  
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
#### service_requests NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のservice_requestsの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "service-request:638344",  
  "type": "service_requests",  
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
    "type": "StructuredValue",  
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
#### service_requests NGSI-LD キー値の例  
以下は、JSON-LD形式のservice_requestsをkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使うと個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "service-request:638344",  
  "type": "service_requests",  
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
#### service_requests NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のservice_requestsの例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Open311ServiceRequest:service-request:638344",  
    "type": "service_requests",  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
