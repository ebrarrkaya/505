# DEMET KAVRAMI
Demetler de listeler gibi çoklu veri tiplerini tutmamızı sağlayan dizilerdir. Yani içerisinde birden fazla farklı veri tipinde elemanlar bulundurabilmektedir. Demetlerin ayırt edici özellikleri ise, normal parantez () kullanılarak oluşturulması ve içerisindeki elemanlara müdahale edilememesidir.

ÖRNEK:

demet=(1,2,3,5)

print(demet)

print(demet[2])

<a href="https://github.com/ebrarrkaya/505/blob/f9c00091c864f2dc3cee98a3280fc13ae1466c0c/a1.png">ÇIKTI İÇİN TIKLAYINIZ</a>

Demetler de indeks numarasına sahiptir fakat indeks numaraları kullanılarak demet içerisinden herhangi bir değişim yapılamamaktadır. Şimdi hep birlikte örnek bir demet oluşturup "type()" fonksiyonunu kullanarak tipini bulalım:

Örnek Kod:

demet=(1,2.5,"Hello", 235)

print(type(demet))

<a href="https://github.com/ebrarrkaya/505/blob/527deb305db13de299a22e3eb00a43de2b46a49c/a2.png">Çıktımız ise şu şekilde olacaktır.</a>"tuple" yani demet anlamına gelmektedir.

# Demet İçerisindeki Elemanların Konumlarını Bulma
Demet içerisindeki elemanların konumlarını yani indeks numaralarını index() metoduyla bulabiliriz. Aynı şekilde her elemandan kaç tane olduğunu count() metodu ile hesaplayabiliriz. Örnek kodumuz üzerinden inceleyelim.

Örnek Kod:

demet=(1,2.5, "Hello",235)

print(demet.index("Hello"))

<a href="https://github.com/ebrarrkaya/505/blob/75e16ba77238793b44ba3f51291a9db9e448c6b7/A3.png">ÇIKTI İÇİN TIKLAYINIZ</a>

Örnek Kod 2:

demet=(1,2.5, "Hello",235)

print(demet.count(235))

<a href="https://github.com/ebrarrkaya/505/blob/b5ccc1e402d9610ee877ff8b91d18e6badb28b62/a4.png">ÇIKTI İÇİN TIKLAYINIZ</a>
