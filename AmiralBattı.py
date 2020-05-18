import random
import os

def OyunAlaniOlustur(boyut = 10, doldurulacakDeger = '?'):
    # Bu fonksiyon verilen boyutta bir liste şeklinde oyun alanı oluşturur.
    # Oyun alanının her bir hücresine parametre olarak verilen doldurulacak değeri yazar.
    # Girilmeyen parametreler için boyut = 10 ve doldurulacak değer = ? 
    # varsayılan değerlerdir.
    oyunAlani = [[doldurulacakDeger for x in range(boyut)] for y in range(boyut)] 
    return oyunAlani;

def GemiOlustur(bas, yon, uzunluk ):
    # Bu fonksiyon [x,y] olarak verilen başlangıç koordinatlarını kullanarak
    # verilen yön ve uzunluktaki geminin koordinatlarını hesaplar ve geminin
    # işgal ettiği bütün koordinatları döner.
    # Yön = 0 -> gemi yatay, Yön = 1 -> gemi dikey
    if yon == 0:
        return [[bas[0]+x, bas[1]] for x in range(uzunluk)]
    else:
        return [[bas[0], bas[1] + x] for x in range(uzunluk)]
    
def FiloOlustur(oyunAlani):
    # Bu fonksiyon 1,2,3 ve 4 birim uzunluktaki gemileri oyun alanı
    # üzerine yerleştirir. Gemi yerleri ve yönleri rastgeledir.
    # Gemiler birbirleri ile çakışmayacak şekilde yerleştirilir
    
    boyut = len(oyunAlani)

    # 4 birim uzunluklu gemiyi rastgele başlangıç noktası ve yön ile oluştur
    gemi4 = GemiOlustur([random.randrange(boyut-3), random.randrange(boyut-3)], random.randint(0, 1), 4)
    
    # 3 birim uzunluklu gemiyi daha önce oluşturulmuş gemilerle 
    # çakışmayana kadar deneyerek rastgele başlangıç noktası ve yön ile oluştur.
    while True:
        gemi3 = GemiOlustur([random.randrange(boyut-2), random.randrange(boyut-2)], random.randint(0, 1), 3)
        if not any(gemiKoordinati in gemi3 for gemiKoordinati in gemi4):
            break
    while True:
       gemi2 = GemiOlustur([random.randrange(boyut-1), random.randrange(boyut-1)], random.randint(0, 1), 2)
       if not any(gemiKoordinati in gemi2 for gemiKoordinati in gemi4) and not any(gemiKoordinati in gemi2 for gemiKoordinati in gemi3):
           break       
    while True:
       gemi1 = GemiOlustur([random.randrange(boyut), random.randrange(boyut)], random.randint(0, 1), 1)
       if not any(gemiKoordinati in gemi1 for gemiKoordinati in gemi4) and not any(gemiKoordinati in gemi1 for gemiKoordinati in gemi3) and not any(gemiKoordinati in gemi1 for gemiKoordinati in gemi2):
           break        
    
    return gemi1, gemi2, gemi3, gemi4

def GemileriYerlestir(oyunAlani, gemi1, gemi2, gemi3, gemi4):
    # Bu fonksiyon oyun alanı içerisine gemileri yerleştirir
    for gemi in [gemi1, gemi2, gemi3, gemi4]:
        for koordinat in gemi:
            oyunAlani[koordinat[1]][koordinat[0]] = 'G'
    
def OyunAlaniniYaz(oyunAlani, mod):
    # Bu fonksiyon oyun alanını ekrana yazar. 
    # Açık veya gizli mod tercihine göre gemiler gösterilir veya gösterilmez.
    boyut = len(oyunAlani)
    for satir in reversed(range(0,boyut)):
        for sutun in range(0,boyut):
            if mod == 0:
                if oyunAlani[satir][sutun] == 'G':
                    print('{:3}'.format('?'), end="")
                else:
                    print('{:3}'.format(oyunAlani[satir][sutun]), end="")
            else:
                print('{:3}'.format(oyunAlani[satir][sutun]), end="")
        print()

def AtisYap(oyunAlani, x, y):
    # Bu fonksiyon oyun alanındaki koordinatları verilen bir noktaya atış yapar.
    # Atış yapılan noktaya göre geri dönüş yapar.
    # 3 durum incelenir: 
    # - Daha önce atış yapılmış bir nokta vurulmaya çalışılmıştır
    # - Bir gemi vurulmuştur
    # - Atış isabet ettirilememiştir

    if oyunAlani[y][x] == '*' or oyunAlani[y][x] == 'X':
        print("\nBurayı daha önce vurdunuz!")
    elif oyunAlani[y][x] == 'G':
        print("\nTebrikler bir gemi vurdunuz!")
        oyunAlani[y][x] = 'X'
    else:
        print("\nMaalesef isabet edemediniz!")
        oyunAlani[y][x] = '*'
    
    
def oyun():
    # Bu fonksiyon 1 tur Amiral Battı oyununu oynatır.
    os.system('cls')    # Konsolu temizle
    print("Amiral battı oyununa hoşgeldiniz!\n")
    print("Kare matris olan oyun alanının boyutunu en az 10 olacak şekilde tamsayı olarak giriniz.")
    
    # Kullanıcıdan oyun alanı boyutunu al
    while True:
        try:
            boyut = int(input("Boyut: "))
            if boyut < 10:
                print("\nOyun alanının boyutları 10x10 veya daha büyük olacak şekilde değer girin!")
            else:
                break
        except ValueError:
            print("\nSadece tamsayi girin!")

    # Kullanıcıdan oyun modunu al
    print("\nGemilerin gösterileceği Açık Mod için 1, Gizli Mod için 0 giriniz.")
    while True:
        try:
            mod = int(input("Mod: "))
            if not(mod == 0 or mod == 1):
                print("\nSadece 0 ve 1 değerleri ile seçim yapın!")
            else:
                break
        except ValueError:
            print("\nSadece 0 ve 1 değerleri ile seçim yapın!")
            
    # Oyun alanını ve gemileri hazırla
    oyunAlani = OyunAlaniOlustur(boyut,'?')
    gemi1, gemi2, gemi3, gemi4 = FiloOlustur(oyunAlani)
    filo = [gemi1,gemi2,gemi3,gemi4];
    GemileriYerlestir(oyunAlani, gemi1, gemi2, gemi3, gemi4)
    mermi = round(boyut*boyut/3)
    os.system('cls')    # Konsolu temizle
    OyunAlaniniYaz(oyunAlani,mod)  
    print("\nOyun alanının sol alt köşesi (1,1) noktasıdır.")
    
    # Kullanıcıdan atış koordinatlarını al ve oyun bitene kadar atış yap
    while True:
        print("\nAtışın yapılacağı (x,y) koordinatlarını giriniz.")
        while True:
            try:
                x = int(input("x: "))
                y = int(input("y: "))
                if x > boyut or y > boyut or x < 1 or y < 1:
                    print("\nOyun alanı içerisinde olacak şekilde değerler giriniz!")
                else:
                    break
            except ValueError:
                print("\nSadece tamsayi girin!")
        os.system('cls')    # Konsolu temizle
        AtisYap(oyunAlani, x-1, y-1)
        
        # Gemilerin batıp batmadığını kontrol et
        for gemi in filo:
            try: 
                gemi.remove([x-1,y-1])
            except:
                pass
            if len(gemi) == 0:
                filo.remove(gemi)
                print("Tebrikler bir gemiyi batırdınız!")

        # Mermiyi azalt
        mermi -= 1
        print(f"\nKalan mermi: {mermi}")
        
        # Oyun alanını ekrana yaz
        print("\n")
        OyunAlaniniYaz(oyunAlani,mod)
        
        # Oyunun bitip bitmediğini kontrol et      
        if not any('G' in koordinat for koordinat in oyunAlani):
            print("\nBütün gemiler vuruldu!")
            print(f"\nTebrikler {mermi} puan ile oyunu kazandınız!")
            return
        
        # Mermilerin bitip bitmediğini kontrol et
        if mermi <= 0:
            print("\nMermileriniz bitti. Kaybettiniz!")
            return
        

if __name__ == "__main__":
    # Kullanıcı devam etmek istemeyene kadar oyunu oynat
    while True:
        oyun()
        tekrar = input("Tekrar oynamak ister misiniz? ( Evet için E/e, Hayır H/h ): ")
        if not(tekrar == 'e' or tekrar == 'E'):
            print("\nÇıkış yapılıyor..!")
            break
