**Program Pengurutan Umur Mahasiswa**

**Deskripsi Singkat**
Program ini dibuat untuk membantu mengelola data umur mahasiswa dengan cara mengurutkannya menggunakan aturan Ascending, dimana data umur mahasiswa diurutkan dari nilai terkecil ke nilai terbesar. Dalam kasus ini, program akan menerima input yang dimasukkan user berupa jumlah mahasiswa dan daftar umur mereka, kemudian memprosesnya agar tersusun rapi.

Algoritma struktur data yang digunakan adalah Insertion Sort. Algoritma ini bekerja dengan cara mengambil satu data yang belum terurut lalu menyisipkannya ke posisi yang tepat pada bagian data yang sudah terurut.

**Source Kode**

<img width="480" height="431" alt="source kode1" src="https://github.com/user-attachments/assets/5ba92919-7bd1-486e-a525-b19fd24ab02c" />

<img width="402" height="147" alt="source kode2" src="https://github.com/user-attachments/assets/359f5290-ed39-4106-91f4-c8e6fa80a942" />

Baris pertama: def insertion_sort(arr, n): untuk mendefinisikan fungsi yang menerima dua parameter, yaitu daftar data (arr) dan jumlah elemen (n)

Baris keduaa: for i in range(1, n): untuk melakukan perulangan yang di mulai dari indeks ke-1. Algoritma ini menganggap elemen pertama sudah terurut sehingga algoritma ini mulai membandingkan dari elemen kedua.

Baris ketiga: temp = arr[i] digunakan untuk menyimpan nilai [i] agar nilai ini tidak ditimpa oleh arr[j] dan bisa digeser jika perlu.

Baris keempat: j = i - 1 untuk menentukan indeks j sebagai elemen tepat di sebelah kiri indeks i untuk mulai dibandingkan.

Baris kelima: while j >= 0 and arr[j] > temp: digunakan ketika belum mencapai awal daftar (j >= 0) dan nilai kiri di sebelah kiri lebih besar dari nilai temp, maka perulangan berlanjut.

Baris keenam: 

































