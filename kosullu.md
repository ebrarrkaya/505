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

# ELİF KOŞULU
Elif koşulu, ikiden fazla koşulumuz varsa ilk koşul hariç diğer koşulları oluşturmak için kullanılmaktadır. Elif ifadesini kullandıktan sonra (tıpkı if koşulunda olduğu gibi) parantez içerisinde koşul ifademizi belirtiriz ve parantezi kapattıktan sonra iki nokta üst üste sembolunu kullanırız. Yani girinti oluşturmalıyız. Şimdi bu duruma örnek algoritma oluşturup, daha sonra ise algoritmayı kodlarımıza derleyelim.

Örnek Kod:

deger1=int(input("Lutfen birinci degeri giriniz: "))

deger2=int(input("Lutfen ikinci degeri giriniz: "))

deger3=int(input("Lutfen ucuncu degeri giriniz: "))

if deger1>=deger2 and deger1>=deger3:

    print("{} degeri en buyuk sayidir.".format(deger1))
elif deger2>=deger1 and deger2>=deger3:

    print("{} degeri en buyuk sayidir.".format(deger2))
elif deger3>=deger1 and deger3>=deger2:

    print("{} degeri en buyuk sayidir.".format(deger3))

<a href="https://github.com/ebrarrkaya/202/blob/0b813e65fdfedbdac3fe98857f7cfb01412d8258/DDDD.png">ÇIKTI İÇİN TIKLAYINIZ</a>

#  ELSE KOŞULU

Else ifadesi bizim için "Girilen hiçbir koşul sağlanmıyorsa" anlamına gelmektedir, else ifadesinden sonra herhangi bir kontrol durumu girmemize gerek yoktur çünkü zaten kendi başına bir koşul belirtmektedir. Bu yüzden else koşulunda da girinti oluşturulması gereklidir.

Örnek Kod 1:

yas=int(input("Lutfen yasinizi giriniz: "))

if(yas>=18):

    print("Araba ve motor ehliyeti alabilirsiniz!")
elif(yas>=15):

    print("Motor ehliyeti alabilirsiniz!")
else:

    print("Ehliyet alamazsiniz!")

<a href="https://github.com/ebrarrkaya/202/blob/65c7e1781650893acc67ef7c5e75921f4efbc245/eee.png">ÇIKTI 1</a>

<a href="https://github.com/ebrarrkaya/202/blob/60c3b007a744658fa7a3e0155e8ec51814e2adb6/AAAAA.png">ÇIKTI 2</a>

Örnek Kod 2: 

kartno=123456

cvv=110

skt="10/28"

kartnos=int(input("Kart Numarasi Giriniz: "))

cvvs=int(input("Cvv Giriniz: "))

skts=input("Son Kullanma Tarihini Giriniz(aa/yy): ")

if kartnos==kartno and cvvs==cvv and skts==skt:

    print("Sisteme hosgeldiniz!")
else:

    print("Sisteme giris yapilamiyor")

<a href="https://github.com/ebrarrkaya/202/blob/2d71ce0b63823c0db6fc56713d28be018f9e87cf/gggg.png">ÇIKTI 1</a>

<a href="https://github.com/ebrarrkaya/202/blob/d7eb3ef2caaf486f9cfcf4d7fbbfc038229ecd11/ffff.png">ÇIKTI 2</a>

[KOŞULLU YAPILARA ÖRNEK KODLAR](https://github.com/ebrarrkaya/909/blob/7b8ef1ce8b65ed1afbe19327e6c27b9f46b8ea75/README.md)
