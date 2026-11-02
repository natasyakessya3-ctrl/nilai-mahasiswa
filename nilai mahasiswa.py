jumlah = int(input("Masukkan jumlah mahasiswa: "))

total_nilai = 0

for i in range(1, jumlah + 1):
    nilai = float(input(f"Masukkan nilai mahasiswa {i}: "))
    total_nilai += nilai

rata_rata = total_nilai / jumlah

print("\n===== HASIL PENILAIAN =====")
print("Jumlah mahasiswa:", jumlah)
print("Nilai rata-rata:", rata_rata)
