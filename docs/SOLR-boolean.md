# Boolean

Example for boolean

```
-----
Boolean
-----

select title,lang from wikipages where solr_query = 'content:(river and people)';
cqlsh> select title,lang from solrdemo.wikipages where solr_query = 'content:(river and people)';

 title               | lang
---------------------+------
 Treaty of Lancaster |   de
 Treaty of Lancaster |   fr
 Treaty of Lancaster |   en
 Treaty of Lancaster |   es
 Treaty of Lancaster |   ru
      1870s in music |   en
      1870s in music |   es
      1870s in music |   ru
      1870s in music |   de
      1870s in music |   fr

(10 rows)
cqlsh>

cqlsh> select title,lang from solrdemo.wikipages where solr_query = 'content:(Treaty AND Lancaster)';

 title               | lang
---------------------+------
 Treaty of Lancaster |   de
 Treaty of Lancaster |   fr
 Treaty of Lancaster |   en
 Treaty of Lancaster |   es
 Treaty of Lancaster |   ru

(5 rows)
```

