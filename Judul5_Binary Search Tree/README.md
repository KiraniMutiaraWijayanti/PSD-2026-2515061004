**Sistem Manajemen Stok Toko berbasis BST**

**Deskripsi Singkat**

Program ini adalah aplikasi kasir dan gudang sederhana untuk mengelola stok barang secara fleksibel. Lewat program ini, kamu bisa menambah produk baru, mencari barang lewat harganya, serta menghitung jumlah variasi stok dan total nilai aset toko.
Keunggulan utamanya ada pada efisiensi. Katalog produk otomatis tersusun rapi dari yang termurah sampai termahal tanpa perlu proses urut ulang (sorting) yang bikin lemot. Selain itu, kamu juga bisa langsung tahu produk mana yang paling murah dan paling mahal secara instan.

Aplikasi ini menggunakan struktur data Binary Search Tree (BST) atau Pohon Pencarian Biner yang bekerja lewat sistem percabangan. Setiap titik data di dalamnya menyimpan nama barang sekaligus harganya yang menjadi acuan utama. Pohon ini memisahkan data ke dua arah, di mana barang yang lebih murah otomatis masuk ke cabang kiri, sedangkan yang lebih mahal masuk ke cabang kanan. Ketika ingin menampilkan katalog, program menggunakan metode Inorder Traversal yang membaca cabang kiri terlebih dahulu baru kemudian beralih ke kanan, sehingga daftar barang otomatis tersusun rapi dari harga termurah hingga termahal.
