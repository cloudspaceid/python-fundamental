"""
File demo print text with Python!
Semua sintaksis dasar bahasa peprograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
#Skuensial
print("*** Skuensial ***")
print("Start")
print("Proses")
print("Finish")

#Percabangan
print("*** Percabangan ***")
engine = 1
hand_break = 0
if engine > 0:
    print("Engine start")
    if hand_break == 1:
        print("Car stop")
    else:
        print("Car run")

else:
    print("Engine stop")
