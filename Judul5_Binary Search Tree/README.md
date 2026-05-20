**Sistem Manajemen Stok Toko berbasis BST**

**Deskripsi Singkat**

Program ini adalah aplikasi kasir dan gudang sederhana untuk mengelola stok barang secara fleksibel. Lewat program ini, kamu bisa menambah produk baru, mencari barang lewat harganya, serta menghitung jumlah variasi stok dan total nilai aset toko.
Keunggulan utamanya ada pada efisiensi. Katalog produk otomatis tersusun rapi dari yang termurah sampai termahal tanpa perlu proses urut ulang (sorting) yang bikin lemot. Selain itu, kamu juga bisa langsung tahu produk mana yang paling murah dan paling mahal secara instan.

Aplikasi ini menggunakan struktur data Binary Search Tree (BST) atau Pohon Pencarian Biner yang bekerja lewat sistem percabangan. Setiap titik data di dalamnya menyimpan nama barang sekaligus harganya yang menjadi acuan utama. Pohon ini memisahkan data ke dua arah, di mana barang yang lebih murah otomatis masuk ke cabang kiri, sedangkan yang lebih mahal masuk ke cabang kanan. Ketika ingin menampilkan katalog, program menggunakan metode Inorder Traversal yang membaca cabang kiri terlebih dahulu baru kemudian beralih ke kanan, sehingga daftar barang otomatis tersusun rapi dari harga termurah hingga termahal.


**Source Kode**

<img width="757" height="502" alt="kode 1" src="https://github.com/user-attachments/assets/0243546c-91ee-4f58-ab4d-833811b9e40a" />

<img width="634" height="439" alt="kode 2" src="https://github.com/user-attachments/assets/14f2790e-6b77-493e-bd80-e657b12bf4cc" />

<img width="707" height="440" alt="kode 3" src="https://github.com/user-attachments/assets/d3547861-a808-49e3-a23a-4198afd42695" />

<img width="581" height="472" alt="kode 4" src="https://github.com/user-attachments/assets/bbffd21a-c93a-47cc-80f5-301a4bf2f93d" />

<img width="749" height="440" alt="kode 5" src="https://github.com/user-attachments/assets/8fe2386f-2c6d-4448-8943-238010c52802" />

<img width="768" height="321" alt="kode 6" src="https://github.com/user-attachments/assets/d91898c4-3709-4c1b-83c8-1970799de3a8" />

class Node:

Logika: Kita membuat sebuah cetakan atau definisi objek baru bernama Node. Anggap saja ini seperti mendesain struktur label kotak barang di gudang.

def __init__(self, key, nama_barang): 

Logika: fungsi persiapan awal saat sebuah kotak barang baru dibuat. Fungsi ini meminta dua informasi wajib: harga barang (key) dan nama barangnya (nama_barang).

self.key = key 

Logika: Komputer mencatat dan mengunci nominal harga yang dimasukkan ke dalam variabel internal bernama key.

self.nama_barang = nama_barang 
Logika: Komputer mencatat nama barang yang dimasukkan ke dalam variabel internal bernama nama_barang.

self.left = None 

Menginisialisasi penunjuk arah kiri (left pointer) dengan nilai None. Ini berarti saat objek dibuat, ia belum terhubung ke anak kiri (left child).

self.right = None 
Menginisialisasi penunjuk arah kanan (right pointer) dengan nilai None. Ini berarti objek baru belum memiliki hubungan ke anak kanan (right child).

class TokoBST:

Mendeklarasikan kelas utama bernama TokoBST yang akan mengelola seluruh node menjadi satu kesatuan struktur pohon pencarian biner (BST).

def __init__(self): 

Fungsi untuk menginisialisasi status awal dari struktur data pohon.

self.root = None 

Mengatur atribut .root (node akar teratas) dengan nilai awal None, menandakan bahwa pohon dalam kondisi kosong (empty tree).

def insert_node(self, root, key, nama_barang): 
fungsi rekursif internal untuk mencari posisi selip yang tepat. Menerima argumen berupa status node saat ini (root), nilai key baru, dan nama_barang baru.

if root is None:

Kondisi berhenti rekursif (base case). Memeriksa apakah posisi pointer saat ini bernilai kosong (None).

return Node(key, nama_barang) 

Jika kondisi terpenuhi, fungsi akan melakukan instansiasi objek Node baru menggunakan argumen tersebut dan mengembalikannya ke pemanggil.

if key < root.key: 

Kondisi percabangan pertama. Membandingkan apakah nilai key baru lebih kecil dari nilai .key milik node saat ini.

root.left = self.insert_node(root.left, key, nama_barang) 
Jika kondisi lebih kecil terpenuhi, fungsi memanggil dirinya sendiri secara rekursif ke arah root.left dan hasilnya diikat kembali ke penunjuk .left node saat ini.

elif key > root.key: 

Kondisi percabangan kedua. Memeriksa apakah nilai key baru lebih besar dari nilai .key milik node saat ini.

root.right = self.insert_node(root.right, key, nama_barang) 

Jika kondisi lebih besar terpenuhi, fungsi memanggil dirinya sendiri secara rekursif ke arah root.right dan hasilnya diikat kembali ke penunjuk .right node saat ini.

return root 

Mengembalikan referensi alamat memori dari node saat ini (root) untuk menjaga keutuhan struktur pohon yang terhubung setelah rekursi selesai.


def insert(self, key, nama_barang): 

Fungsi antarmuka publik yang dieksekusi oleh pengguna untuk menambahkan data.

self.root = self.insert_node(self.root, key, nama_barang) 

Memulai eksekusi fungsi rekursif insert_node dengan mengoper titik mulai dari akar utama pohon (self.root), lalu memperbarui status .root dengan pohon baru.

def search_node(self, root, key): 

Fungsi rekursif internal untuk melacak keberadaan key tertentu di dalam memori pohon.

if root is None: 

Base case pertama. Memeriksa apakah pencarian telah mencapai ujung daun kosong tanpa menemukan hasil.

return None 

Jika mencapai node kosong, fungsi mengembalikan nilai None (artinya data tidak ditemukan).

if root.key == key:

Base case kedua. Memeriksa apakah nilai .key pada node saat ini sama persis dengan key yang dicari.

return root)

Jika bernilai sama, proses rekursi berhenti dan fungsi mengembalikan seluruh objek root tersebut.

if key < root.key: 

Memeriksa apakah nilai key yang dicari memiliki nominal lebih kecil dari nilai node saat ini.

return self.search_node(root.left, key)

Jika lebih kecil, arah pencarian dialihkan dengan memanggil kembali fungsi secara rekursif ke sub-pohon bagian kiri (root.left).

return self.search_node(root.right, key)

Jika tidak lebih kecil (berarti lebih besar), arah pencarian otomatis dialihkan ke sub-pohon bagian kanan (root.right) melalui panggilan rekursif.

Operasi Pencarian Data Publik (search)
def search(self, key):

Fungsi untuk mengakses fitur pencarian data.

return self.search_node(self.root, key) 
Mengeksekusi dan mengembalikan hasil dari fungsi search_node yang dijalankan pertama kali dari koordinat .root. 

def urut_murah_ke_mahal(self, root):

Metode penelusuran pohon menggunakan algoritma Inorder Traversal (pola urutan kunjungan: Kiri - Root - Kanan).

if root is None:

Kondisi batas rekursif. Memeriksa apakah penelusuran telah menyentuh batas terbawah dari suatu cabang pohon.

return 

Jika benar kosong, fungsi melakukan perintah return kosong untuk keluar dari tumpukan eksekusi (pop stack) dan kembali ke node parent sebelumnya.

self.urut_murah_ke_mahal(root.left)

Fungsi melakukan panggilan rekursif mendalam ke cabang sebelah kiri (root.left) untuk memproses seluruh data bernilai lebih kecil terlebih dahulu.

print(f"- {root.nama_barang}: Rp{root.key}") 

Menampilkan (output) string berisi nilai atribut .nama_barang dan .key milik node yang sedang aktif ke layar konsol.

self.urut_murah_ke_mahal(root.right) 

Fungsi melakukan panggilan rekursif ke cabang sebelah kanan (root.right) untuk memproses sisa data yang bernilai lebih besar.

def find_min(self, root): 

Metode berulang (iterative method) untuk menemukan nilai terkecil pada pohon.

if root is None:

Validasi awal untuk memeriksa apakah parameter objek pohon yang dikirimkan bernilai kosong.

return None

Jika kosong, fungsi langsung mengembalikan nilai None untuk menghindari error pembacaan memori.

current = root 

Mendeklarasikan variabel pointer lokal baru bernama current yang merujuk pada alamat memori node root sebagai titik awal penelusuran.

while current.left is not None:

Menjalankan blok perulangan (looping). Kondisinya adalah selama atribut pointer .left milik objek current tidak bernilai kosong (None), maka program akan terus melompat masuk ke node anak bagian kiri (current = current.left).

def find_max(self, root):

Mendeklarasikan fungsi internal untuk mendeteksi node dengan nilai key terbesar di dalam pohon.

if root is None:

Validasi untuk memeriksa apakah parameter objek pohon yang dioper bernilai kosong.

return None

Jika pohon kosong, fungsi langsung mengembalikan nilai None untuk mencegah kesalahan pembacaan memori.

current = root 

Membuat variabel pointer lokal bernama current dan mengisinya dengan koordinat awal node root.

while current.right is not None: 

Melakukan perulangan selama pointer anak kanan (.right) milik node current memiliki isi atau tidak bernilai None.

current = current.right

Menggeser posisi pointer current untuk masuk satu tingkat lebih dalam ke node anak bagian kanan.

return current

Mengembalikan objek node terakhir (posisi paling ujung kanan kanan) yang otomatis merupakan pemilik harga tertinggi.

def count_nodes(self, root): 

Mendeklarasikan fungsi rekursif untuk menghitung total kuantitas node yang hidup di dalam pohon.

if root is None: 

Base case rekursi, mendeteksi jika penelusuran telah mencapai cabang kosong.

return 0 

Jika posisi kosong, fungsi mengembalikan nilai integer 0 ke tumpukan eksekusi.

return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

Menghitung total node dengan rumus akumulasi: angka 1 (node saat ini) ditambah hasil perhitungan rekursif cabang kiri, ditambah hasil rekursif cabang kanan.

def sum_nodes(self, root):

Mendeklarasikan fungsi rekursif untuk menjumlahkan seluruh nominal angka key yang ada di dalam pohon.

if root is None: 
Base case rekursi untuk mendeteksi batas akhir atau cabang yang kosong.

return 0 

Jika kosong, fungsi mengembalikan nilai 0 agar tidak memengaruhi hasil penjumlahan.

return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right) 

Mengembalikan hasil penjumlahan nilai .key milik node saat ini, dikombinasikan dengan total nilai dari hasil rekursi sub-pohon kiri dan sub-pohon kanan.

def main(): 

Deklarasi fungsi utama aplikasi tempat seluruh skenario eksekusi dijalankan.

toko = TokoBST() 

Instansiasi objek baru dari kelas TokoBST ke dalam variabel lokal toko untuk mengaktifkan struktur data pohon kosong.

toko.insert(50000, "Kemeja Polos") sampai toko.insert(75000, "Celana Pendek") 

Memanggil metode .insert() secara beruntun untuk menyuntikkan 5 data barang awal ke dalam memori objek toko.

pilih = 0 

Inisialisasi variabel kontrol bernama pilih dengan nilai awal 0 sebagai penampung angka menu.

while pilih != 7:

Membuka blok perulangan looping menu utama, yang akan terus berjalan selama nilai variabel pilih tidak sama dengan 7.

print(...) (Baris 82-89)

Mengeksekusi perintah keluaran (output) standar untuk mencetak antarmuka teks menu manajemen toko ke layar terminal.

try: 

Membuka blok penanganan kesalahan (error handling) untuk mengantisipasi kegagalan input data dari pengguna.

pilih = int(input("Pilih menu: "))

Menangkap string masukan pengguna melalui fungsi input(), mengonversinya menjadi tipe data integer lewat int(), lalu menyimpannya ke variabel pilih.

except ValueError: 

Menangkap pengecualian error (ValueError) jika pengguna memasukkan input karakter teks non-angka.

print("Input tidak valid!") 

Menampilkan pesan peringatan kesalahan format input ke layar konsol.

continue

Memaksa program untuk langsung melompat kembali ke awal perulangan while tanpa mengeksekusi baris kode di bawahnya.

elif pilih == 1: 

Jika nilai variabel pilih sama dengan 1, program mengeksekusi blok kode penambahan barang.

try: 

Membuka blok penanganan kesalahan (error handling) khusus untuk input penambahan data barang.

harga = int(input("Masukkan harga barang: Rp")) 

Menerima input teks harga dari pengguna, mengonversinya menjadi integer, lalu menyimpannya ke variabel lokal harga.

nama = input("Masukkan nama barang: ") 

Menerima input teks nama produk dari pengguna dan menyimpannya langsung ke variabel string nama.

toko.insert(harga, nama) 

Memanggil metode .insert() milik objek toko dengan mengirimkan argumen harga dan nama untuk dimasukkan ke memori pohon.

print(f"{nama} berhasil ditambahkan!") 

Menampilkan string konfirmasi sukses ke layar konsol dengan memformat variabel nama.

except ValueError: 

Blok penangkap kesalahan jika pengguna memasukkan karakter non-angka pada kolom input harga.

print("Harga harus berupa angka!") 

Menampilkan teks pesan kesalahan ke konsol pengguna jika terjadi kegagalan konversi integer.

elif pilih == 2:

Penjelasan: Evaluasi kondisi bersyarat. Jika nilai pilih sama dengan 2, program beralih ke operasi pencarian data.

try: 

Membuka blok penanganan kesalahan untuk mengantisipasi kesalahan ketik pada menu pencarian.

harga_cari = int(input("Cari barang dengan harga: Rp")) 

Mengambil input nominal angka harga yang ingin dicari dan menyimpannya ke variabel harga_cari.

hasil = toko.search(harga_cari) 

Memanggil fungsi .search() milik objek toko dan menyimpan objek kembaliannya (Node atau None) ke dalam variabel hasil.

if hasil: 

Evaluasi kondisi boolean. Memeriksa apakah variabel hasil berisi sebuah objek Node (bernilai True) atau kosong (bernilai False).

print(f"Ditemukan: {hasil.nama_barang} seharga Rp{hasil.key}") 

Jika objek ditemukan, program mengambil properti .nama_barang dan .key milik node tersebut lalu mencetaknya ke layar.

else:

Blok alternatif jika kondisi if hasil tidak terpenuhi (variabel bernilai None).

print("Tidak ada barang dengan harga tersebut.")

Mencetak string pemberitahuan bahwa pencarian harga gagal atau data tidak eksis di pohon.

except ValueError: 

Menangkap kesalahan format input jika kolom pencarian diisi teks non-angka.

print("Input harus angka!") 

Menampilkan pesan kesalahan input ke konsol.

elif pilih == 3: 
Evaluasi kondisi bersyarat untuk membuka fitur cetak seluruh data inventaris toko.

print("\n--- KATALOG PRODUK ---") 

Mencetak teks pemisah dekoratif untuk judul katalog ke konsol.

toko.urut_murah_ke_mahal(toko.root) 

Menjalankan metode Inorder Traversal dengan melempar parameter node akar teratas (toko.root) untuk mencetak semua barang secara terurut.

elif pilih == 4:

Evaluasi kondisi bersyarat jika pengguna menekan angka menu 4.

min_node = toko.find_min(toko.root)

Memanggil fungsi penelusuran cabang kiri dan menyimpan objek node dengan nilai terendah ke variabel min_node.

max_node = toko.find_max(toko.root)

Memanggil fungsi penelusuran cabang kanan dan menyimpan objek node dengan nilai tertinggi ke variabel max_node.

if min_node and max_node:

Memeriksa kondisi validitas memori untuk memastikan kedua objek tersebut ada (pohon tidak dalam kondisi kosong).

print(f"Termurah: {min_node.nama_barang} (Rp{min_node.key})") 

Mengekstrak dan menampilkan nama serta harga produk dari objek penampung nilai minimum.

print(f"Termahal: {max_node.nama_barang} (Rp{max_node.key})") 

Mengekstrak dan menampilkan nama serta harga produk dari objek penampung nilai maksimum.

elif pilih == 5: 

Evaluasi kondisi bersyarat jika pengguna memilih opsi menu 5.

print(f"Total variasi produk di toko: {toko.count_nodes(toko.root)} jenis") 

Memanggil fungsi perhitungan node count_nodes dari titik akar, lalu mencetak total variasi barang yang aktif.

elif pilih == 6: 

Evaluasi kondisi bersyarat jika pengguna memilih opsi menu 6.

print(f"Total nilai gabungan aset produk: Rp{toko.sum_nodes(toko.root)}") 

Memanggil fungsi akumulator sum_nodes dari titik akar, lalu menampilkan total nilai finansial aset ke layar.

elif pilih == 7:

Evaluasi kondisi bersyarat akhir untuk menangkap instruksi keluar dari aplikasi.

print("Program selesai.") 

Penjelasan: Mencetak kalimat penutup aplikasi ke layar konsol sebelum perulangan menu dihentikan.

if __name__ == "__main__": 

Kondisi khusus Python untuk mendeteksi apakah berkas script ini dieksekusi secara langsung sebagai program utama, bukan diimpor sebagai modul oleh berkas lain.

main() 

Memanggil dan memicu jalannya fungsi komponen pengendali utama main() untuk memulai aplikasi.


**Output**

<img width="631" height="459" alt="output 1" src="https://github.com/user-attachments/assets/5554f112-717b-417a-8c56-41ad0680f931" />

<img width="534" height="550" alt="output 2" src="https://github.com/user-attachments/assets/0d50a34e-be28-4bb8-a961-b0d88fc1a000" />

<img width="630" height="607" alt="output 3" src="https://github.com/user-attachments/assets/d61c5598-1358-4424-b0f2-6b9a0339b4f8" />

Saat pengguna memasukkan Baju Cardigan seharga 30000 rupiah, program langsung menempatkannya ke posisi cabang yang tepat agar urutan pohon tidak berantakan. Keunggulan sistem ini langsung terlihat saat pengguna mencari harga 15000 rupiah, di mana program bisa langsung menemukan Gantungan Kunci secara instan tanpa harus mengecek seluruh barang satu per satu dari awal.

Kerapian sistem pohon ini terbukti saat semua daftar barang dicetak. Karena data yang lebih murah selalu ditaruh di sebelah kiri dan yang lebih mahal di sebelah kanan, program tinggal membacanya secara berurutan dari kiri ke kanan untuk menghasilkan daftar katalog yang otomatis terurut dari harga termurah sampai termahal. Melalui logika yang sama, program juga bisa langsung menunjuk ujung cabang paling kiri untuk menemukan produk termurah dan ujung cabang paling kanan untuk produk termahal, yaitu Gantungan Kunci dan Jaket Denim.

Pada bagian akhir, program menghitung total seluruh titik data yang aktif di dalam memorinya untuk mengetahui bahwa ada enam jenis variasi produk di dalam toko. Bersamaan dengan itu, program juga menjumlahkan angka harga dari setiap barang yang ada di dalam jaringan pohon tersebut untuk menghasilkan hitungan total nilai aset toko secara tepat, yaitu sebesar 315000 rupiah.
















