# Count



Simple examples of counts from Wikipedia content. Shows counts of all docs containing the term. 

```
-----
COUNT
-----

SELECT count(*) FROM solrdemo.wikipages WHERE solr_query = '{"q":"content:\"man\""}' ;

cqlsh:solrdemo> SELECT count(*) FROM solrdemo.wikipages WHERE solr_query = '{"q":"content:\"river\""}' ;

 count
-------
    10

(1 rows)
```