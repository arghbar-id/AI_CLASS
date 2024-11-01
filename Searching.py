# Daftar A dan nilai x yang ingin dicari, data = 20 data
A = [2, 2, 1, 3, 10, 6, 7, 8, 9, 4, 2, 1, 5, 7, 4, 8, 7, 2, 10, 4]

# Menampilkan jumlah data dalam Acls
print("Jumlah data dalam A:", len(A))

# Meminta input nilai x dari pengguna
x = int(input("Masukkan nilai x yang ingin dicari: "))

# Mengecek apakah x ganjil atau genap
if x % 2 != 0:  # Jika x adalah angka ganjil
    print("Tidak ada hasil")
else:
    # Menghitung kemunculan x dalam A
    kemunculan = A.count(x)

    # Mendapatkan semua indeks di mana x muncul dalam A
    indeks_kemunculan = [i for i, nilai in enumerate(A) if nilai == x]

    # Menampilkan hasil
    print("Kemunculan x sebanyak:", kemunculan)
    print("Indeks kemunculan x, berada pada indeks ke:", indeks_kemunculan)
