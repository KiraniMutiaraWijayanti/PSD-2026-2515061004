**Program Pengurutan Umur Mahasiswa**

**Deskripsi Singkat**

Program ini dibuat untuk membantu mengelola data umur mahasiswa dengan cara mengurutkannya menggunakan aturan Ascending, dimana data umur mahasiswa diurutkan dari nilai terkecil ke nilai terbesar. Dalam kasus ini, program akan menerima input yang dimasukkan user berupa jumlah mahasiswa dan daftar umur mereka, kemudian memprosesnya agar tersusun rapi.

Algoritma struktur data yang digunakan adalah Insertion Sort. Algoritma ini bekerja dengan cara mengambil satu data yang belum terurut lalu menyisipkannya ke posisi yang tepat pada bagian data yang sudah terurut.

**Source Kode**

<img width="480" height="431" alt="source kode1" src="https://github.com/user-attachments/assets/5ba92919-7bd1-486e-a525-b19fd24ab02c" />

<img width="402" height="147" alt="source kode2" src="https://github.com/user-attachments/assets/359f5290-ed39-4106-91f4-c8e6fa80a942" />

Baris pertama: def insertion_sort(arr, n): untuk mendefinisikan fungsi yang menerima dua parameter, yaitu daftar data (arr) dan jumlah elemen (n)

Baris dua: for i in range(1, n): untuk melakukan perulangan yang di mulai dari indeks ke-1. Algoritma ini menganggap elemen pertama sudah terurut sehingga algoritma ini mulai membandingkan dari elemen kedua.

Baris tiga: temp = arr[i] digunakan untuk menyimpan nilai [i] agar nilai ini tidak ditimpa oleh arr[j] dan bisa digeser jika perlu.

Baris empat: j = i - 1 untuk menentukan indeks j sebagai elemen tepat di sebelah kiri indeks i untuk mulai dibandingkan.

Baris lima: while j >= 0 and arr[j] > temp: digunakan ketika belum mencapai awal daftar (j >= 0) dan nilai kiri di sebelah kiri lebih besar dari nilai temp, maka perulangan berlanjut.

Baris enam: arr[j + 1] = arr[j]: Menggeser nilai yang lebih besar ke posisi sebelah kanan untuk memberi ruang bagi temp.

Baris tujuh: j -= 1: Mengurangi nilai j untuk terus membandingkan dengan elemen-elemen di sebelah kirinya lagi.

Baris delapan: arr[j + 1] = temp: Setelah posisi yang tepat ditemukan (ketika arr[j] tidak lagi lebih besar dari temp), masukkan nilai temp ke posisi tersebut.

Baris sembilan: n = int(input("Masukkan jumlah mahasiswa: ")): Meminta pengguna memasukkan jumlah data yang akan diolah.

Baris sepuluh: except ValueError:: Menangani kesalahan jika pengguna memasukkan teks atau simbol alih-alih angka

Baris sebelas: arr = []: Menyiapkan daftar kosong untuk menyimpan umur mahasiswa.

Baris dua belas: for i in range(n):: Perulangan untuk mengambil input umur sebanyak n kali.

Baris tiga belas: umur = int(input()): Mengambil input angka umur dari pengguna

Baris empat belas: arr.append(umur): Menambahkan angka umur yang valid ke dalam daftar arr.

Baris lima belas: print(f"Umur sebelum diurutkan: {arr}"): Menampilkan daftar umur asli sebelum proses pengurutan.

Baris enam belas: insertion_sort(arr, n): Memanggil fungsi pengurutan yang telah dibuat sebelumnya.

Baris tujuh belas: for i in range(n): print(arr[i], end=" "): Mencetak elemen-elemen di dalam daftar satu per satu secara mendatar setelah berhasil diurutkan.

Baris delapan belas: if __name__ == "__main__": main(): Memastikan fungsi main() dipanggil hanya ketika file ini dijalankan secara langsung


**Output**

<img width="376" height="129" alt="output 1" src="https://github.com/user-attachments/assets/4390388b-2326-4bfb-ae01-3c027df31cd0" />

<img width="400" height="146" alt="output 2" src="https://github.com/user-attachments/assets/a90e5762-4c53-4fec-bd31-d9e4c71993d0" />

<img width="340" height="128" alt="output 3" src="https://github.com/user-attachments/assets/1a1cf6eb-6b0b-49c3-8c97-0269424b0168" />



















