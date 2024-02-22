import random
sayi = random.randint(1, 100)

oyuncu_adi = input("Merhaba, adın ne? ")
tahmin_sayisi = 0
print('Tanıştığımıza memnun oldum {}! \nHadi birlikte bir oyun oynayalım, ben aklımdan 1 ile 100 arasında bir sayı tutacağım, sen de tahmin etmeye çalışacaksın, anlaştık mı? \nAyrıca unutma, tahmin etmek için yalnızca 10 hakkın var!:'.format(oyuncu_adi))

while tahmin_sayisi < 10:
    tahmin = int(input())
    tahmin_sayisi += 1
    if tahmin < sayi:
        print('Tahminin çok düşük, biraz yükseltebilirsin!')
    if tahmin > sayi:
        print('Tahminin çok yüksek, biraz düşürebilirsin!')
    if tahmin == sayi:
        break
if tahmin == sayi:
    print( 'Başarılar {}, sayıyı toplam {} denemede tahmin ettin!'.format(oyuncu_adi, tahmin_sayisi))
else:
    print('Sayıyı tahmin edemedin. \nSayı {} idi.'.format(sayi))