import os


print("=" * 50)
print("AMALIY 3: Joriy papkani aniqlash")
print("=" * 50)

joriy_papka = os.getcwd()
print("Joriy papka:", joriy_papka)

print("\nIchidagi elementlar:")
for element in os.listdir(joriy_papka):
    print(element)



print("\n" + "=" * 50)
print("AMALIY 4: Papka yaratish")
print("=" * 50)

papka_nomi = input("Papka nomini kiriting: ")

if os.path.exists(papka_nomi):
    print("Bu papka allaqachon mavjud.")
else:
    os.mkdir(papka_nomi)
    print(f"'{papka_nomi}' papkasi yaratildi.")



print("\n" + "=" * 50)
print("AMALIY 5: Fayl mavjudligini tekshirish")
print("=" * 50)

fayl_nomi = input("Fayl nomini kiriting: ")

if os.path.exists(fayl_nomi) and os.path.isfile(fayl_nomi):
    print(f"{fayl_nomi} mavjud.")
else:
    print(f"{fayl_nomi} mavjud emas.")



print("\n" + "=" * 50)
print("AMALIY 6: Fayl hajmini aniqlash")
print("=" * 50)

if os.path.exists("data.txt"):
    hajm = os.path.getsize("data.txt")
    print(f"Fayl hajmi: {hajm} bytes")
else:
    print("data.txt topilmadi, avval uni yarating.")



print("\n" + "=" * 50)
print("AMALIY 7: Fayl yoki papka?")
print("=" * 50)

nom = input("Nom kiriting: ")

if not os.path.exists(nom):
    print("Bunday fayl yoki papka mavjud emas.")
elif os.path.isdir(nom):
    print("Bu papka.")
elif os.path.isfile(nom):
    print("Bu fayl.")
