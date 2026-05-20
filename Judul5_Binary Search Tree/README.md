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



**Output**

<img width="631" height="459" alt="output 1" src="https://github.com/user-attachments/assets/5554f112-717b-417a-8c56-41ad0680f931" />

<img width="534" height="550" alt="output 2" src="https://github.com/user-attachments/assets/0d50a34e-be28-4bb8-a961-b0d88fc1a000" />

<img width="630" height="607" alt="output 3" src="https://github.com/user-attachments/assets/d61c5598-1358-4424-b0f2-6b9a0339b4f8" />

Saat pengguna memasukkan Baju Cardigan seharga 30000 rupiah, program langsung menempatkannya ke posisi cabang yang tepat agar urutan pohon tidak berantakan. Keunggulan sistem ini langsung terlihat saat pengguna mencari harga 15000 rupiah, di mana program bisa langsung menemukan Gantungan Kunci secara instan tanpa harus mengecek seluruh barang satu per satu dari awal.

Kerapian sistem pohon ini terbukti saat semua daftar barang dicetak. Karena data yang lebih murah selalu ditaruh di sebelah kiri dan yang lebih mahal di sebelah kanan, program tinggal membacanya secara berurutan dari kiri ke kanan untuk menghasilkan daftar katalog yang otomatis terurut dari harga termurah sampai termahal. Melalui logika yang sama, program juga bisa langsung menunjuk ujung cabang paling kiri untuk menemukan produk termurah dan ujung cabang paling kanan untuk produk termahal, yaitu Gantungan Kunci dan Jaket Denim.

Pada bagian akhir, program menghitung total seluruh titik data yang aktif di dalam memorinya untuk mengetahui bahwa ada enam jenis variasi produk di dalam toko. Bersamaan dengan itu, program juga menjumlahkan angka harga dari setiap barang yang ada di dalam jaringan pohon tersebut untuk menghasilkan hitungan total nilai aset toko secara tepat, yaitu sebesar 315000 rupiah.
















