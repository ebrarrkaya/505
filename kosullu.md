# KOŞULLU YAPILAR
Bir duruma bağlı olarak, belirlenen koşullara göre bizler, bilgisayara istediğimiz işlemi yaptırabiliriz. Bu işlemleri, koşullu yapılarımızı yanı, if-elif-else yapılarını kullanarak gerçekleştiririz. Tabi ki bu yapıları kullanmadan önce bir koşulun ne olduğu hakkında bilgi sahibi olalım. Koşul, bir olayın gerçekleşme durumunu veya bir durumun doğruluğunu kontrol etmek için kullanılan şart veya ifadedir. Programlama bağlamında koşul, belirli bir durumun doğru veya yanlış olup olmadığını kontrol etmek için kullanılan ifadelerdir. Günlük yaşantımızdan koşullu yapılara örnek cümlelerimizi inceleyim.

>> Eğer yağmur yağıyorsa, şemsiyeni al.

>> Dersten geçmek istiyorsan, 50'nin üzerinde not al.

>> Güneşe alerjin varsa, güneş kremi sür.

>> Eğer uçağa biniyorsan, check-in yaptır.

Mantığı hakkında bilgi sahibi olduğumuza göre şimdi bizler için önemli olan girinti kavramı hakkında bilgi sahibi olalım. Girinti, Python programlama dilinde oldukça önemli bir kavramdır. Python, diğer bazı programlama dilleri gibi süslü parantezler {) veya başka bir belirteç kullanmaz. Bunun yerine, Python, programları düzenlemek ve kod bloklarını tanımlamak için girinti (indentation) adı verilen boşluk karakterleri kullanır. Girinti, programın okunabilirliğini arttırır. Örneğin koşullu yapılarımızı oluşturduğumuz zaman, koşula bağlı işlemler yapılacaksa, o koşulun girintisi oluşturulmalı ve yapılacakları belirtilmelidir. Python'da koşullu yapılar, fonksiyonlar ve döngüler gibi yapılarda girinti oluşturulmalıdır. Aksi durumda, bir koşula, döngüye ve fonksiyona bir görev ataması gerçekleştirilemez. Python'da girinti oluşturulmak isteniyorsa, TAB tuşu kadar boşluk bırakılmalıdır.

# İF KOŞULU
Python'da if koşulu, programların belirli koşullar altında farklı işlemler yapmasını sağlayan temel yapı taşlarından biridir. İf koşulu, belirtilen şartın doğru ol duğu durumlarda belirli kod bloklarının çalıştırılmasını sağlar. İf koşulunu her zaman ilk koşulumuz için kullanmaktayız. İf koşulunu kullanabilmek için başta bir durum belirtmemiz gerekir ve if ifadesini yazdıktan hemen sonra parantez içerisinde kontrol durumu belirlenir. Bir alt satırda ise şartlar sağlanıyorsa yapılmak istenen işlem belirlenir. Tabii ki girintiye dikkat etmeliyiz. Eğer koşul sağlanırsa if çalışır ve istenen işlem gerçekleşir.

Örnek Kod:

yas=int(input("Lutfen yasinizi giriniz:"))

if (yas>=18):
    print("Ehliyet alabilirsiniz")

Örnek Kod 2:

instagram_db={
"usernamedb":"ebrr0ck",
"sifredb":"12345",
"date":"22.11.2024 - 15:18.15116"
}

username=input("Lutfen kullanici adini gir:")

password=input("Lutfen sifreni gir:")
if (instagram_db["usernamedb"]==username and instagram_db["sifredb"]==password):

    print("Sisteme hosgeldiniz {}".format(username))
    print("Sisteme en son giris tarihi: {}".format(instagram_db["date"]))

<a href="https://github.com/ebrarrkaya/505/blob/597e4d24b50df1fe62b802c3eb7f6c961275df98/a9.png">ÇIKTI İÇİN TIKLAYINIZ</a>
