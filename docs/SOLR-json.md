JSON Query

Simple examples of JSON query with wikipedia data set

```
JSON

select title,lang from wikipages where solr_query = '{"q": "content:river"}' LIMIT 100;

cqlsh:solrdemo> select title,lang from wikipages where solr_query = '{"q": "content:river"}' LIMIT 100;

 title               | lang
---------------------+------
    Denizli Province |   es
    Denizli Province |   fr
    Denizli Province |   de
    Denizli Province |   en
    Denizli Province |   ru
 Treaty of Lancaster |   de
 Treaty of Lancaster |   fr
 Treaty of Lancaster |   en
 Treaty of Lancaster |   es
 Treaty of Lancaster |   ru

(10 rows)
cqlsh:solrdemo> select title,lang from wikipages where solr_query = '{"q": "content:river" , "fq": "lang:en"}' LIMIT 100;

 title               | lang
---------------------+------
    Denizli Province |   en
 Treaty of Lancaster |   en

(2 rows)

cqlsh:solrdemo> select title,lang from wikipages where solr_query = '{"q": "content:(river and man)" , "fq": "lang:en"}' LIMIT 100;

 title                                  | lang
----------------------------------------+------
                       Denizli Province |   en
                    Treaty of Lancaster |   en
 Russian destroyer Vice-Admiral Kulakov |   en
                      Hydrofunk Records |   en
                    Henry Samuel Priest |   en
                         1870s in music |   en

(6 rows)

For filter caching beter to do this...
select title,lang from wikipages where solr_query = '{ "fq": "lang:en", "q": "content:(river and man)"}' LIMIT 100;
cqlsh:solrdemo> select title,lang from wikipages where solr_query = '{ "fq": "lang:en", "q": "content:(river and man)"}' LIMIT 100;

 title                                  | lang
----------------------------------------+------
                    Treaty of Lancaster |   en
                       Denizli Province |   en
                    Henry Samuel Priest |   en
                         1870s in music |   en
 Russian destroyer Vice-Admiral Kulakov |   en
                      Hydrofunk Records |   en

(6 rows)
```