# Fungsi untuk menghitung nilai fitness
def hitung_fitness(kromosom, barang, ukuran_gudang):
    total_untung = 0
    total_ukuran = 0
    for i in range(len(kromosom)):
        if kromosom[i] == 1:
            total_untung += barang[i][1]
            total_ukuran += barang[i][2]
    if total_ukuran > ukuran_gudang:
            return 0 # Penalti jika melebihi kapasitas
    else:
        return total_untung
    
# # Contoh penggunaan
# # Data barang (nama, keuntungan, ukuran)
# barang = [
#     ("Barang1", 60, 10),
#     ("Barang2", 100, 20),
#     ("Barang3", 120, 30),
#     ("Barang4", 90, 25),
#     ("Barang5", 70, 15)
# ]

# ukuran_gudang = 50 # Kapasitas maksimum tas
    
# # Definisi contoh populasi awal
# populasi_awal = [
#     [1, 0, 1, 0, 1], # Contoh kromosom individu
#     [0, 1, 0, 1, 0],
#     [1, 1, 0, 0, 1],
#     # Tambahkan lebih banyak individu sesuai kebutuhan
# ]

# # Contoh penggunaan
# fitness_populasi = [hitung_fitness(individu, barang, ukuran_gudang) for individu in populasi_awal]

# # Menampilkan nilai fitness
# print("\nNilai Fitness:")
# for idx, fitness in enumerate(fitness_populasi):
#     print(f"Individu {idx+1}: Fitness = {fitness}")