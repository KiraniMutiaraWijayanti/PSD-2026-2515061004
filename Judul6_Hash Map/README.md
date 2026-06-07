**Program Pengecekan Motor di Parkiran**

**Deskripsi Singkat**

Program ini adalah simulasi database kendaraan berbasis Hash Table berukuran 10 slot yang berfungsi menyimpan dan mencari data plat nomor berdasarkan kunci angka.

Struktur data ini menggunakan fungsi hash modulo untuk menentukan posisi indeks data secara cepat. Jika terjadi bentrokan indeks (collision), metode Open Addressing dengan Linear Probing akan mencari slot terdekat berikutnya secara berurutan. Keandalan sistem ini didukung oleh Manajemen Status Slot (EMPTY, OCCUPIED, DELETED) yang menjaga agar alur pencarian data tidak terputus saat ada data yang dihapus. Di akhir program, mekanisme ini langsung diuji melalui penginputan empat data motor serta simulasi pencarian kuncinya.

Source Kode

<img width="684" height="582" alt="kode 1" src="https://github.com/user-attachments/assets/e0f855eb-aa89-4b1b-af6d-8e6c728f6c43" />

<img width="722" height="518" alt="kode 2" src="https://github.com/user-attachments/assets/9a424a0f-3d45-4c00-ba0b-c791eafc422d" />

<img width="733" height="507" alt="kode 3" src="https://github.com/user-attachments/assets/4760a5eb-f870-4581-8f24-d8e75a28492b" />

<img width="638" height="480" alt="kode 4" src="https://github.com/user-attachments/assets/cf08263e-67b8-4dcd-91ed-38908282d914" />

class SlotState

Kelas SlotState digunakan sebagai penanda status setiap slot pada Hash Table.

EMPTY = 0
Menandakan slot masih kosong dan belum pernah digunakan.

OCCUPIED = 1
Menandakan slot sedang berisi data mahasiswa.

DELETED = 2
Menandakan data pada slot sudah dihapus tetapi slot tersebut pernah digunakan sebelumnya.

class Entry

Membuat kelas untuk menyimpan satu data mahasiswa pada Hash Table.

def init(self):
Fungsi yang dijalankan saat objek Entry dibuat.

self.key = None
Menyimpan key data berupa NPM mahasiswa. Awalnya bernilai None.

self.value = None
Menyimpan informasi berupa nama mahasiswa dan nilai yang diperoleh. Awalnya bernilai None.

self.state = SlotState.EMPTY
Menentukan bahwa status awal slot adalah kosong.

class HashMapOpenAddressing

Membuat kelas Hash Table menggunakan metode Open Addressing.

def init(self, size=10)

Constructor untuk membuat Hash Table dengan ukuran 10 slot.

self.SIZE = size
Menyimpan ukuran Hash Table.

self.table = [Entry() for _ in range(self.SIZE)]
Membuat list yang berisi objek Entry sebanyak ukuran tabel.

def hash_function(self, key)

Fungsi untuk menentukan posisi data mahasiswa dalam tabel.

return (key % self.SIZE + self.SIZE) % self.SIZE
Menghitung indeks hash menggunakan operasi modulo terhadap ukuran tabel.

def insert(self, key, value)

Digunakan untuk menambahkan data mahasiswa ke dalam Hash Table.

idx = self.hash_function(key)
Menghitung indeks awal berdasarkan NPM mahasiswa.

first_deleted = -1
Menyimpan posisi slot yang pernah dihapus. Nilai -1 berarti belum ditemukan slot DELETED.

for step in range(self.SIZE):
Melakukan probing atau pencarian slot kosong sebanyak ukuran tabel.

i = (idx + step) % self.SIZE
Menghitung posisi saat proses probing menggunakan Linear Probing.

if self.table[i].state == SlotState.OCCUPIED:
Memeriksa apakah slot sudah terisi data.

if self.table[i].key == key:
Jika NPM yang dimasukkan sudah ada, maka data lama akan diperbarui.

self.table[i].value = value
Mengganti data nilai mahasiswa yang lama dengan data baru.

return True
Menandakan proses update data berhasil.

elif self.table[i].state == SlotState.DELETED:
Memeriksa apakah slot pernah digunakan tetapi datanya sudah dihapus.

if first_deleted == -1:
Jika belum ada slot DELETED yang tersimpan.

first_deleted = i
Menyimpan posisi slot DELETED tersebut.

else:
Berarti slot yang ditemukan masih kosong.

if first_deleted != -1:
Jika sebelumnya ditemukan slot DELETED.

i = first_deleted
Menggunakan slot DELETED tersebut untuk menyimpan data baru.

self.table[i].key = key
Menyimpan NPM mahasiswa sebagai key.

self.table[i].value = value
Menyimpan nama mahasiswa beserta nilainya sebagai value.

self.table[i].state = SlotState.OCCUPIED
Mengubah status slot menjadi terisi.

return True
Menandakan data berhasil ditambahkan.

if first_deleted != -1:
Jika tidak ditemukan slot kosong tetapi ada slot DELETED.

self.table[first_deleted].key = key
Menyimpan NPM pada slot DELETED.

self.table[first_deleted].value = value
Menyimpan informasi mahasiswa pada slot DELETED.

self.table[first_deleted].state = SlotState.OCCUPIED
Mengubah status slot menjadi terisi.

return True
Menandakan proses penyimpanan berhasil.

return False
Jika seluruh tabel penuh dan tidak ada slot yang dapat digunakan.

def search(self, key)

Digunakan untuk mencari data mahasiswa berdasarkan NPM.

idx = self.hash_function(key)
Menentukan indeks awal pencarian.

for step in range(self.SIZE):
Melakukan proses probing.

i = (idx + step) % self.SIZE
Menghitung indeks yang sedang diperiksa.

if self.table[i].state == SlotState.EMPTY:
Jika menemukan slot kosong.

return None
Menandakan data mahasiswa tidak ditemukan.

if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
Jika ditemukan NPM yang dicari.

return self.table[i]
Mengembalikan data mahasiswa yang ditemukan.

return None
Jika seluruh tabel telah diperiksa dan data tidak ditemukan.

def remove_key(self, key)

Digunakan untuk menghapus data mahasiswa berdasarkan NPM.

entry = self.search(key)
Mencari data mahasiswa terlebih dahulu.

if entry is None:
Jika data tidak ditemukan.

return False
Menandakan penghapusan gagal.

entry.state = SlotState.DELETED
Mengubah status slot menjadi DELETED sehingga data dianggap telah dihapus.

return True
Menandakan penghapusan berhasil.

def display(self)

Digunakan untuk menampilkan isi Hash Table.

print("\nIsi Hash Table (Data Nilai Mahasiswa):")
Menampilkan judul data yang akan ditampilkan.

for i in range(self.SIZE):
Menelusuri seluruh indeks pada Hash Table.

print(f"{i}: ", end="")
Menampilkan nomor indeks.

if self.table[i].state == SlotState.EMPTY:
Jika slot kosong.

print("EMPTY")
Menampilkan status EMPTY.

elif self.table[i].state == SlotState.DELETED:
Jika slot pernah digunakan tetapi datanya sudah dihapus.

print("DELETED")
Menampilkan status DELETED.

else:
Jika slot berisi data mahasiswa.

print(f"(NPM: {self.table[i].key}, Nilai: {self.table[i].value})")
Menampilkan NPM serta informasi nilai mahasiswa.

def cek_nilai(self, nilai)

Digunakan untuk mencari data nilai mahasiswa berdasarkan NPM.

hasil = self.search(nilai)
Memanggil fungsi pencarian.

if hasil is not None:
Jika data ditemukan.

print(f"Data ditemukan -> {hasil.value}")
Menampilkan nama mahasiswa dan nilai yang diperoleh.

else:
Jika data tidak ditemukan.

print("Data nilai Mahasiswa tidak ditemukan!")
Menampilkan pesan bahwa data tidak tersedia.

def main()

Merupakan fungsi utama program.

data_nilai = HashMapOpenAddressing(size=10)
Membuat Hash Table dengan ukuran 10 slot.

data_nilai.insert(2515061004, "Kirana Larasati = A+")
Menambahkan data mahasiswa pertama.

Hash:

2515061004 % 10 = 4

Disimpan pada indeks 4.

data_nilai.insert(2515061068, "Radita Pramesti Regita C.A = B+")

Hash:

2515061068 % 10 = 8

Disimpan pada indeks 8.

data_nilai.insert(2515061009, "Dwika Prilando = B+")

Hash:

2515061009 % 10 = 9

Disimpan pada indeks 9.

data_nilai.insert(2515061001, "Budi Santoso = B")

Hash:

2515061001 % 10 = 1

Disimpan pada indeks 1.

data_nilai.display()
Menampilkan seluruh isi Hash Table.

print("-" * 50)
Menampilkan garis pemisah.

print("\n[Mencari nilai Mahasiswa dengan NPM]")
Menampilkan judul pencarian.

data_nilai.cek_nilai(2515061004)
Mencari data mahasiswa dengan NPM 2515061004.

data_nilai.cek_nilai(2515061001)
Mencari data mahasiswa dengan NPM 2515061001.

data_nilai.cek_nilai(2515061009)
Mencari data mahasiswa dengan NPM 2515061009.

if name == "main":

Digunakan untuk memastikan program dijalankan secara langsung, bukan diimpor dari file lain.

main()
Memanggil fungsi utama sehingga seluruh proses penyimpanan, penampilan, dan pencarian data nilai mahasiswa dapat dijalankan.



