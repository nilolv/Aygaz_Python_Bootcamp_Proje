import random

def tas_kagit_makas_NİHAL_ZEREN_KURUOGLU():

    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Kurallar: Taş makası yener, Kağıt taşı yener, Makas kağıdı yener.")
    print("Oyundan çıkmak için 'q' tuşuna basın.")

    secenekler = ["taş", "kağıt", "makas"]
    oyun_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0

    while True:

        oyun_sayisi += 1
        tur_sayisi = 0
        oyuncu_tur_galibiyetleri = 0
        bilgisayar_tur_galibiyetleri = 0

        while oyuncu_tur_galibiyetleri < 2 and bilgisayar_tur_galibiyetleri < 2:
            print("\nTur:", tur_sayisi + 1)
            oyuncu_secimi = input("Taş mı, Kağıt mı, Makas mı? (Çıkmak istiyorsan 'q'): ").lower()
            if oyuncu_secimi == 'q':
                print("Oyundan çıkılıyor...")
                return

            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçim! Lütfen tekrar deneyin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_tur_galibiyetleri += 1
            else:
                print("Bu turu kaybettiniz!")
                bilgisayar_tur_galibiyetleri += 1

            tur_sayisi += 1

        if oyuncu_tur_galibiyetleri == 2:
            print("\nTebrikler! Oyunu kazandınız!")
            oyuncu_galibiyetleri += 1
        else:
            print("\nMaalesef, oyunu kaybettiniz.")
            bilgisayar_galibiyetleri += 1

        devam = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        if devam != 'evet':
            break

    print("\nOyun Bitti!")
    print(f"Toplam Oyun Sayısı: {oyun_sayisi}")
    print(f"Toplam Oyuncu Galibiyeti: {oyuncu_galibiyetleri}")
    print(f"Toplam Bilgisayar Galibiyeti: {bilgisayar_galibiyetleri}")


tas_kagit_makas_NİHAL_ZEREN_KURUOGLU()
