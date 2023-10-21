print ("\n   SILAHKAN INPUT DATA ANDA \n=============================\n")
Nama = input("Masukan Nama Anda       :")
NIM = input("Masukan NIM Anda        :")
UAS =float(input ("Masukan nilai Uas Anda  :"))
UTS = float(input ("Masukan Nilai UTS Anda  :"))
TGS = float(input ("Masukan Nilai Tugas Anda:"))
ABS = float(input ("Masukan Jumlah Kehadiran:"))

nUAS = UAS * 0.4
nUTS = UTS * 0.3
nTGS = TGS * 0.2
nABS = ABS * 0.1

na = nUAS+nUTS+nTGS+nABS

print ("\n NILAI AKHIR MAHASISWA RAHARJA \n=============================\n")
print ("NAMA : %s"%Nama)
print ("NIM : %s"%NIM)
print ("Nilai : %d"%na)
print ("Grade :")

if na >= 80 :
    print("A")

elif na >= 60 :
    print("B")

elif na >= 40 :
    print("C")

elif na >= 20 :
    print("D")

elif na <= 19 :
    print("E")

