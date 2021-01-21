# dataModel.IssueTracking
These data models allow to perform civic issue tracking. They have been designed with a view to enabling trivial interoperability between FIWARE NGSI version 2 and NGSI-LD and [Open311](http://www.open311.org/). As a result, property names have not been normalized to the `camelCase`syntax, they remain as currently specified by Open311. That is the rationale behind naming entity types with `Open311` as prefix. However, a few properties are added, so that FIWARE NGSI version 2 implementations can properly store and serve Open 311 data.
In the medium term, might propose to the Open311 Community a harmonized data model aligned with the rest of smart data models and schema.org. In fact, using these data models and a FIWARE NGSI version 2 o rNGSI-LD implementation it is trivial to implement the APIs proposed by Open311. Another option would be the use of [JSON-LD](http://json-ld.org) to define equivalencies and mappings between a FIWARE / Schema.org data model and Open 311.

### List of data models

The following entity types are available:
- [Open311_ServiceRequest](https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/Open311_ServiceRequest/README.md). An entity of type ServiceRequest is an acceptable Open 311 service request. Such entity encompasses all the properties defined by Open 311 at POST Service Request and GET Service Request.

- [Open311_ServiceType](https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/Open311_ServiceType/README.md). As per Open311 an entity of type ServiceType is an acceptable 311 service request type. A request type can be unique to the city/jurisdiction.



### Contributors
[Link](https://github.com/smart-data-models/dataModel.IssueTracking/blob/master/CONTRIBUTORS.yaml) to the 4 current contributors of the data models of this Subject.


### Contribution
You can raise an [issue](https://github.com/smart-data-models/dataModel.IssueTracking/issues) or submit your [PR](https://github.com/smart-data-models/dataModel.IssueTracking/pulls) on existing data models


