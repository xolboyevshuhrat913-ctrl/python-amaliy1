import os

while True:
    print("\n===== FILE MANAGER =====")
    print("1. Papkadagi fayllarni ko'rish")
    print("2. Yangi papka yaratish")
    print("3. Yangi fayl yaratish")
    print("4. Faylni o'qish")
    print("5. Faylga yozish")
    print("6. Faylni o'chirish")
    print("7. Papkani o'chirish")
    print("8. Fayl hajmini ko'rish")
    print("9. Chiqish")

    tanlov = input("\nTanlang: ")

    if tanlov == "1":
        elementlar = os.listdir()
        if elementlar:
            for element in elementlar:
                print(element)
        else:
            print("Papka bo'sh.")

    elif tanlov == "2":
        papka_nomi = input("Papka nomi: ")
        if os.path.exists(papka_nomi):
            print("Bu papka allaqachon mavjud.")
        else:
            os.mkdir(papka_nomi)
            print("Papka yaratildi.")

    elif tanlov == "3":
        fayl_nomi = input("Fayl nomi: ")
        if os.path.exists(fayl_nomi):
            print("Bu fayl allaqachon mavjud.")
        else:
            with open(fayl_nomi, "w") as f:
                pass   # bo'sh fayl yaratish
            print("Fayl yaratildi.")

    elif tanlov == "4":
        fayl_nomi = input("Fayl nomi: ")
        if os.path.exists(fayl_nomi) and os.path.isfile(fayl_nomi):
            with open(fayl_nomi, "r") as f:
                mazmun = f.read()
            print("\nFayl mazmuni:")
            print(mazmun)
        else:
            print("Bunday fayl topilmadi.")

    elif tanlov == "5":
        fayl_nomi = input("Fayl nomi: ")
        matn = input("Yozmoqchi bo'lgan matningizni kiriting: ")
        with open(fayl_nomi, "a") as f:
            f.write(matn + "\n")
        print("Faylga yozildi.")

    elif tanlov == "6":
        fayl_nomi = input("O'chirmoqchi bo'lgan fayl nomi: ")
        if os.path.exists(fayl_nomi) and os.path.isfile(fayl_nomi):
            os.remove(fayl_nomi)
            print("Fayl o'chirildi.")
        else:
            print("Bunday fayl topilmadi.")

    elif tanlov == "7":
        papka_nomi = input("O'chirmoqchi bo'lgan papka nomi: ")
        if os.path.exists(papka_nomi) and os.path.isdir(papka_nomi):
            os.rmdir(papka_nomi)   # eslatma: faqat BO'SH papkani o'chiradi
            print("Papka o'chirildi.")
        else:
            print("Bunday papka topilmadi (yoki bo'sh emas).")

    elif tanlov == "8":
        fayl_nomi = input("Fayl nomi: ")
        if os.path.exists(fayl_nomi) and os.path.isfile(fayl_nomi):
            hajm = os.path.getsize(fayl_nomi)
            print(f"Fayl hajmi: {hajm} bytes")
        else:
            print("Bunday fayl topilmadi.")

    elif tanlov == "9":
        print("Dasturdan chiqildi. Xayr!")
        break

    else:
        print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")
