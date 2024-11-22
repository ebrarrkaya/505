# SÖZLÜK KAVRAMI
Bilindiği üzere sözlükler, anahtar kelimeler ve o kelimelerin anlamlarından oluş maktadır. Python yazılım dilinde de sözlükler anahtar kelimeler ve onlara denk olan değerlerden oluşmaktadır. Bir sözlük oluşturulurken süslü parantez "{}" kullanılmaktadır. Anahtar kelime ve değer arasına iki nokta üst üste ":" sembolü konulmaktadır. Anahtar kelimeler string tipinde olmalıdır. Değerlerin ise veri kısıtlaması yoktur. İstediğiniz herhangi bir veri olabilir (liste, tam sayı, demet vb.)

Sözlükler için konum değerleri bulunmamaktadır. Yani sözlükte bulunan verilerin bir indeks numarası yoktur.

Örnek Kod:

banka={
"AD":"EBRAR",
"SOYAD":"KAYA",
"BAKİYE":10000,
"USDTRYPARITE":34.5
}

print(banka)

<a href="https://github.com/ebrarrkaya/505/blob/c10b8be6fb2ed2b89f0397d76143b7a18473bea8/a5.png">ÇIKTI İÇİN TIKLAYINIZ</a>

# SÖZLÜĞÜN ANAHTARINA ULAŞMAK
api={"username":"ebrr0ck","password":"12345"}

db={"ebrr0ck","12345"}

print(api["username"]==db[0])

print(api["password"]==db[1])

# SÖZLÜĞÜN DEĞİŞTİRİLMESİ
api["password"]="87654"

print(api)

<a href="https://github.com/ebrarrkaya/505/blob/392a470edeb97c2e3b07681938ca7062c013dde6/z1.png">ÇIKTI İÇİN TIKLAYINIZ</a>
