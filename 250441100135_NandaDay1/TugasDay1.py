print("\n")
print("=== Masukkan Nilai Terlebih Dahulu ===")
nilai_tugas = float(input("Masukkan Nilai Tugas : "))
nilai_uts = float(input("Masukkan Nilai UTS : "))
nilai_uas = float(input("Masukkan Nilai UAS : "))

bobot_tugas = 30
bobot_uts = 30
bobot_uas = 40

akhir_tugas = nilai_tugas * (bobot_tugas /100) 
akhir_uts = nilai_uts * (bobot_uts /100) 
akhir_uas = nilai_uas * (bobot_uas /100) 

nilai_akhir = akhir_tugas + akhir_uts + akhir_uas

print("\n======= Nilai yang Diperoleh =======")
print("Nilai Tugas :", nilai_tugas)
print("Nilai UTS   :", nilai_uts)
print("Nilai UAS   :", nilai_uas)

print("\n=========== Nilai Akhir ===========")
print(f"Nilai akhir dari Tugas ({bobot_tugas}%) : {akhir_tugas}")
print(f"Nilai akhir dari UTS   ({bobot_uts}%) : {akhir_uts}")
print(f"Nilai akhir dari UAS   ({bobot_uas}%) : {akhir_uas}")
print("\n-----------------------------------")
print("Total Nilai Akhir :", nilai_akhir)
print("\n")