mahasiswa_list = []   
dosen_list = []       


def input_nim():
    while True:
        nim = input("Masukkan NIM (maks 12 digit): ")
        if nim.isdigit() and len(nim) <= 12:
            return nim
        print("NIM hanya boleh angka dan maksimal 12 digit!")


def input_nip():
    while True:
        nip = input("Masukkan NIP (maks 18 digit): ")
        if nip.isdigit() and len(nip) <= 18:
            return nip
        print("NIP hanya boleh angka dan maksimal 18 digit!")


def tambah_mahasiswa():
    print("\n=== Tambah Mahasiswa ===")
    nama = input("Masukkan nama mahasiswa: ")
    nim = input_nim()
    status = input("Masukkan status mahasiswa (Aktif / Cuti / Lulus): ")

    daftar_fakultas = ["FT", "FEB"]

    print("\nPilih Fakultas:")
    for i, f in enumerate(daftar_fakultas, start=1):
        print(f"{i}. {f}")

    while True:
        pilih_fak = input("Masukkan nomor fakultas (1-2): ")
        if pilih_fak in ["1", "2"]:
            fakultas = daftar_fakultas[int(pilih_fak) - 1]
            break
        print("Pilihan tidak valid!")

    if fakultas == "FT":
        daftar_prodi = ["Informatika", "Sistem Informasi", "Industri", "Mesin"]
    else:
        daftar_prodi = ["Akuntansi", "Manajemen", "Ekonomi Pembangunan", "Ekonomi Syariah"]

    print("\nPilih Prodi:")
    for i, p in enumerate(daftar_prodi, start=1):
        print(f"{i}. {p}")

    while True:
        pilih_prodi = input("Masukkan nomor prodi (1-4): ")
        if pilih_prodi in ["1", "2", "3", "4"]:
            prodi = daftar_prodi[int(pilih_prodi) - 1]
            break
        print("Pilihan tidak valid!")

    semester_tuple = ("1", "2", "3", "4", "5", "6", "7", "8")
    print("\nDaftar Semester:", semester_tuple)
    semester = input("Masukkan semester: ")

    krs = input("Masukkan jumlah mata kuliah di KRS: ")
    nilai = input("Masukkan nilai IPK / semester: ")

    mahasiswa_list.append({
        "nama": nama,
        "nim": nim,
        "status": status,
        "fakultas": fakultas,
        "prodi": prodi,
        "semester": semester,
        "krs": krs,
        "nilai": nilai
    })

    print("\nMahasiswa berhasil ditambahkan!\n")


def tampilkan_mahasiswa():
    print("\n=== Data Mahasiswa ===")
    if not mahasiswa_list:
        print("Belum ada data mahasiswa.\n")
        return
    
    for i, m in enumerate(mahasiswa_list, start=1):
        print(f"{i}. Nama: {m['nama']}, NIM: {m['nim']}, Status: {m['status']}")
        print(f"   Fakultas: {m['fakultas']}, Prodi: {m['prodi']}, Semester: {m['semester']}")
        print(f"   KRS: {m['krs']} matkul, Nilai: {m['nilai']}")
    print()


def update_mahasiswa():
    tampilkan_mahasiswa()
    if not mahasiswa_list:
        return

    pilih = input("Masukkan nomor mahasiswa yang akan di-update: ")
    if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(mahasiswa_list):
        print("Nomor tidak valid!")
        return
    
    index = int(pilih) - 1
    m = mahasiswa_list[index]

    print("\n=== Pilih Data yang Ingin Diupdate ===")
    print("1. Nama")
    print("2. NIM")
    print("3. Status")
    print("4. Fakultas")
    print("5. Prodi")
    print("6. Semester")
    print("7. Jumlah KRS")
    print("8. Nilai")
    print("9. Batal")

    pilihan = input("Pilih menu update: ")

    if pilihan == "1":
        m["nama"] = input("Masukkan Nama baru: ") or m["nama"]
    elif pilihan == "2":
        m["nim"] = input_nim()
    elif pilihan == "3":
        m["status"] = input("Status baru: ") or m["status"]
    elif pilihan == "4":
        m["fakultas"] = input("Masukkan Fakultas baru: ") or m["fakultas"]
    elif pilihan == "5":
        m["prodi"] = input("Masukkan Prodi baru: ") or m["prodi"]
    elif pilihan == "6":
        m["semester"] = input("Semester baru: ") or m["semester"]
    elif pilihan == "7":
        m["krs"] = input("Jumlah KRS baru: ") or m["krs"]
    elif pilihan == "8":
        m["nilai"] = input("Nilai baru: ") or m["nilai"]
    elif pilihan == "9":
        print("Update dibatalkan.\n")
        return
    else:
        print("Pilihan tidak valid!")
        return

    print("Data mahasiswa berhasil diperbarui!\n")


def delete_mahasiswa():
    tampilkan_mahasiswa()
    if not mahasiswa_list:
        return

    pilih = input("Masukkan nomor mahasiswa yang akan dihapus: ")

    if pilih.isdigit() and 1 <= int(pilih) <= len(mahasiswa_list):
        del mahasiswa_list[int(pilih) - 1]
        print("Data mahasiswa berhasil dihapus!\n")
    else:
        print("Nomor tidak valid!\n")


def tambah_dosen():
    print("\n=== Tambah Dosen ===")
    nama = input("Masukkan nama dosen: ")
    nip = input_nip()
    matkul = input("Masukkan mata kuliah :")

    matkul_set = set(matkul.split(","))
    matkul_bersih = ", ".join(matkul_set)

    dosen_list.append({
        "nama": nama,
        "nip": nip,
        "mata_kuliah": matkul_bersih
    })

    print("Dosen berhasil ditambahkan!\n")

def tampilkan_dosen():
    print("\n=== Data Dosen ===")
    if not dosen_list:
        print("Belum ada data dosen.\n")
        return

    for i, d in enumerate(dosen_list, start=1):
        print(f"{i}. Nama: {d['nama']}, NIP: {d['nip']}, Mata Kuliah: {d['mata_kuliah']}")
    print()

def update_dosen():
    tampilkan_dosen()
    if not dosen_list:
        return

    pilih = input("Masukkan nomor dosen yang akan di-update: ")
    if not pilih.isdigit() or int(pilih) < 1 or int(pilih) > len(dosen_list):
        print("Nomor tidak valid!")
        return

    index = int(pilih) - 1
    d = dosen_list[index]

    print("\n=== Pilih Data yang Ingin Diupdate ===")
    print("1. Nama")
    print("2. NIP")
    print("3. Mata Kuliah")
    print("4. Batal")

    pilihan = input("Pilih menu update: ")

    if pilihan == "1":
        d["nama"] = input("Nama baru: ") or d["nama"]
    elif pilihan == "2":
        d["nip"] = input_nip()
    elif pilihan == "3":
        baru = input("Masukkan mata kuliah yang baru : ")
        matkul_set = set(baru.split(","))
        d["mata_kuliah"] = ", ".join(matkul_set)
    elif pilihan == "4":
        print("Update dibatalkan.\n")
        return
    else:
        print("Pilihan tidak valid!")
        return

    print("Data dosen berhasil diperbarui!\n")

def delete_dosen():
    tampilkan_dosen()
    if not dosen_list:
        return

    pilih = input("Masukkan nomor dosen yang akan dihapus: ")

    if pilih.isdigit() and 1 <= int(pilih) <= len(dosen_list):
        del dosen_list[int(pilih) - 1]
        print("Data dosen berhasil dihapus!\n")
    else:
        print("Nomor tidak valid!\n")

def search_mahasiswa():
    print("\n=== Cari Mahasiswa ===")
    keyword = input("Masukkan Nama atau NIM: ").lower()

    found = False
    for m in mahasiswa_list:
        if keyword in m["nama"].lower() or keyword in m["nim"].lower():
            print("\nDitemukan:")
            print(f"Nama     : {m['nama']}")
            print(f"NIM      : {m['nim']}")
            print(f"Status   : {m['status']}")
            print(f"Fakultas : {m['fakultas']}")
            print(f"Prodi    : {m['prodi']}")
            print(f"Semester : {m['semester']}")
            print(f"KRS      : {m['krs']}")
            print(f"Nilai    : {m['nilai']}")
            found = True

    if not found:
        print("Mahasiswa tidak ditemukan.\n")


def search_dosen():
    print("\n=== Cari Dosen ===")
    keyword = input("Masukkan Nama atau NIP: ").lower()

    found = False
    for d in dosen_list:
        if keyword in d["nama"].lower() or keyword in d["nip"].lower():
            print("\nDitemukan:")
            print(f"Nama        : {d['nama']}")
            print(f"NIP         : {d['nip']}")
            print(f"Mata Kuliah : {d['mata_kuliah']}")
            found = True

    if not found:
        print("Dosen tidak ditemukan.\n")

def statistik():
    print("\n=== STATISTIK DATA ===")
    
    print("Total Mahasiswa :", len(mahasiswa_list))
    print("Total Dosen     :", len(dosen_list))
    print("----------------------------------")
    
    status_count = {"Aktif": 0, "Cuti": 0, "Lulus": 0}
    for m in mahasiswa_list:
        if m["status"] in status_count:
            status_count[m["status"]] += 1
    
    print("Status Mahasiswa:")
    for s, jml in status_count.items():
        print(f"  {s} : {jml}")
    print("----------------------------------")

    fakultas_count = {}
    for m in mahasiswa_list:
        fak = m["fakultas"]
        fakultas_count[fak] = fakultas_count.get(fak, 0) + 1
    
    print("Fakultas:")
    for f, jml in fakultas_count.items():
        print(f"  {f} : {jml}")
    print("----------------------------------")
    
    prodi_count = {}
    for m in mahasiswa_list:
        p = m["prodi"]
        prodi_count[p] = prodi_count.get(p, 0) + 1
    
    print("Program Studi:")
    for p, jml in prodi_count.items():
        print(f"  {p} : {jml}")
    
    print()

def menu():
    while True:
        print("===== MENU =====")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Update Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Tambah Dosen")
        print("6. Tampilkan Dosen")
        print("7. Update Dosen")
        print("8. Hapus Dosen")
        print("9. Cari Mahasiswa")
        print("10. Cari Dosen")
        print("11. Statistik")
        print("12. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1": tambah_mahasiswa()
        elif pilihan == "2": tampilkan_mahasiswa()
        elif pilihan == "3": update_mahasiswa()
        elif pilihan == "4": delete_mahasiswa()
        elif pilihan == "5": tambah_dosen()
        elif pilihan == "6": tampilkan_dosen()
        elif pilihan == "7": update_dosen()
        elif pilihan == "8": delete_dosen()
        elif pilihan == "9": search_mahasiswa()
        elif pilihan == "10": search_dosen()
        elif pilihan == "11": statistik()
        elif pilihan == "12":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")


menu()