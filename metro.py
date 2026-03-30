# MetroKart Simulyatoru

PIN = "1234"
cehd = 3

# Başlanğıc dəyərlər
balans = 0.0
borc = 0.0
gunluk_limit = 100.0
gunluk_artirilan = 0.0

gedis_sayi = 0
umumi_odenis = 0.0
umumi_endirim = 0.0

emeliyyatlar = []

rejim = "normal"  # normal / telebe / pensiya

# PIN yoxlama
while cehd > 0:
    daxil = input("PIN daxil et: ")
    if daxil == PIN:
        break
    else:
        cehd -= 1
        print("Yanlış PIN!")
        if cehd == 0:
            print("Kart bloklandı.")
            exit()

# Əsas menyu
while True:
    print("\n--- MENU ---")
    print("1) Balansı göstər")
    print("2) Balans artır")
    print("3) Gediş et")
    print("4) Son əməliyyatlar")
    print("5) Günlük statistika")
    print("6) Parametrlər")
    print("0) Çıxış")

    secim = input("Seçim et: ")

    # 1️⃣ Balans
    if secim == "1":
        print(f"Balans: {balans:.2f} AZN | Borc: {borc:.2f}")

    # 2️⃣ Balans artır
    elif secim == "2":
        try:
            mebleg = float(input("Məbləğ daxil et: "))
            if mebleg <= 0:
                print("Yalnız müsbət olmalıdır!")
                continue

            if gunluk_artirilan + mebleg > gunluk_limit:
                print("Günlük limit keçildi!")
                continue

            gunluk_artirilan += mebleg

            # əvvəl borc silinir
            if borc > 0:
                if mebleg >= borc:
                    mebleg -= borc
                    borc = 0
                else:
                    borc -= mebleg
                    mebleg = 0

            balans += mebleg

            emeliyyatlar.append(("Artırma", mebleg, 0, balans))

        except:
            print("Yanlış giriş!")

    # 3️⃣ Gediş
    elif secim == "3":
        gedis_sayi += 1

        # qiymət seçimi
        if rejim == "telebe":
            qiymet = 0.20
            endirim = 0.20
        elif rejim == "pensiya":
            qiymet = 0.15
            endirim = 0.25
        else:
            if gedis_sayi == 1:
                qiymet = 0.40
                endirim = 0
            elif 2 <= gedis_sayi <= 4:
                qiymet = 0.36
                endirim = 0.04
            else:
                qiymet = 0.30
                endirim = 0.10

        # balans yoxlama
        if balans >= qiymet:
            balans -= qiymet
            umumi_odenis += qiymet
            umumi_endirim += endirim
            print("Keçid uğurlu!")

        elif 0.30 <= balans < 0.40:
            sec = input("Təcili keçid edilsin? (bəli/xeyr): ")
            if sec == "bəli":
                balans -= 0.30
                borc += 0.10
                print("Təcili keçid edildi!")
            else:
                print("Keçid ləğv edildi.")
                continue
        else:
            print("Balans kifayət etmir!")
            continue

        emeliyyatlar.append(("Gediş", qiymet, endirim, balans))

    # 4️⃣ Son əməliyyatlar
    elif secim == "4":
        try:
            n = int(input("Neçə əməliyyat göstərilsin: "))
            for e in emeliyyatlar[-n:]:
                print(e)
        except:
            print("Yanlış giriş!")

    # 5️⃣ Statistika
    elif secim == "5":
        print(f"Gediş sayı: {gedis_sayi}")
        print(f"Ümumi ödəniş: {umumi_odenis:.2f}")
        print(f"Endirim: {umumi_endirim:.2f}")
        print(f"Artırılan məbləğ: {gunluk_artirilan:.2f}")

    # 6️⃣ Parametrlər
    elif secim == "6":
        print("1) Limit dəyiş")
        print("2) Rejim dəyiş")
        alt = input("Seçim: ")

        if alt == "1":
            try:
                gunluk_limit = float(input("Yeni limit: "))
            except:
                print("Yanlış!")

        elif alt == "2":
            print("normal / telebe / pensiya")
            rejim = input("Rejim seç: ")

    # 0️⃣ Çıxış
    elif secim == "0":
        print("Proqram dayandırıldı.")
        break

    else:
        print("Yanlış seçim!")
