# a_star_algoritma_ile_labirent_cozme
## KULLANİLAN ALGORİTMA: 

### A*(STAR) ALGORITMASI:
A* algoritması yapı olarak muteber sezgisel (admissable heuristic) bir algoritma olarak sınıflandırılabilir. Bunun sebebi algoritmasının mesafe hesaplamada kullandığı fonksiyondur: 

f(n) = g(n) + h(n) denklemindeki 

 f(n) = hesaplama yapan sezgisel (heuristic) fonksiyon. 

g(n) = Başlangıç düğümünden mevcut düğüme kadar gelmenin maliyeti 

h(n) = Mevcut düğümden hedef düğüme varmak için tahmin edilen mesafe. 

Dikkat edileceği üzere f(n) fonksiyonunun sezgisel olma sebebi, bu fonksiyon içerisinde bulunan ve tahmine dayalı olan h(n) sezgisel fonksiyonudur. 

## Algoritmanın çalışması: 

 Algoritma yukarıdaki toplama işlemini kullanan oldukça basit bir yapıya sahiptir. Veri yapısı olarak bir öncelik sırası (priority queue) kullanan algoritmada en öncelikli olan düğüm f(n) değeri en düşük olan düğümdür. 

 Algoritma her adımda en düşük değeri (Ve dolayısıyla en önemli) düğümü alır (yani bu düğüme gider) ve düğümü sıradan (queue) çıkarır. 

Gidilen bu düğüme göre komşu olan bütün düğümlerin değerleri güncellenir (artık bu düğüme gelmenin bir maliyeti vardır ve dikkat edilirse f(n) fonksiyonu içerisinde bu değer yer almaktadır.) 

Algoritma yukarıdaki adımları hedefe varana kadar (yani hedef düğümü öncelik sırasında (priority queue) en öne gelene kadar) veya sırada (queue) düğüm kalmayana kadar tekrarlar.

<img src="https://github.com/sudebeyza/a_star_algoritma_ile_labirent_cozme/assets/115953068/734cbbf4-6f75-4092-928c-5d1d79f0fc74" width=200 height=300>

# SONUCLAR
PROJE CIKTILARI: 

Baslangic noktasi belirlendi. 


 <img src="https://github.com/sudebeyza/a_star_algoritma_ile_labirent_cozme/assets/115953068/49e90842-c527-403d-a6f8-afc7d9549954" width=300 height=200>

Bitis noktasi belirlendi. 



<img src="https://github.com/sudebeyza/a_star_algoritma_ile_labirent_cozme/assets/115953068/8a67eb0d-16c5-4ef5-8a5c-c911ca640891" width=300 height=200>

Duvarlar belirlendi. 

<img src="https://github.com/sudebeyza/a_star_algoritma_ile_labirent_cozme/assets/115953068/12a18112-a309-407e-8eaa-7de0c093b7f1" width=300 height=200>


A* algoritmasi kullanilarak labirent cozuldu.


<img src="https://github.com/sudebeyza/a_star_algoritma_ile_labirent_cozme/assets/115953068/20bbcab0-1d7a-42ca-a15c-7f06706ba0e2" width=300 height=200>

 

 

 

 

 

 

 

     4.	A* algoritmasi kullanilarak labirent cozuldu. 

 



 
 
