# Fuzzy



Simple Fuzzy searching

```
cqlsh> select title from solrdemo.wikipages where solr_query = 'content:rive~2' LIMIT 100;

 title
----------------------------------------
                    Gruen Watch Company
                        Clauert-Rundweg
                      Hydrofunk Records
                      Hydrofunk Records
                      Hydrofunk Records
                      Hydrofunk Records
                      Hydrofunk Records
                    Treaty of Lancaster
                    Treaty of Lancaster
                    Treaty of Lancaster
                    Treaty of Lancaster
                    Treaty of Lancaster
                       Heinrich Maschke
                       Denizli Province
                       Denizli Province
                       Denizli Province
                       Denizli Province
                       Denizli Province
                  Sphagnum girgensohnii
                        Currituck-Insel
                         1870s in music
                         1870s in music
                         1870s in music
                         1870s in music
                         1870s in music
               Critique arabe classique
               Critique arabe classique
               Critique arabe classique
               Critique arabe classique
                         Wilhelm Bacher
                         Wilhelm Bacher
                         Wilhelm Bacher
                         Wilhelm Bacher
                                   Cine
                                   Cine
                        Briesen-Kaserne
 Russian destroyer Vice-Admiral Kulakov
 Russian destroyer Vice-Admiral Kulakov
 Russian destroyer Vice-Admiral Kulakov
 Russian destroyer Vice-Admiral Kulakov
 Russian destroyer Vice-Admiral Kulakov
                         Hafizh Syahrin
                         Hafizh Syahrin
                         Hafizh Syahrin
                         Hafizh Syahrin
                                Apizaco
                                Apizaco
                        Calle Ave María
                        Calle Ave María
                         Cherry-Eisfall
    Церковь Святого Великомученика Мины
    Церковь Святого Великомученика Мины
    Церковь Святого Великомученика Мины
                               Verdenne
                               Verdenne
                               Verdenne
                               Verdenne
                       Mariano Barberán
                       Mariano Barberán
   Liste der Kulturdenkmäler in Orsfeld
                         Cristino Mallo
                         Cristino Mallo
                 Distrito de La Infanta
                 Distrito de La Infanta
                      Vincent Benedetti
                      Vincent Benedetti
                      Vincent Benedetti
                      Vincent Benedetti

(68 rows)
```





```
-----
fuzzy
------

1 and 2 are the only options..

select title from wikipages where solr_query = 'title:vice~1' LIMIT 100;
select title from wikipages where solr_query = 'title:rive~2' LIMIT 100;
select title,content,lang from wikipages where solr_query = 'content:vince~' LIMIT 1;


SELECT * FROM users where solr_query = '
{ "q": "*:*", "fq": "email:r\\\"q@example"}
';

select title from wikipages where solr_query='{"q": "*:*", "fq": "content:riv\\\"ri-"}
```