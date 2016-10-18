# Startup DSE Search

Goal is to create a quick start to learn the basic of DSE Search with only C* background and skill set.

Verions is DSE 4.8.8

The following Use Case was setup as the goals. 

## Requirements

```
Pre Requisites:     basic data modeling
Learning Objectives:  Understanding the setup/configuration and ways to query Cassandra data
Use Case:   Internet of Things, Query Engine to search through data
Deliverables:  Demonstrate from the SOLR admin UI and from cqlsh you can view the ingested data as per the requirements and be able to justify the use of various parsers and schema configurations

Learning Modules:
1.     Configuring DSE Search
2.     Tuning DSE Search
3.     Cassandra-loader
4.     dsetool – Solr configuration
5.     Solr Tokenizers – string vs text
6.     Solr – Query parsers
7.     Solr – ngrams, stemming and fuzzy searching
8.     Solr – languages
9.     Solr – geo location
10.   Solr syntax – basic
11.   Solr query syntax – advanced features
12.   CQLSH and solr_query

Use Case Requirements (again can use umbrella data model and data to load with some modifications)
·       Ingest given data
·       Be able to search and retrieve results:
o   In English, French and Spanish
o   Utilize fuzzy searching during any search
o   Sort/order results
o   Filter out any common words
o   Retrieve faceted results
o   Find results by geo location within x distance
o   Average sensor data that is returned in a given query
```

## Solution 

### Ingest

Develop simple python program for seeding DSE with random data from Wikipedia. Pages are loaded in a number of languages. 

Ingest Process

### Setup 

Cluster : DSE 4.8.8. cluster running on AWS. All nodes are running C* and Search, 

Client: python application and SSH into cluster to execute cqlsh commands for test queries. 

### DSE Search Examples

Following are examples for the Use Case provided. 

First pass is to provide cqlsh commands/scripts. then add the same cqlsh from a python client application. The following are links to cqlsh examples for each use case requirement

#### Search and Retrieve results in cqlsh:

- Fuzzy Searching
- Mulit Language
- Sort/order results
- Filter out any common words
- [Retrieve faceted results](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-facet.md)
- Find results by geo location within x distance
- Averages



#### Other SOLR queries and Features

- [JSON query](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-json.md)
- [Counts](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-count.md)
- [Range Search](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-range.md)
- [Term Boosting](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-termboosting.md)
- [Required](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-required.md)

