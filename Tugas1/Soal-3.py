teori = float(input("Masukkan nilai teori - "))
praktek = float(input("Masukkan nilai praktek - "))

if teori >= 70 and praktek >= 70:
    print("Selamat, anda lulus!")
elif teori >= 70 and praktek < 70:
    print("Anda harus mengulang ujian praktek")
elif teori < 70 and praktek >= 70:
    print("Anda harus mengulang ujian teori")
elif teori < 70 and praktek < 70:
    print("Anda harus mengulang ujian teori dan praktek")