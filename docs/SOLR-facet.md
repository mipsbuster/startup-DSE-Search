# Facet SOLR

Tied to query ...

Reference:

http://www.datastax.com/dev/blog/adv-solr-cqlc
The same goes for facet queries. Note that because of the way the cql protocol is designed (around rows and columns),
DSE returns the facet results inside a single cell in JSON format.

## Examples 

```
select title,lang FROM solrdemo.wikipages WHERE solr_query='{"facet":{"pivot":"lang"},"q":"content:river"}' ;

 facet_pivot
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {"lang":[{"field":"lang","value":"de","count":2},{"field":"lang","value":"en","count":2},{"field":"lang","value":"es","count":2},{"field":"lang","value":"fr","count":2},{"field":"lang","value":"ru","count":2}]}

(1 rows)
```

```
cqlsh:solrdemo> select * from solrdemo.wikipages where solr_query='{"facet":{"pivot":"category"},"q":"content:*.*"}' ;

 facet_pivot
--------------------------------------------------------------------------------------------------------------------
 {"category":[{"field":"category","value":"articles","count":38},,{"field":"category","value":"wikidata","count":16},{"field":"category","value":"de","count":14},{"field":"category","value":"2016","count":10},{"field":"category","value":"lacking","count":10},{"field":"category","value":"march","count":10},{"field":"category","value":"sources","count":10},{"field":"category","value":"text","count":10},{"field":"category","value":"province","count":9},{"field":"category","value":"алфавиту","count":9},{"field":"category","value":"викиданных","count":9},{"field":"category","value":"значения","count":9},{"field":"category","value":"из","count":9},{"field":"category","value":"категория:википедия:статьи","count":9},{"field":"category","value":"переопределением","count":9},{"field":"category","value":"по","count":9},
{"field":"category","value":"en","count":8},
{"field":"category","value":"liés","count":8},
{"field":"category","value":"на","count":6},{"field":"category","value":"россии","count":6},{"field":"category","value":"1744","count":5},{"field":"category","value":"1853","count":5},{"field":"category","value":"1870s","count":5},{"field":"category","value":"1930","count":5},{"field":"category","value":"1995","count":5},{"field":"category","value":"19th","count":5},{"field":"category","value":"2011","count":5},{"field":"category","value":"2013","count":5},{"field":"category","value":"alumni","count":5},{"field":"category","value":"america","count":5},{"field":"category","value":"american","count":5},{"field":"category","value":"appointed","count":5},{"field":"category","value":"august","count":5},{"field":"category","value":"australian","count":5},{"field":"category","value":"biographical","count":5},{"field":"category","value":"births","count":5},{"field":"category","value":"britain","count":5},{"field":"category","value":"category","count":5},{"field":"category","value":"century","count":5},{"field":"category","value":"cleveland","count":5},{"field":"category","value":"college","count":5},{"field":"category","value":"commons","count":5},{"field":"category","value":"coordinates","count":5},{"field":"category","value":"county","count":5},{"field":"category","value":"court","count":5},{"field":"category","value":"dates","count":5},{"field":"category","value":"deaths","count":5},{"field":"category","value":"decade","count":5},{"field":"category","value":"denizli","count":5},{"field":"category","value":"different","count":5},{"field":"category","value":"directory","count":5},{"field":"category","value":"district","count":5},{"field":"category","value":"dmy","count":5},{"field":"category","value":"eastern","count":5},{"field":"category","value":"established","count":5},{"field":"category","value":"external","count":5},{"field":"category","value":"federal","count":5},{"field":"category","value":"great","count":5},{"field":"category","value":"grover","count":5},{"field":"category","value":"harpalinae","count":5},{"field":"category","value":"hip","count":5},{"field":"category","value":"history","count":5},{"field":"category","value":"hop","count":5},{"field":"category","value":"id","count":5},{"field":"category","value":"identifiers","count":5},{"field":"category","value":"incorporating","count":5},{"field":"category","value":"indigenous","count":5},{"field":"category","value":"iroquois","count":5},{"field":"category","value":"judges","count":5},{"field":"category","value":"kingdom","count":5},{"field":"category","value":"labels","count":5},{"field":"category","value":"lancaster","count":5},{"field":"category","value":"language","count":5},{"field":"category","value":"links","count":5},{"field":"category","value":"microformats","count":5},{"field":"category","value":"missouri","count":5},{"field":"category","value":"music","count":5},{"field":"category","value":"needing","count":5},{"field":"category","value":"north","count":5},{"field":"category","value":"october","count":5},{"field":"category","value":"page","count":5},{"field":"category","value":"pennsylvania","count":5},{"field":"category","value":"peoples","count":5},{"field":"category","value":"record","count":5},{"field":"category","value":"references","count":5}]}

(1 rows)
```



```
cqlsh:solrdemo> select * from solrdemo.wikipages where solr_query='{"facet":{"pivot":"parent"},"q":"content:*.*"}' ;

 facet_pivot
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 {"parent":[{"field":"parent","value":"546179492","count":5},{"field":"parent","value":"585529230","count":5},{"field":"parent","value":"671068703","count":5},{"field":"parent","value":"711852350","count":5},{"field":"parent","value":"732830630","count":5},{"field":"parent","value":"740330635","count":5},{"field":"parent","value":"744316113","count":5},{"field":"parent","value":"119930723","count":4},{"field":"parent","value":"128044676","count":4},{"field":"parent","value":"63675982","count":3},{"field":"parent","value":"70055709","count":3},{"field":"parent","value":"76479781","count":3},{"field":"parent","value":"76566572","count":3},{"field":"parent","value":"93323468","count":2},{"field":"parent","value":"93939984","count":2},{"field":"parent","value":"94156070","count":2},{"field":"parent","value":"144905863","count":1},{"field":"parent","value":"151943843","count":1},{"field":"parent","value":"154896745","count":1},{"field":"parent","value":"156380831","count":1},{"field":"parent","value":"157565800","count":1},{"field":"parent","value":"95076812","count":1}]}

(1 rows)
```

