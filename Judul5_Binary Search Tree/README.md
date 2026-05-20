**Sistem Manajemen Stok Toko berbasis BST**

**Deskripsi Singkat**

Program ini adalah aplikasi kasir dan gudang sederhana untuk mengelola stok barang secara fleksibel. Lewat program ini, kamu bisa menambah produk baru, mencari barang lewat harganya, serta menghitung jumlah variasi stok dan total nilai aset toko.
Keunggulan utamanya ada pada efisiensi. Katalog produk otomatis tersusun rapi dari yang termurah sampai termahal tanpa perlu proses urut ulang (sorting) yang bikin lemot. Selain itu, kamu juga bisa langsung tahu produk mana yang paling murah dan paling mahal secara instan.

Aplikasi ini menggunakan struktur data Binary Search Tree (BST) atau Pohon Pencarian Biner. Cara kerjanya mirip percabangan pohon dengan aturan berikut:

Isi Data: Setiap titik data (node) menyimpan dua info sekaligus, yaitu nama barang dan harga barang (sebagai acuan angka).

Cabang Kiri: Otomatis menampung barang-barang yang harganya lebih murah.

Cabang Kanan: Otomatis menampung barang-barang yang harganya lebih mahal.

Metode Cetak (Inorder): Program membaca data dari cabang kiri, tengah, lalu kanan. Pola inilah yang membuat daftar katalog otomatis terurut rapi dari yang paling murah ke paling mahal.
