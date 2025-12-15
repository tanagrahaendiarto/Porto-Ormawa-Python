#kakulator python


print("Selamat datang di Kalkulator Sederhana")
print("Program ini bisa membantu kamu menghitung angka dengan mudah.\n")

while True:
    # Menu Pilihan Bilangan 
    print("Silakan pilih operasi yang kamu inginkan:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Modulus (%)")
    print("6. Pangkat (^)")
    print("0. Keluar dari program")

    pilihan = input("Masukkan pilihan kamu (0–6): ")

    # Jika User Ingin Keluar
    if pilihan == "0":
        print("\nTerima kasih sudah menggunakan")
        print("Semoga harimu menyenangkan!")
        break

    # Meminta input 
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))

    # Proses kakulator
    if pilihan == "1":
        hasil = angka1 + angka2
        print(f"Hasil penjumlahan dari {angka1} dan {angka2} adalah {hasil}")

    elif pilihan == "2":
        hasil = angka1 - angka2
        print(f"Hasil pengurangan dari {angka1} dan {angka2} adalah {hasil}")

    elif pilihan == "3":
        hasil = angka1 * angka2
        print(f"Hasil perkalian dari {angka1} dan {angka2} adalah {hasil}")

    elif pilihan == "4":
        if angka2 == 0:
            print("Maaf angka tidak bisa dibagi dengan nol.")
        else:
            hasil = angka1 / angka2
            print(f"Hasil pembagian dari {angka1} dan {angka2} adalah {hasil}")

    elif pilihan == "5":
        if angka2 == 0:
            print("Modulus dengan nol tidak diperbolehkan.")
        else:
            hasil = angka1 % angka2
            print(f"Sisa pembagian dari {angka1} dibagi {angka2} adalah {hasil}")

    elif pilihan == "6":
        hasil = angka1 ** angka2
        print(f"Hasil {angka1} pangkat {angka2} adalah {hasil}")

    else:
        print("Pilihan tidak dikenali. Coba pilih angka 0 sampai 6 ya.")

    print("\n-----------------------------------\n")
