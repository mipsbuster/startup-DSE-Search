# Range Search



Simple example for range search 

```
-----
Range Search
-----

solr_query = 'term:[1 TO 10]'

cqlsh:solrdemo> select title, lang ,parent from wikipages where solr_query = 'parent:[1 TO 67927153]';

 title          | lang | parent
----------------+------+-----------
       Piz Zupò |   fr | 112090497
       Piz Zupò |   ru | 112090497
       Dioryche |   de | 546179492
       Dioryche |   en | 546179492
       Dioryche |   ru | 546179492
 1870s in music |   en | 585529230
 1870s in music |   es | 585529230
 1870s in music |   ru | 585529230
       Piz Zupò |   de | 112090497
       Piz Zupò |   es | 112090497
```