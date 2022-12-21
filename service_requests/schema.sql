/* (Beta) Export of data model service_requests of the subject dataModel.IssueTracking for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE status_type AS ENUM ('closed', 'open');CREATE TYPE service_requests_type AS ENUM ('service_requests');
CREATE TABLE service_requests (address json, agency_responsible text, alternateName text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, device_id text, email text, expected_datetime text, first_name text, id text, jurisdiction_id text, last_name text, location json, media_url text, name text, owner json, phone text, requested_datetime text, seeAlso json, service_code text, service_name text, service_notice text, service_request_id text, source text, status status_type, status_notes text, type service_requests_type, updated_datetime text);