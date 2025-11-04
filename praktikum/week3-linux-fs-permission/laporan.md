
# Laporan Praktikum Minggu [3]
Topik: [Manajemen File dan Permission di Linux]

---

## Identitas
- **Nama**  : [Latifah Risti Anggraeni]  
- **NIM**   : [250202945]  
- **Kelas** : [1IKRB]

---

## Tujuan
1. Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
2. Menggunakan chmod dan chown untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori

### 1. Sistem Berkas Linux
Semua data tersimpan dalam struktur hierarki dimulai dari `/` (root).  
Direktori penting:
- `/home` → data pengguna  
- `/etc` → konfigurasi sistem  
- `/tmp` → file sementara  

### 2. Navigasi Sistem File
Perintah dasar:
- `pwd` → menampilkan direktori aktif  
- `ls` → melihat isi folder  
- `cd` → berpindah direktori  
- `cat` → membaca isi file  

### 3. Permission (Hak Akses)
Menentukan siapa yang bisa membaca, menulis, atau mengeksekusi file.  
Contoh:
- `rwx` → owner (read, write, execute)  
- `r-x` → group (read, execute)  
- `r--` → others (read only)

### 4. Ownership (Kepemilikan)
Setiap file punya **user** (pemilik) dan **group**.  
Perintah:  
- `chown` → ubah pemilik file  
- `chmod` → ubah hak akses file  

### 5. Peran chmod & chown
- `chmod` menjaga file agar hanya bisa diakses sesuai izin.  
- `chown` memastikan file dimiliki oleh user yang berwenang.  
Keduanya penting untuk **keamanan dan kontrol akses** di sistem Linux.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```

---

## Kode / Perintah
```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```

```bash
   cat /etc/passwd | head -n 5
   ```

```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```

---

## Hasil Eksekusi
![Screenshot hasil](screenshots/praktikum3.png)

---

## Analisis

## Eksperimen 1
- **Direktori aktif** ada dibagian `/home/latifah181rr`
- **Isi folder** ada dibagian `percobaan.txt`, `praktikum/`, `README-cloudshell.txt`
- **File tersembunyi** ada dibagian `.` dan `..`

Perintah `pwd`, `ls`, `cd`, dan `ls -a` biasanya digunakan untuk menavigasi sistem file dan menampilkan isi direktori, termasuk file tersembunyi.

---

## Eksperimen 2
- **Perintahnya** `cat /etc/passwd | head -n 5`
- Untuk **Isi file** berisi data pengguna sistem (user account list)
- **Struktur baris**  
  `username:password:UID:GID:comment:home:shell`
- **Contoh:**  
  `root:x:0:0:root:/root:/bin/bash` 

File `/etc/passwd` menyimpan informasi dasar setiap user, termasuk direktori home dan shell yang digunakan.

---

## Eksperimen 3 
Pada eksperimen ini dibuat sebuah file baru bernama `percobaan.txt` menggunakan perintah:

```bash
echo "Hello Latifah181RR" > percobaan.txt
````

File tersebut awalnya memiliki izin akses:

```
-rw-rw-r--
```

Artinya **pemilik** dan **grup** dapat membaca serta menulis file, sedangkan **pengguna lain** hanya bisa membacanya.

Kemudian dijalankan perintah berikut untuk mengubah hak akses file:

```bash
chmod 600 percobaan.txt
```

Setelah perintah ini dijalankan, permission file berubah menjadi:

```
-rw-------
```

Perubahan ini membuat file hanya bisa **dibaca dan ditulis oleh pemiliknya**, sedangkan pengguna lain tidak memiliki akses sama sekali. Sehingga file lebih aman dan bersifat privat.

Selanjutnya, dilakukan perubahan kepemilikan file dengan perintah:

```bash
sudo chown root percobaan.txt
```

Hasilnya, kepemilikan file berpindah dari user `latifah181rr` menjadi `root`, namun hak aksesnya tetap sama (`-rw-------`).
Perubahan ini menunjukkan bahwa hanya **user root (administrator)** yang memiliki kontrol penuh atas file tersebut.

`chmod` mengatur hak akses file, sedangkan `chown` mengubah kepemilikan file. Keduanya berperan penting dalam menjaga keamanan dan kontrol akses pada sistem Linux.


---

## Kesimpulan
Praktikum ini mengajarkan bahwa:

1. Sistem file Linux memiliki struktur hierarki yang jelas.
2. File memiliki izin akses dan kepemilikan yang dapat diatur untuk menjaga keamanan.
3. Perintah chmod dan chown berperan penting dalam pengelolaan hak akses file.
4. Dokumentasi serta penggunaan Git menjadi bagian penting dari workflow praktikum berbasis sistem operasi.

Secara keseluruhan kami dapat memahami cara mengelola file, direktori, hak akses, dan kepemilikan dalam Linux serta pentingnya menjaga keamanan sistem melalui pengaturan permission dan ownership yang tepat.

---

## Tugas
# Tabel Observasi
|  No | Perintah                                   | Hasil                                                          | Fungsi Perintah                                |
 :-: | :----------------------------------------- | :--------------------------------------------------------------------------------- | :--------------------------------------------- |
|  1  | `pwd`                                      | `/home/latifah181rr`                                                               | Menampilkan direktori aktif saat ini           |
|  2  | `ls -l`                                    | Menampilkan daftar file lengkap (dengan izin, owner, group, ukuran, tanggal, nama) | Melihat isi direktori secara detail            |
|  3  | `cd /tmp`                                  | Berpindah ke direktori `/tmp`                                                      | Navigasi ke folder sementara sistem            |
|  4  | `ls -a`                                    | Menampilkan semua file termasuk tersembunyi (`.`, `..`)                            | Melihat seluruh isi direktori                  |
|  5  |`cat /etc/passwd`                          | `head -n 5`                                                                         | Menampilkan 5 baris pertama dari `/etc/passwd` |
|  6  | `echo "Hello <NAME><NIM>" > percobaan.txt` | Membuat file teks berisi kalimat tersebut                                          | Membuat file baru dengan konten tertentu       |
|  7  | `ls -l percobaan.txt`                      | `-rw-rw-r--`                                                                       | Menampilkan detail izin dan kepemilikan file   |
|  8  | `chmod 600 percobaan.txt`                  | Mengubah izin file jadi `rw-------`                                                | Memberikan akses hanya untuk pemilik file      |
|  9  | `sudo chown root percobaan.txt`            | Owner berubah menjadi `root`                                                       | Mengubah pemilik file                          |

---

## Fungsi tiap perintah dan arti kolom permission (`rwxr-xr--`)
Penjelasan setiap simbol dari perintah `rwxr-xr--`:

1. **r** (read) artinya izin membaca isi file atau daftar direktori.
2. **w** (write) artinya izin mengubah isi file atau menambah/menghapus file dalam direktori.
3. **x** (execute) artinya izin menjalankan file atau masuk ke direktori.
4. **-** (strip) artinya tidak memiliki izin tersebut.
   berarti:
   - **owner**: boleh baca, tulis, eksekusi.
   - **group**: boleh baca dan eksekusi.
   - **others**: hanya boleh baca.

---

## Peran `chmod` dan `chown` dalam keamanan sistem Linux.

Perintah `chmod` dan `chown` berperan penting dalam menjaga keamanan sistem Linux. `chmod` digunakan untuk mengatur izin akses agar hanya pengguna tertentu yang dapat membaca, menulis, atau menjalankan file, sedangkan `chown` digunakan untuk mengubah kepemilikan file. Kombinasi keduanya memberikan lapisan keamanan yang kuat, mencegah penyalahgunaan file, serta menjaga integritas dan kerahasiaan data dalam sistem Linux.

---

## Quiz
1. [Apa fungsi dari perintah `chmod`?]  
   **Jawaban:** `chmod` biasanya digunakan untuk mengatur atau mengubah izin akses suatu file atau direktori di sistem operasi Linux.

2. [Apa arti dari kode permission `rwxr-xr--`?]  
   **Jawaban:** Arti tanda pertama menunjukkan jenis file (`-` untuk file biasa dan `d` untuk direktori). Tiga karakter berikutnya menunjukkan izin untuk pemilik (owner), yaitu `rwx` yang berarti dapat membaca, menulis, dan mengeksekusi. Tiga karakter selanjutnya menunjukkan izin untuk grup (group), yaitu `r-x` yang berarti hanya dapat membaca dan mengeksekusi tanpa menulis. Tiga karakter terakhir menunjukkan izin untuk pengguna lain (others), yaitu `r--` yang berarti hanya dapat membaca. Dengan demikian, file berizin `-rwxr-xr--` bisa dijalankan oleh pemilik dan grup, sedangkan pengguna lain hanya dapat membacanya.

3. [Jelaskan perbedaan antara `chown` dan `chmod`.]  
   **Jawaban:** Perbedaannya `chown` dapat mengatur apa yang boleh di lakukan seperti izin sedangkan `chmod` mengatur siapa yang berhak mengatur file tersebut seperti pemegang.

---

## Refleksi Diri
Bagian yang paling menantang pada praktikum minggu ini adalah memahami perubahan permission dan ownership menggunakan perintah `chmod` dan `chown`, terutama dalam membedakan hak akses antara user, group, dan others. Untuk mengatasinya, saya mencoba langsung dengan menjalankan perintah di terminal juga mengamati hasil sebelum dan sesudah perubahan, kemudian membaca dokumentasi dibagian `man chmod` dan `man chown` agar dapat lebih memahami fungsi serta dampak dari setiap opsi yang digunakan.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
