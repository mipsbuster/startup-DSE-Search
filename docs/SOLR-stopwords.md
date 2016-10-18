# Stop Words

To begin, you need to define a field type that uses the ManagedStopFilterFactory, such as:

```
<fieldType class="org.apache.solr.schema.TextField" name="managed_en" positionIncrementGap="100">
  <analyzer>
    <tokenizer class="solr.StandardTokenizerFactory"/>
    <filter class="solr.ManagedStopFilterFactory" 
            managed="english" />
  </analyzer>
</fieldType>
```

In the wilipages example the content fields is to be configured. 

Upload the custom resource files:

The return code 0 indicates success.

```
$ dsetool reload_core solrdemo.wikipages solrconfig=solrconfig.xml schema=schema.xml reindex=false deleteAll=false
```



Check the core's config

```
dsetool get_core_schema solrdemo.wikipages current=true
```

here is the output

```
root@node0:~/solr# dsetool get_core_schema solrdemo.wikipages current=true
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<schema name="autoSolrSchema" version="1.5">
<types>
<fieldType class="org.apache.solr.schema.StrField" name="StrField"/>
<fieldType class="org.apache.solr.schema.TextField" name="TextField">
<analyzer>
<tokenizer class="solr.StandardTokenizerFactory"/>
<filter class="solr.LowerCaseFilterFactory"/>
</analyzer>
</fieldType>
<fieldType name="int" class="solr.TrieIntField" precisionStep="0" omitNorms="true" positionIncrementGap="0"/>
<fieldType class="org.apache.solr.schema.TextField" name="managed_en" positionIncrementGap="100">
  <analyzer>
    <tokenizer class="solr.StandardTokenizerFactory"/>
    <filter class="solr.ManagedStopFilterFactory" 
            managed="english" />
  </analyzer>
</fieldType>
</types>
<fields>
<field indexed="true" multiValued="false" name="title" stored="true" type="StrField"/>
<field indexed="true" multiValued="false" name="parent" stored="true" type="StrField"/>
<field indexed="true" multiValued="false" name="links" stored="true" type="TextField"/>
<field indexed="true" multiValued="false" name="content" stored="true" type="managed_en"/>
<field indexed="true" multiValued="false" name="lang" stored="true" type="StrField"/>
<field indexed="true" multiValued="true" name="category" stored="true" type="TextField"/>
</fields>
<uniqueKey>(title,parent,lang)</uniqueKey>
</schema>
```



```
http://host:port/solr/resource/keyspace.table/filename.ext
```

```
http://host:port/solr/resource/solrdemo.wikipages/stopwords.txt
```

check the output of stop words

```
curl "http://localhost:8983/solr/solrdemo.wikipages/schema/analysis/
stopwords/english"
```