# HEADER (JUDUL PROGRAM)
print("\n PIZZA HUT \n")
SALAMPEMBUKA = "Selamat Datang di Pizza HUT"
print("\n", SALAMPEMBUKA)
print("_" * 90, "\n")

# DAFTAR MENU
print("Toping Yang Kami Miliki: frankfuter, meatmonsta, cheeselovers")
print("Cruzt Yang Kami Miliki: cheesybites, panpizza, sosis")
print("Size Yang Kami Miliki: small, medium, large", "\n")

# INPUT TOPING
PilihToping = str(input("Masukkan Pilihan Toping: "))

if PilihToping == "frankfuter":
    print("30.000")
    HargaToping = int(30000)
elif PilihToping == "meatmonsta":
    print("25.000")
    HargaToping = int(25000)
elif PilihToping == "cheeselovers":
    print("20.000")
    HargaToping = int(20000)
else:
    print("Toping yang anda pilih tidak tersedia")
    HargaToping = 0

# INPUT CRUZT
PilihCruzt = str(input("Masukkan Pilihan Cruzt: "))
if PilihCruzt == "cheesybites":
    print("50.000")
    HargaCruzt = int(50000)
elif PilihCruzt == "sosis":
    print("30.000")
    HargaCruzt = int(30000)
elif PilihCruzt == "panpizza":
    print("25.000")
    HargaCruzt = int(25000)
else:
    print("Cruzt yang anda pilih tidak tersedia")
    HargaCruzt = 0

# INPUT SIZE
PilihSize = str(input("Masukkan Pilihan Size: "))
if PilihSize == "large":
    print("50.000")
    HargaSize = int(50000)
elif PilihSize == "medium":
    print("25.000")
    HargaSize = int(25000)
elif PilihSize == "small":
    print("20.000")
    HargaSize = int(20000)
else:
    print("Size yang anda pilih tidak tersedia")
    HargaSize = 0

# INPUT TAMBAHAN KEJU
TambahanKeju = str(input("Mau pakai keju? (yes/no) "))
if TambahanKeju == "yes":
    print("+Keju")
    HargaTambahan = int(13000)
else:
    HargaTambahan = int(0)

# TOTAL HARGA
print("_" * 90, "\n")
print("Thank you for choosing Pizza Hut Deliveries!")
HargaTotalPesananAnda = int(HargaToping + HargaCruzt + HargaSize + HargaTambahan)
print("Your Final bill is Rp."+ str(HargaTotalPesananAnda))


