# MLprototipleri

Bu depo, temel makine öğrenmesi algoritmalarının Python ve NumPy üzerinden uygulanması ile ilgili çalışmalarımı kayıt altına almak amacı ile oluşturuldu.
Asıl hedef, makine öğrenimi ile ilgili kütüphanelerin kullanımından ziyade matematiksel temellerin anlaşılmasıdır.

### LinearRelation.py: 
Bu kod, temel olarak aralarında doğrusal ilişkilerin bulunduğu veri kümelerinde öğrenme gerçekleştirir. Örnek olarak girdi katmanı 3, çıktı katmanı ise 2 katmandan oluşan bir yapay sinir ağı üzerinde çalışılmıştır,
bundan dolayı girdi verileri sıralı 3'lüler, çıtkı verileri ise sıralı 2'liler yapısındadır. 
(a,b,c) şeklindeki bir sıralı üçlü için belirlenmiş ilişki (a+b+c,2c-b) şeklindedir.

### BackProg..py:
Bu kod ise tek-katmanlı sinir ağlarının üstesinden gelemediği XOR öğrenme probleminin geri yayılım algoritması aracılığı ile çok katmanlı sinir ağı üzerinden çözülmesini amaçlamaktadır. 
