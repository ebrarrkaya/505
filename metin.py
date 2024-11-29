cumle="Kucuk, sirin bir kasabada yasayan Ali; doga sevgisiyle dolu, kitap okumayi seven, hayallerinin pesinden kosan cesur, comert, nazik bir insandi."
sesli="aeiou"
sessiz="bcdfghjkKlmnprstvyz"
noktalama=",.;"
seslisayi=0
sessizsayi=0
noktalamasayi=0
for x in cumle:
    if x in sesli:
        seslisayi+=1
    elif x in sessiz:
        sessizsayi+=1
    elif x in noktalama:
        noktalamasayi+=1
print("Metinde {} tane sesli harf vardir.".format(seslisayi))
print("Metinde {} tane sessiz harf vardir.".format(sessizsayi))
print("Metinde {} tane noktalama isareti vardir.".format(noktalamasayi))
