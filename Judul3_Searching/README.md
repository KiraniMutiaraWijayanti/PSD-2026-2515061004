**Program Pencarian Nama Karyawan Untuk Verifikasi Kehadiran**

**Deskripsi Singkat**

Program ini dibuat untuk mengecek data kehadiran karyawan dalam sebuah kantor. Program ini tidak hanya memberi tahu apakah orang tersebut ada di lokasi, tapi juga bisa menghitung sudah berapa kali dia menempelkan kartu absennya ke mesin pemindai. Hal ini berguna untuk memantau jika ada karyawan yang melakukan tapping lebih dari sekali.

Program ini menggunakan algoritma Sequential Search (Pencarian Berurutan) untuk memindai list data. Keunikan dari kode ini adalah ia tidak langsung berhenti saat menemukan nama, melainkan terus mencari hingga akhir list untuk menghitung total kemunculan nama tersebut (counter), yang direpresentasikan sebagai jumlah tapping absen dalam satu hari.

Source Kode

<img width="710" height="501" alt="kode 1" src="https://github.com/user-attachments/assets/6a389415-a19c-4497-9e7d-ba5de3e25879" />

<img width="753" height="247" alt="kode 2" src="https://github.com/user-attachments/assets/3288b9d6-7b71-42c9-ac75-e8a9c6c25e22" />

def sequential_search(data, n, target):
Fungsi ini bernama sequential_search yang menerima tiga parameter yaitu data, jumlah total data (n), dan nama yang ingin dicari (target).

i = 0
variabel i sebagai penanda indeks atau urutan. Kita mulai dari angka 0 karena dalam pemrograman, daftar selalu dihitung dari urutan ke-0.

counter = 0
Variabel ini berfungsi sebagai penghitung. Setiap kali nama yang dicari ditemukan, angka di sini akan bertambah.

while i < n:
Kode ini meminta pengulangan. Selama posisi kita (i) belum melewati total jumlah data (n), program akan terus mengecek daftar tersebut.

if data[i] == target:
Kode melakukan pengecekan. Program membandingkan nama pada urutan ke-i dalam daftar dengan nama yang kita cari.

counter += 1
Jika namanya cocok, maka jumlah temuan (counter) ditambah 1.

i += 1
Setelah mengecek satu nama, program pindah ke urutan berikutnya agar program tidak berhenti di situ saja.

return counter
Setelah semua daftar dicek, fungsi ini mengembalikan total jumlah temuan kepada program utama.

Program Utama (main)
data = ["Andi", "Budi", ..., "Lia"]
kode ini tempat penyimpanan data nama-nama karyawan yang sudah absen hari ini.

n = len(data)
Program menghitung berapa banyak total nama yang ada di dalam daftar tadi secara otomatis.

while True:
Baris ini menciptakan pengulangan tanpa henti yang bertujuan untuk memastikan pengguna memasukkan input dengan benar.

target = input("\nMasukkan NAMA karyawan yang ingin dicari: ")
Program berhenti sejenak untuk meminta kamu mengetikkan nama karyawan yang ingin dicari informasinya.

if target: break
Logika ini memastikan bahwa jika kamu memasukkan nama (tidak membiarkannya kosong), program akan keluar dari pengulangan dan lanjut ke tahap berikutnya.

counter = sequential_search(data, n, target)
program memanggil fungsi pencarian yang kita bahas di Bagian 1 tadi untuk mulai bekerja mencari nama yang kamu ketik.

if counter > 0:
Program melakukan pengecekan terakhir. Jika jumlah temuan lebih dari 0, berarti karyawan tersebut ada dalam catatan.

else:
Jika jumlahnya tetap 0 setelah dicari ke seluruh daftar, program akan menginfokan bahwa nama tersebut memang tidak ada atau belum melakukan absen.

if __name__ == "__main__":
Baris standar Python ini memastikan bahwa program akan langsung berjalan otomatis ketika file ini dibuka.

**Output**

<img width="721" height="133" alt="output 1" src="https://github.com/user-attachments/assets/4f90ee35-7b59-47b2-ad7c-27c8efebdd02" />

<img width="721" height="133" alt="output 1" src="https://github.com/user-attachments/assets/622ba39a-1e8e-41ce-af2b-827dee3f7a80" />

Saat kode coba di run maka user diminta untuk memasukkan nama karyawan yang akan di cek kehadirannya. Seperti pada output user mencoba mengecek nama Dewi, Maka program akan menampilkan Karyawan Dewi ditemukan 1 sekali yang artinya Dewi telah melakukan tapping absen dalam sehari.

https://youtu.be/sDE-hgGKzdo










