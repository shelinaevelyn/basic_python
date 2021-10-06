
listnama = []
listtlp = []
i = True
y = range(len(listnama))

while i:
    print("-----------------------")
    print("----Selamat datang!----")
    print("-Menu-")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print("-----------------------")
    menu = input("Pilih menu:")
    if menu=="2":
        nama = input("Masukkan nama-")
        tlp = input("Masukkan No Telepon -")
        listnama.append(nama)
        listtlp.append(tlp)
    elif menu=="1":
        for x in range(len(listnama)): 
            print("Nama:", listnama[x])
            print("No Telepon:", listtlp[x])
    elif menu=="3":
        print("Program selesai, sampai jumpa!")
        i = False
    else:
        print("Menu tidak tersedia")

