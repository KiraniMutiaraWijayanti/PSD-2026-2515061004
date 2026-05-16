**Program Tumpukan Buku di Perpustakaan**

**Deskripsi Singkat**

Aplikasi ini merupakan simulasi tumpukan buku interaktif yang dioperasikan lewat perintah teks di terminal. Di sini, kita bisa dengan mudah menambah buku baru, mengambil buku dari posisi paling atas, mengintip buku teratas tanpa harus memindahkannya, atau melihat semua daftar buku yang ada. Supaya aplikasi tidak mendadak macet atau error saat kita salah mengetikkan pilihan, program ini sudah dipasang sistem penangkap kesalahan otomatis.

Di balik layarnya, program ini memanfaatkan struktur data Stack (Tumpukan) dengan basis array berukuran tetap. Aturan main dari tumpukan ini memakai prinsip LIFO (Last In, First Out). Sederhananya, buku yang paling terakhir kita taruh di atas tumpukan justru akan menjadi buku yang pertama kali diambil saat tumpukan itu dibongkar.


**Source Kode**

<img width="704" height="566" alt="kode 1" src="https://github.com/user-attachments/assets/7637171b-392c-491c-91a7-55243995ca9d" />

<img width="578" height="536" alt="kode 2" src="https://github.com/user-attachments/assets/fe833f02-9f92-4e3f-bfe1-9ead787d23bf" />

<img width="619" height="473" alt="kode 3" src="https://github.com/user-attachments/assets/19d11c3d-69b1-4ac8-8f96-3e19214e7317" />

class StackArray: (Untuk mendeklarasikan kelas baru bernama StackArray)

def __init__(self, max_size=100): (Fungsi ini dipakai untuk menyiapkan tumpukan di awal. Kalau kita tidak memasukkan angka ukurannya pas bikin objek, tumpukan ini otomatis bakal punya kapasitas maksimal 100.

self.MAX = max_size (Menyimpan batas maksimum kapasitas stack ke dalam variabel properti self.MAX.)

self.st = [None] * self.MAX (Membuat list (array) kosong berukuran tetap sebanyak self.MAX dan mengisinya dengan nilai None. Ini adalah tempat penyimpanan elemen tumpukan.)

self.top_idx = -1 (Menginisialisasi penunjuk indeks posisi paling atas (top). Nilai -1 menandakan bahwa stack masih kosong (belum ada indeks 0).

def is_empty(self): (Fungsi yang digunakan untuk mengecek apakah tumpukan dalam keadaan kosong)

return self.top_idx == -1 (Jika nilai top_idx masih -1, fungsi akan mengembalikan nilai True (kosong), jika tidak maka False.)

def is_full(self): (Fungsi yang digunakan untuk mengecek apakah tumpukan sudah penuh)

return self.top_idx == self.MAX - 1 (indeks array dimulai dari 0, stack akan penuh jika top_idx sudah mencapai nilai max_size - 1 (misal kapasitas 100, maka indeks penuhnya adalah 99). Mengembalikan True jika penuh.)

def push(self, x): (Fungsi push menerima satu parameter x, yaitu data yang ingin dimasukkan)

if self.is_full(): (Melakukan validasi terlebih dahulu dan Mengecek kondisi apakah tumpukan sudah penuh)

print("Stack penuh") (Jika penuh, program mencetak pesan peringatan ke layar.)

return (Keluar dari metode tanpa melakukan tindakan apa pun (mencegah stack overflow)

self.top_idx += 1 (Jika tidak penuh, geser penunjuk indeks teratas naik 1 tingkat ke atas untuk menempati slot kosong berikutnya.)

self.st[self.top_idx] = x (Masukkan data x ke dalam array self.st pada posisi indeks top_idx yang baru.

print(f"Push {x} berhasil") (Mencetak pesan konfirmasi bahwa data sukses ditambahkan.)

def pop(self): (Fungsi pop untuk mengambil elemen teratas.)

if self.is_empty(): (Melakukan validasi terlebih dahulu. Apakah tumpukannya kosong?)

print("Stack kosong") (Jika kosong, program mencetak pesan bahwa tidak ada data yang bisa diambil.)

return (Keluar dari metode (mencegah pencarian indeks negatif yang salah atau stack underflow).

print(f"Pop {self.st[self.top_idx]} berhasil") (Menampilkan data yang berada di posisi paling atas (self.top_idx) ke layar sebelum data tersebut "dihapus")

self.top_idx -= 1 (Logika penghapusannya cukup dengan menurunkan nilai indeks top_idx sebanyak 1. Secara otomatis, elemen yang tadinya di atas tidak lagi dianggap sebagai bagian dari stack, dan posisinya siap ditimpa jika ada operasi push berikutnya.)

def peek(self): (Deklarasi fungsi bernama peek.)

if self.is_empty(): Memeriksa kondisi tumpukan terlebih dahulu menggunakan fungsi is_empty().

print("Stack kosong") (Jika tumpukan kosong, program menampilkan pesan peringatan karena tidak ada elemen yang bisa dilihat.)

return (Keluar dari metode agar kode di bawahnya tidak dieksekusi.)

print(f"Elemen teratas: {self.st[self.top_idx]}") (Jika tidak kosong, program akan mencetak nilai yang berada pada indeks paling atas (self.top_idx) tanpa mengubah posisi penunjuk indeks tersebut.)

def display(self): (deklarasi fungsi bernama display)

if self.is_empty(): (Validasi untuk mengecek apakah tumpukan dalam keadaan kosong.)

print("Stack kosong") (Jika terbukti kosong, program mencetak pesan pemberitahuan.)

return (Langsung keluar dari metode.)

print("Isi stack (atas ke bawah): ", end="") (Mencetak teks judul sebelum menampilkan data. Parameter end="" digunakan agar baris cetakan berikutnya menyambung di baris yang sama (tidak membuat baris baru).

for i in range(self.top_idx, -1, -1): (Melakukan perulangan (looping) mundur. Perulangan dimulai dari indeks teratas (self.top_idx), berjalan mundur mendekati -1 (berhenti di indeks 0), dengan langkah surut sebesar -1. Ini dilakukan demi mematuhi konsep LIFO (menampilkan dari yang paling atas dulu).)

print(self.st[i], end=" ") (Mencetak elemen tumpukan pada indeks ke-i diikuti dengan spasi, sehingga semua elemen tercetak berjejer ke samping dalam satu baris.)

print() (Mencetak baris baru kosong setelah perulangan selesai, agar tampilan menu selanjutnya tidak berantakan.)

def main(): (Deklarasi fungsi utama bernama main().)

stack = StackArray() (Membuat objek (instansiasi) baru dari kelas StackArray dan menyimpannya dalam variabel stack. Karena tidak ada angka di dalam kurung, objek ini otomatis menggunakan ukuran default (100 elemen).)

pilih = 0 (Menginisialisasi variabel pilih dengan nilai awal 0 untuk menyimpan angka menu yang diinput oleh pengguna nanti.)

while pilih != 5: (Membuat perulangan blok menu. Selama pengguna tidak memilih angka 5 (Keluar), menu di bawahnya akan terus ditampilkan berulang-ulang.)

 print("\n=== STACK (Array) ===")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Tampilkan")
        print("5. Keluar") (Mencetak teks judul antarmuka dan daftar pilihan operasi (Push, Pop, Peek, Tampilkan, Keluar) ke layar pengguna. Variabel \n di baris 48 berfungsi untuk memberi jarak satu baris kosong di bagian atas sebelum judul menu dicetak.)

try: (Ini digunakan sebagai antisipasi agar program tidak crash atau error secara mendadap jika pengguna tidak sengaja memasukkan input berupa huruf/karakter saat program meminta input angka.)

pilih = int(input("Pilih: "))
Program meminta input dari pengguna, lalu fungsi int() akan langsung mengubah teks input tersebut menjadi tipe data bilangan bulat (integer) untuk disimpan ke variabel pilih.

except ValueError:
Jika pengguna memasukkan input yang bukan angka (misalnya huruf atau simbol), fungsi int() di baris sebelumnya akan memicu ValueError. Baris ini bertugas menangkap error tersebut.

print("Input tidak valid!")
Memberitahu pengguna lewat layar bahwa input yang mereka masukkan salah/bukan angka baku.

continue
Memaksa program untuk langsung melompat kembali ke awal perulangan while (kembali menampilkan menu), mengabaikan semua baris kode pengecekan menu di bawahnya.

if pilih == 1:
Jika pengguna memilih menu angka 1 (Push / Tambah Data).

try:
Membuka blok pengaman error baru khusus untuk proses input data buku

val = str(input("Nama Buku: "))
Meminta input nama buku dari pengguna dan memastikannya bertipe string lewat fungsi str(), lalu disimpan di variabel val.

stack.push(val)
Memanggil metode push dari objek stack untuk memasukkan nama buku (val) ke tumpukan.

except ValueError:
Mengantisipasi jika terjadi kesalahan konversi tipe data saat input nama buku.

print("Input tidak valid!")
Menampilkan pesan galat jika proses input gagal.

elif pilih == 2:
Jika pengguna memilih menu angka 2 (Pop / Hapus Data Teratas).

stack.pop()
Memanggil fungsi pop() untuk mengeluarkan dan menghapus elemen paling atas dari tumpukan.

elif pilih == 3:
Jika pengguna memilih menu angka 3 (Peek / Mengintip Data Teratas).

elif pilih == 3:
Jika pengguna memilih menu angka 3 (Peek / Mengintip Data Teratas).

elif pilih == 4:
Jika pengguna memilih menu angka 4 (Tampilkan seluruh tumpukan).

stack.display()
Memanggil fungsi display() untuk mencetak daftar buku dari posisi teratas hingga terbawah.

elif pilih == 5:
Jika pengguna memilih menu angka 5 (Keluar dari program).

print("Program selesai.")
Mencetak pesan penutup ke layar. Karena nilai pilih sekarang berubah menjadi 5, kondisi while pilih != 5 di baris sebelumnya akan bernilai salah, sehingga perulangan otomatis berhenti.

else:
Jika angka yang dimasukkan pengguna berupa integer tetapi tidak ada di daftar menu (misalnya memasukkan angka 7 atau -1).

print("Pilihan tidak valid!")
Menampilkan pesan bahwa angka menu tersebut tidak tersedia.

if __name__ == "__main__":
Kondisi ini memeriksa apakah file skrip Python ini sedang dijalankan secara langsung (sebagai program utama), bukan sedang diimpor (import) sebagai modul oleh file skrip lain.

main()
Jika terbukti dijalankan langsung, baris ini memanggil fungsi main(). Di sinilah seluruh rangkaian logika menu interaktif tumpukan buku di atas mulai berputar dan bekerja

**Output**

<img width="718" height="408" alt="output 1" src="https://github.com/user-attachments/assets/020bbd38-cd95-4006-932c-59dafddac690" />

<img width="459" height="317" alt="output2" src="https://github.com/user-attachments/assets/c0002f68-7d62-4f39-ba69-49d529f127df" />

<img width="450" height="160" alt="output 3" src="https://github.com/user-attachments/assets/bdf70223-45fc-4e83-8aed-1e426ca14bfb" />

Saat program berjalan, tumpukan awalnya kosong. Pengguna kemudian memasukkan dua data secara berurutan, yaitu "Buku Logika" dan "Buku Matematika Diskrit". Sesuai prinsip tumpukan, "Buku Matematika Diskrit" sebagai data terbaru otomatis berada di posisi paling atas, tepat di atas "Buku Logika".

Ketika pengguna memilih menu untuk menghapus data, program akan mengeluarkan "Buku Matematika Diskrit" terlebih dahulu karena posisinya yang paling atas. Setelah itu, tumpukan menyisakan "Buku Logika", yang kemudian langsung dikeluarkan juga saat pengguna melakukan penghapusan untuk kedua kalinya.

Pada akhirnya, ketika pengguna mencoba menampilkan seluruh isi tumpukan, semua data telah habis terhapus sehingga program mendeteksi array dalam keadaan bersih dan menampilkan pesan bahwa tumpukan sudah kosong.
