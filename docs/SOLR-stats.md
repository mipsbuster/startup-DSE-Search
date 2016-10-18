# Stats



Simple stats

```
curl "http://localhost:8983/solr/solrdemo.wikipages/select?parent=*:*"
```



```
curl "http://localhost:8983/solr/solrdemo.wikipages/select?q=*:*&fq={!tag=stock_check}inStock:true&stats=true&stats.field={!ex=stock_check+key=instock_prices+min=true+max=true+mean=true+percentiles='90,99'}parent&stats.field={!key=all_prices}parent&rows=0&indent=true"
```

