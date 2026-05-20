class Node:
    def __init__(self, key, nama_barang):
        self.key = key  
        self.nama_barang = nama_barang
        self.left = None
        self.right = None


class TokoBST:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, nama_barang):
        if root is None:
            return Node(key, nama_barang)
        if key < root.key:
            root.left = self.insert_node(root.left, key, nama_barang)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, nama_barang)
        return root

    def insert(self, key, nama_barang):
        self.root = self.insert_node(self.root, key, nama_barang)

    def search_node(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def urut_murah_ke_mahal(self, root):
        if root is None:
            return
        self.urut_murah_ke_mahal(root.left)
        print(f"- {root.nama_barang}: Rp{root.key}")
        self.urut_murah_ke_mahal(root.right)

    def find_min(self, root):
        if root is None:
            return None
        current = root
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, root):
        if root is None:
            return None
        current = root
        while current.right is not None:
            current = current.right
        return current

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def sum_nodes(self, root):
        if root is None:
            return 0
        return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right)


def main():
    toko = TokoBST()
    
    toko.insert(50000, "Kemeja Polos")
    toko.insert(25000, "Kaos Kaki")
    toko.insert(120000, "Jaket Denim")
    toko.insert(15000, "Gantungan Kunci")
    toko.insert(75000, "Celana Pendek")

    pilih = 0
    while pilih != 7:
        print("\n=== SISTEM MANAJEMEN TOKO (BST) ===")
        print("1. Tambah Barang Baru")
        print("2. Cari Barang Berdasarkan Harga exact")
        print("3. Tampilkan Katalog (Termurah -> Termahal)")
        print("4. Cek Produk Termurah & Termahal")
        print("5. Hitung Total Variasi Produk")
        print("6. Hitung Total Nilai Aset Seluruh Barang")
        print("7. Keluar")
        
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue
            
        if pilih == 1:
            try:
                harga = int(input("Masukkan harga barang: Rp"))
                nama = input("Masukkan nama barang: ")
                toko.insert(harga, nama)
                print(f"{nama} berhasil ditambahkan!")
            except ValueError:
                print("Harga harus berupa angka!")
        elif pilih == 2:
            try:
                harga_cari = int(input("Cari barang dengan harga: Rp"))
                hasil = toko.search(harga_cari)
                if hasil:
                    print(f"Ditemukan: {hasil.nama_barang} seharga Rp{hasil.key}")
                else:
                    print("Tidak ada barang dengan harga tersebut.")
            except ValueError:
                print("Input harus angka!")
        elif pilih == 3:
            print("\n--- KATALOG PRODUK ---")
            toko.urut_murah_ke_mahal(toko.root)
        elif pilih == 4:
            min_node = toko.find_min(toko.root)
            max_node = toko.find_max(toko.root)
            if min_node and max_node:
                print(f"Termurah: {min_node.nama_barang} (Rp{min_node.key})")
                print(f"Termahal: {max_node.nama_barang} (Rp{max_node.key})")
        elif pilih == 5:
            print(f"Total variasi produk di toko: {toko.count_nodes(toko.root)} jenis")
        elif pilih == 6:
            print(f"Total nilai gabungan aset produk: Rp{toko.sum_nodes(toko.root)}")
        elif pilih == 7:
            print("Program selesai.")


if __name__ == "__main__":
    main()