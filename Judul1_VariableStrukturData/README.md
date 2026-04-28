**Sistem Manajemen Antrean Warung MBG**

**Deskripsi Singkat**

Program ini dirancang untuk mengelola sistem antrean pesanan di warung MBG secara efisien menggunakan konsep struktur data dinamis. Program mendukung penambahan antrean reguler, antrean prioritas, penyajian pesanan, serta fitur pembatalan jika ada kesalahan dalam penyajian.

Algoritma yang digunakan dalam program ini adalah Doubly Linked List untuk mengelola antrean (queue) agar proses penambahan di depan prioritas maupun di belakang dapat dilakukan dengan mudah. Selain itu, program menggunakan konsep stack untuk menyimpan riwayat pesanan yang sudah disajikan, sehingga fitur undo dapat mengembalikan pesanan terakhir yang selesai ke posisi depan antrean.

**Source Code**

<img width="583" height="409" alt="ss 1" src="https://github.com/user-attachments/assets/1f727d99-5972-42fd-b8b2-1be45b3c6f9e" />

<img width="492" height="342" alt="ss 2" src="https://github.com/user-attachments/assets/e61f8d42-2e8b-46aa-b56a-ace73e7074d6" />

<img width="487" height="245" alt="ss 3" src="https://github.com/user-attachments/assets/2b8d2cd3-76f1-4622-9428-6b6484393086" />


**Penjelasan Kode**

class Node: Mendefinisikan cetak biru objek penyimpanan data

def_init_(self, data): inisialisasi awal saat node dibuat

self.data = data: Menyimpan nilai pesanan ke dalam node.

self.next = self.prev = None: Menyiapkan dua "tangan" atau pointer; next untuk menunjuk ke depan dan prev untuk menunjuk ke belakang (Doubly Linked List).

def_init_(self): Menyiapkan kondisi awal sistem saat dijalankan.

self.front = self.rear = None: Pointer front (depan) dan rear (belakang) digunakan untuk mengelola antrean (Queue).

self.top_riwayat = None: Pointer untuk mengelola tumpukan riwayat pesanan yang sudah selesai (Stack).

new = Node(pesanan): Membuat node baru dari nama pesanan.

if not self.front:: Jika antrean masih kosong, maka node baru tersebut menjadi front sekaligus rear.

elif prioritas:: Jika memilih menu prioritas (input 2), node baru diletakkan di paling depan.

new.next, self.front.prev, self.front = self.front, new, new: Melakukan pertukaran pointer agar front yang lama bergeser ke belakang node baru.

else:: Jika pesanan reguler (input 1), node baru diletakkan di paling belakang.

new.prev, self.rear.next, self.rear = self.rear, new, new: Menghubungkan rear yang lama dengan node baru di belakangnya.

if not self.front: return ...: Validasi agar program tidak error jika mencoba menyajikan dari antrean kosong.

pesanan = self.front.data: Mengambil data dari antrean terdepan.

new_history = Node(pesanan): Membuat node baru untuk disimpan di riwayat.

new_history.next, self.top_riwayat = self.top_riwayat, new_history: Menerapkan logika Stack (LIFO), di mana pesanan terbaru yang selesai akan berada di posisi top.

self.front = self.front.next: Menggeser antrean depan ke orang berikutnya.

pesanan = self.top_riwayat.data: Mengambil data dari tumpukan riwayat paling atas.

self.top_riwayat = self.top_riwayat.next: Menghapus data tersebut dari riwayat.

self.tambah_antrean(pesanan, prioritas=True): Memasukkan kembali pesanan tersebut ke antrean paling depan menggunakan fungsi prioritas.

while curr_q:: Mengunjungi setiap node dari front sampai None untuk mengumpulkan daftar antrean.

while curr_h:: Mengunjungi setiap node dari top_riwayat untuk mengumpulkan daftar pesanan yang sudah selesai.

menu = { ... }: Menggunakan Dictionary dan Lambda untuk memetakan input angka pengguna ke fungsi yang sesuai di dalam class WarungMBG.

while True:: Menjalankan perulangan menu terus-menerus hingga pengguna memilih angka '6' (Keluar).












