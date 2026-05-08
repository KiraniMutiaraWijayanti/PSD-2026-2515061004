def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    data = ["Andi", "Budi", "Siti", "Kirani", "Dewi", "Fiki", "Sinta", "Lia"]
    
    n = len(data)
    print("=== LOG KEHADIRAN KARYAWAN HARI INI ===")
    print(f"Daftar Log: {data}")
    
    while True:
        target = input("\nMasukkan NAMA karyawan yang ingin dicari: ")
        if target:
            break
        print("Nama tidak boleh kosong!")

    counter = sequential_search(data, n, target)
    
    print("-" * 40)
    if counter > 0:
        print(f"Karyawan '{target}' ditemukan dalam log sebanyak {counter} kali.")
        print(f"Ini berarti {target} melakukan tapping absen {counter} kali hari ini.")
    else:
        print(f"Nama '{target}' tidak ditemukan. Karyawan ini belum absen.")
    print("-" * 40)


if __name__ == "__main__":
    main()


