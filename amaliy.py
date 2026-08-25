
print("=" * 50)
print("AMALIY 8: Faylga yozish")
print("=" * 50)

talabalar = ["Ali\n", "Vali\n", "Sardor\n", "Madina\n", "Aziza\n"]

with open("students.txt", "w") as file:
    file.writelines(talabalar)

print("students.txt fayliga yozildi.")



print("\n" + "=" * 50)
print("AMALIY 9: Fayldan o'qish")
print("=" * 50)

with open("students.txt", "r") as file:
    data = file.read()

print("Talabalar:\n")
print(data)




print("=" * 50)
print("AMALIY 10: Faylga yangi ma'lumot qo'shish")
print("=" * 50)


with open("students.txt", "w") as file:
    file.writelines(["Ali\n", "Vali\n", "Sardor\n"])

yangi_student = input("Yangi student: ")

with open("students.txt", "a") as file:   
    file.write(yangi_student + "\n")

print("\nYangilangan fayl:")
with open("students.txt", "r") as file:
    print(file.read())



print("=" * 50)
print("AMALIY 11: Studentlarni fayldan o'qish")
print("=" * 50)


with open("students.txt", "w") as file:
    file.writelines([
        "Ali Valiyev\n",
        "Madina Karimova\n",
        "Bekzod Toshmatov\n",
        "Aziza Qodirova\n",
        "Jasur Abdullayev\n"
    ])

with open("students.txt", "r") as file:
    qatorlar = file.readlines()


qatorlar = [qator.strip() for qator in qatorlar]

names = []
surnames = []

for qator in qatorlar:
    ism, familiya = qator.split()
    names.append(ism)
    surnames.append(familiya)

print("Names:")
print(names)

print("\nSurnames:")
print(surnames)

a_bilan_boshlanadigan = [ism for ism in names if ism.startswith("A")]
print("\n'A' bilan boshlanadigan ismlar:")
print(a_bilan_boshlanadigan)
