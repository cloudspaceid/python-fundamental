"""
Looping dengan while
"""

jumlah_buku = 20
print ('Baca semua buku!')

buku_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {buku_dibaca}')

while buku_dibaca < jumlah_buku:
    buku_dibaca += 1
    print(f'Baca buku ke {buku_dibaca}!')

print(f'Buku yang sudah dibaca sebanyak {buku_dibaca}')