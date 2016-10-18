Required

Simple example of requiring a phrase. 

```
-----
required
-----

Ships of the Russian Navy

select title,lang from solrdemo.wikipages where solr_query = 'content:(ships navy + "Ships of the Russian Navy")';

cqlsh:solrdemo> select title,lang,parent from solrdemo.wikipages where solr_query = 'content:(ships navy + "Ships of the Russian Navy")';

 title                                  | lang
----------------------------------------+------
 Russian destroyer Vice-Admiral Kulakov |   de
 Russian destroyer Vice-Admiral Kulakov |   es
 Russian destroyer Vice-Admiral Kulakov |   fr
 Russian destroyer Vice-Admiral Kulakov |   en
 Russian destroyer Vice-Admiral Kulakov |   ru

(5 rows)
```