# Sort



Simple example of sort

```
cqlsh> select title from solrdemo.wikipages where solr_query='{"q":"title:*" , "sort":"title desc"}' limit 100;

 title
--------------------------------------------------
              Церковь Святого Великомученика Мины
              Церковь Святого Великомученика Мины
              Церковь Святого Великомученика Мины
 Система административного управления Туркестаном
 Система административного управления Туркестаном
 Система административного управления Туркестаном
               Рогаль-Левицкий, Дмитрий Романович
               Рогаль-Левицкий, Дмитрий Романович
               Рогаль-Левицкий, Дмитрий Романович
                      Панкратово (Дновский район)
                      Панкратово (Дновский район)
                      Панкратово (Дновский район)
                               Мезонсель-э-Виллер
                               Мезонсель-э-Виллер
                               Мезонсель-э-Виллер
                       Ильинка (Учалинский район)
                       Ильинка (Учалинский район)
                       Ильинка (Учалинский район)
                                 Дьюркович, Мария
                                 Дьюркович, Мария
                                 Дьюркович, Мария
                                    Zalika Souley
                                    Zalika Souley
                                    Zalika Souley
                                    Zalika Souley
                                   Wilhelm Bacher
                                   Wilhelm Bacher
                                   Wilhelm Bacher
                                   Wilhelm Bacher
                                Vincent Benedetti
                                Vincent Benedetti
                                Vincent Benedetti
                                Vincent Benedetti
                                         Verdenne
                                         Verdenne
                                         Verdenne
                                         Verdenne
                              Treaty of Lancaster
                              Treaty of Lancaster
                              Treaty of Lancaster
                              Treaty of Lancaster
                              Treaty of Lancaster
                        Transhumanismo libertario
                        Transhumanismo libertario
                            Sphagnum girgensohnii
                            Sankt Johann im Walde
                            Sankt Johann im Walde
                            Sankt Johann im Walde
                            Sankt Johann im Walde
           Russian destroyer Vice-Admiral Kulakov
           Russian destroyer Vice-Admiral Kulakov
           Russian destroyer Vice-Admiral Kulakov
           Russian destroyer Vice-Admiral Kulakov
           Russian destroyer Vice-Admiral Kulakov
                                         Piz Zupò
                                         Piz Zupò
                                         Piz Zupò
                                         Piz Zupò
                                 Molossus aztecus
                                 Molossus aztecus
                                 Mariano Barberán
                                 Mariano Barberán
             Liste der Kulturdenkmäler in Orsfeld
                    International Food Code (IFC)
                    International Food Code (IFC)
                    International Food Code (IFC)
                    International Food Code (IFC)
                    International Food Code (IFC)
                 Iglesia de San Agustín (Baliuag)
                 Iglesia de San Agustín (Baliuag)
                                Hydrofunk Records
                                Hydrofunk Records
                                Hydrofunk Records
                                Hydrofunk Records
                                Hydrofunk Records
                              Henry Samuel Priest
                              Henry Samuel Priest
                              Henry Samuel Priest
                              Henry Samuel Priest
                              Henry Samuel Priest
                                 Heinrich Maschke
                                   Hafizh Syahrin
                                   Hafizh Syahrin
                                   Hafizh Syahrin
                                   Hafizh Syahrin
                              Gruen Watch Company
                           Distrito de La Infanta
                           Distrito de La Infanta
                                         Dioryche
                                         Dioryche
                                         Dioryche
                                         Dioryche
                                         Dioryche
                                 Denizli Province
                                 Denizli Province
                                 Denizli Province
                                 Denizli Province
                                 Denizli Province
                                  Currituck-Insel
                         Critique arabe classique

(100 rows)
```