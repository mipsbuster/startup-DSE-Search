# Startup DSE Search

Work in progress and my attempts in quickly learning Datastax Enterprise Search. 

Hands on works best for my learning style. Ecountering problems, bugs and hurdles helps in learning and also developing emmpathy and understanding for others who are starting or further down this path. 

Goals:

- Create a quick start to learn the basic of DSE Search with only C* background and skill set.
- Understand the value in DSE search
- Understand the value in NLP
- Gain undertanding of pain points and challenges in search and NLP problems on large distributed datasets
- Gain basic knowledge on the vocabulary of search and NLP as realted to DSE Search
- Gain basic knowledge of the tools and techniques provided by DSE Search in solving Enterprise Search/NLP problems
- Understand the potential challenges and fears of other newbies to DSE Search and NLP
- Create examples in a number of different languages and ingest options to help understand the similarites and uniqueness of each stack

**NOTE** - This is a first pass draft and work in progress.. Not intended for public usage or final solutions. Scratchpad for current learning. I have a number of errors and other issues to fix. 

## Requirements

The following is a list of the general requirements and knowledge base required to get a good first pass understanding of DSE Search. 

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

### Overview

Wanted to start out with a NLP or document focus on the first pass. Also not sure how to do 'Internet of things' with features like multilanguage. So, changed to a document based use case. Will do the 'internet of things' as a seond use case. 

Business use case 1: 

Load document centric data dynamically and randomly from a current Wikipedia data source (www.wikipedia.com) and provide a rich set of documents for learning DSE Search and NLP.  Add additional documents on demand. 

Ex. attributes to load ( title, parent, content, lat/lon, lang, others to be added)

Provide documents for DSE Search in multiple languages. 

Business use case 2:

Internet of things.Simulate internet of things as source of data for DSE Search. 

### Architecture

Phase 1 - Simple cqlsh client (current state)

Phase 2 - *Command line application client and API (future)*

Phase 3 - *Visual UI client(future)*

[add content]

### Modeling

[add content]

### Ingest

Develop simple program for seeding DSE with random data from Wikipedia. Pages are loaded in a number of languages. 

Ingest Process

### Setup 

Cluster : DSE 4.8.8. cluster running on AWS. All nodes are running C* and Search, 

Client: python 2.7.x application and SSH into cluster to execute cqlsh commands for test queries. 

### DSE Search Examples

Following are examples from the 'Requirements Section' above and are part if Business Use Case 1.

First pass is to provide cqlsh commands/scripts. then add the same cqlsh from a client application. 

Clients:

1. Client - 1 DSE cqlsh commands and interface(links below)
2. Client -2 propsed application client with DSE driver(to be developed later)

The following are links to cqlsh examples for each use case requirement. 

#### CQLSH - Search and Retrieve results in cqlsh:

- [Fuzzy Searching](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-fuzzy.md)
- Mulit Language
- [Sort/order results](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-sort.md)
- [Filter out any common words](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-stopwords.md)
- [Retrieve faceted results](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-facet.md)
- Find results by geo location within x distance
- Averages



#### CQLSH - Other SOLR queries and Features

- [JSON query](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-json.md)
- [Counts](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-count.md)
- [Range Search](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-range.md)
- [Term Boosting](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-termboosting.md)
- [Required](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-required.md)
- [Boolean](https://github.com/mipsbuster/startup-DSE-Search/blob/master/docs/SOLR-boolean.md)

