**Program Pengecekan Motor di Parkiran**

**Deskripsi Singkat**

Program ini adalah simulasi database kendaraan berbasis Hash Table berukuran 10 slot yang berfungsi menyimpan dan mencari data plat nomor berdasarkan kunci angka.

Struktur data ini menggunakan fungsi hash modulo untuk menentukan posisi indeks data secara cepat. Jika terjadi bentrokan indeks (collision), metode Open Addressing dengan Linear Probing akan mencari slot terdekat berikutnya secara berurutan. Keandalan sistem ini didukung oleh Manajemen Status Slot (EMPTY, OCCUPIED, DELETED) yang menjaga agar alur pencarian data tidak terputus saat ada data yang dihapus. Di akhir program, mekanisme ini langsung diuji melalui penginputan empat data motor serta simulasi pencarian kuncinya.

Source Kode

<img width="684" height="582" alt="kode 1" src="https://github.com/user-attachments/assets/e0f855eb-aa89-4b1b-af6d-8e6c728f6c43" />

<img width="722" height="518" alt="kode 2" src="https://github.com/user-attachments/assets/9a424a0f-3d45-4c00-ba0b-c791eafc422d" />

<img width="733" height="507" alt="kode 3" src="https://github.com/user-attachments/assets/4760a5eb-f870-4581-8f24-d8e75a28492b" />

<img width="638" height="480" alt="kode 4" src="https://github.com/user-attachments/assets/cf08263e-67b8-4dcd-91ed-38908282d914" />

class SlotState:
kelas SlotState yang digunakan sebagai penanda status setiap slot pada hash table.

EMPTY = 0
Menandakan slot masih kosong dan belum pernah digunakan.

OCCUPIED = 1
Menandakan slot sedang berisi data.

DELETED = 2
Menandakan data pada slot sudah dihapus tetapi slot tersebut pernah digunakan.

class Entry:
Membuat kelas untuk menyimpan satu data pada hash table.

def __init__(self):
Fungsi yang dijalankan saat objek Entry dibuat.

self.key = None
Menyimpan key data. Awalnya bernilai None.

self.value = None
Menyimpan informasi atau nilai data. Awalnya None.

self.state = SlotState.EMPTY
Status awal slot adalah kosong.

class HashMapOpenAddressing:
Membuat kelas hash table menggunakan metode Open Addressing.

def __init__(self, size=10):
Constructor untuk membuat hash table dengan ukuran 10

elf.SIZE = size
Menyimpan ukuran hash table.

self.table = [Entry() for _ in range(self.SIZE)]
Membuat list berisi objek Entry sebanyak ukuran tabel.

def hash_function(self, key):
Fungsi untuk menentukan posisi data dalam tabel.

return (key % self.SIZE + self.SIZE) % self.SIZE
Menghitung indeks hash menggunakan operasi modulo.

def insert(self, key, value):
Digunakan untuk menambahkan data ke hash table.

idx = self.hash_function(key)
Menghitung indeks awal berdasarkan key.

first_deleted = -1
Menyimpan posisi slot yang pernah dihapus.
Nilai -1 berarti belum ditemukan slot DELETED.

for step in range(self.SIZE):
Melakukan probing (pencarian slot kosong) sebanyak ukuran tabel.

i = (idx + step) % self.SIZE
Menghitung posisi saat probing

if self.table[i].state == SlotState.OCCUPIED:
Memeriksa apakah slot sudah terisi.

if self.table[i].key == key:
Jika key sama, data lama akan diperbarui

self.table[i].value = value
Mengganti nilai lama.

return True
Proses selesai.

elif self.table[i].state == SlotState.DELETED:
Jika menemukan slot yang pernah dihapus.

if first_deleted == -1:
Jika belum pernah menyimpan posisi DELETED.

first_deleted = i
Simpan posisi tersebut.

Jika slot EMPTY
            else:
Artinya slot kosong.

if first_deleted != -1:
Jika sebelumnya ada slot DELETED.

i = first_deleted
Gunakan slot DELETED tersebut.

self.table[i].key = key
Menyimpan key.

self.table[i].value = value
Menyimpan informasi kendaraan

self.table[i].state = SlotState.OCCUPIED
Mengubah status menjadi terisi.

return True
Data berhasil ditambahkan.

if first_deleted != -1:
Jika tidak ada slot kosong tetapi ada slot DELETED.

self.table[first_deleted].key = key
Masukkan key ke slot DELETED.

self.table[first_deleted].value = value
Masukkan value.

self.table[first_deleted].state = SlotState.OCCUPIED
Ubah status menjadi terisi.

return True
Berhasil menambah data.

return False
Jika semua slot penuh maka insert gagal.

def search(self, key):
Mencari data berdasarkan key.

idx = self.hash_function(key)
Menentukan indeks awal.

for step in range(self.SIZE):
Melakukan probing.

i = (idx + step) % self.SIZE
Menghitung indeks saat ini.

if self.table[i].state == SlotState.EMPTY:
Jika menemukan slot kosong.
Artinya data tidak ada.

return None
Mengembalikan nilai kosong.

if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
Jika menemukan key yang dicari.

return self.table[i]
Mengembalikan data tersebut.

return None
Jika seluruh tabel dicek dan tidak ditemukan.

def remove_key(self, key):
Menghapus data berdasarkan key

entry = self.search(key)
Mencari data terlebih dahulu.

if entry is None:
Jika data tidak ditemukan.

return False
Penghapusan gagal.

entry.state = SlotState.DELETED
Mengubah status menjadi DELETED.
Data dianggap terhapus.

return True
Penghapusan berhasil.

def display(self):
Menampilkan isi hash table

print("\nIsi Hash Table (Data Kendaraan):")
Menampilkan judul.

for i in range(self.SIZE):
Menelusuri semua indeks tabel.

print(f"{i}: ", end="")
Menampilkan nomor indeks.

if self.table[i].state == SlotState.EMPTY:
Jika slot kosong.

print("EMPTY")
Menampilkan EMPTY.

elif self.table[i].state == SlotState.DELETED:
Jika slot dihapus.

print("DELETED")
Menampilkan DELETED.

else:
Jika slot berisi data.

print(f"(Key Angka: {self.table[i].key}, Info: {self.table[i].value})")
Menampilkan key dan informasi kendaraan.

def cek_plat(self, kode_plat):
Mencari data plat kendaraan berdasarkan kode.

hasil = self.search(kode_plat)
Memanggil fungsi pencarian.

if hasil is not None:
Jika ditemukan.

print(f"Data ditemukan -> {hasil.value}")
Menampilkan informasi kendaraan.

else:
Jika tidak ditemukan.

print("Data plat motor tidak ditemukan!")
Menampilkan pesan gagal.

def main():
Program utama.

data_motor = HashMapOpenAddressing(size=10)
Membuat hash table berukuran 10.

data_motor.insert(18, "BD 1234 XI (Honda Beat - Wijayanti)")
Menambahkan data kendaraan pertama.

Hash:
18 % 10 = 8
Masuk indeks 8.

data_motor.insert(15, "DB 8888 XY (Yamaha NMax - Mutiara)")
15 % 10 = 5
Masuk indeks 5.

data_motor.insert(33, "BE 4571 XA (Suzuki Nex - Kirani)")
33 % 10 = 3
Masuk indeks 3.

data_motor.insert(49, "F 2026 FG (Vespa Sprint - Arutala)")
49 % 10 = 9
Masuk indeks 9.

data_motor.display()
Menampilkan seluruh isi hash table.

print("-" * 50)
Menampilkan garis pemisah

print("\n[Mencari Plat Motor dengan angka 18]")
Menampilkan judul pencarian.

data_motor.cek_plat(18)
Mencari data key 18.

print("\n[Mencari Plat Motor dengan angka 33]")
Menampilkan judul pencarian.

data_motor.cek_plat(33)
Mencari data key 33.

print("\n[Mencari Plat Motor dengan angka (49)]")
Menampilkan judul pencarian.

data_motor.cek_plat(49)
Mencari data key 49.

if __name__ == "__main__":
Memastikan program dijalankan langsung, bukan diimpor dari file lain.

main()
Memanggil fungsi utama.

Output

<img width="800" height="453" alt="output 1" src="https://github.com/user-attachments/assets/522596cc-0dd3-4c40-9d06-c0ea15ff1e89" />

Output dari program diatas adalah memetakan memori tabel hash dan melakukan pencarian secara akurat. Empat data kendaraan berhasil disimpan ke dalam slot yang sesuai dengan sisa hasil bagi fungsi hash modulo: kunci 33 di indeks 3, 15 di indeks 5, 18 di indeks 8, dan 49 di indeks 9, sementara slot lainnya tetap berstatus EMPTY. 

Kemudian program mendemonstrasikan fitur pencarian instan untuk kunci 18, 33, dan 49. Sistem langsung menuju indeks hasil kalkulasi hash masing-masing dan sukses mencetak informasi detail kendaraan beserta nama pemiliknya ke layar terminal tanpa harus memindai seluruh isi tabel dari awal.


