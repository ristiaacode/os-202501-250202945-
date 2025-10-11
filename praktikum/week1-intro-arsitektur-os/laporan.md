
# Laporan Praktikum Minggu [1]
Topik: [Arsitektur Sistem Operasi dan Kernel]

---

## Identitas
- **Nama**  : [Latifah Risti Anggraeni]  
- **NIM**   : [250202945]  
- **Kelas** : [1IKRB]

---

## Tujuan 
> Menjelaskan peran sistem operasi dalam arsitektur komputer.
> Mengidentifikasi komponen utama OS (kernel, system call, device driver, file system).
> Membandingkan model arsitektur OS (monolithic, layered, microkernel).
> Menggambarkan diagram sederhana arsitektur OS menggunakan alat bantu digital (draw.io / mermaid).


---

## Dasar Teori
1. **Sistem Operasi (OS)** adalah perangkat lunak yang berperan sebagai penghubung antara pengguna dan perangkat keras komputer.
2. **Kernel** merupakan inti dari OS yang mengatur proses, memori, file system, dan perangkat keras agar berjalan efisien.
3. **System Call Interface** menjadi jembatan antara aplikasi pengguna dan kernel untuk meminta layanan sistem (misal: membaca file, alokasi memori).
4. **Arsitektur OS** dibedakan menjadi:
   - **Monolithic Kernel**: cepat, tapi risiko tinggi jika crash.
   - **Microkernel**: lebih aman dan stabil, namun sedikit lebih lambat.
   - **Layered Architecture**: modular dan mudah dipelihara.
5. **Perintah seperti `uname`, `lsmod`, dan `dmesg`** digunakan untuk menampilkan informasi kernel, modul, serta pesan aktivitas sistem operasi.

---

## Langkah Praktikum
1. Buka terminal pada sistem operasi Linux.
2. Jalankan perintah `uname -a` untuk melihat versi kernel dan detail sistem.
3. Gunakan `lsmod` | head untuk menampilkan daftar modul kernel yang sedang aktif.
4. Jalankan `dmesg` | head untuk melihat log awal pesan dari kernel.
5. Simpan hasil eksekusi ke dalam file teks untuk dokumentasi.
6. Lakukan commit dan push hasil ke repository GitHub.
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi


---

## Analisis
-Perintah `uname -a` menampilkan informasi kernel seperti versi, arsitektur, dan nama host. Ini menunjukkan bahwa sistem berjalan di atas kernel Linux versi tertentu.
-`lsmod` menunjukkan modul-modul kernel yang dimuat untuk mendukung perangkat keras atau fungsi sistem, seperti jaringan atau penyimpanan.
-`dmesg` menampilkan pesan dari kernel saat sistem booting, termasuk deteksi perangkat keras dan inisialisasi driver.
-Hasil ini menunjukkan bagaimana kernel berfungsi sebagai penghubung utama antara perangkat lunak dan perangkat keras, serta bagaimana sistem call memungkinkan komunikasi antar lapisan seperti di diagram arsitektur OS.
-Jika percobaan dilakukan di Windows, hasilnya berbeda karena sistem operasi tersebut tidak menyediakan akses langsung ke kernel lewat terminal seperti Linux; akses dilakukan melalui PowerShell atau Event Viewer yang sifatnya lebih terbatas.
---

## Kesimpulan
Kernel adalah inti sistem operasi yang berfungsi mengatur semua sumber daya komputer.
Dari hasil percobaan, perintah `uname`, `lsmod`, dan `dmesg` membantu memahami bagaimana kernel bekerja di level rendah.
Struktur Monolithic Kernel seperti pada Linux masih paling umum digunakan dalam sistem modern karena kinerjanya tinggi dan kompatibilitas luas, meskipun sistem hybrid dan modular kini makin banyak diadaptasi.
---

## Tugas
# Laporan Praktikum Minggu 1  
## Arsitektur Sistem Operasi

### Perbedaan untuk Monolithic Kernel, Microkernel, dan Layered Architecture

Monolithic Kernel merupakan arsitektur sistem operasi yang di mana hampir seluruhnya berkomponen inti seperti device drivers, file system, memory management, dan layanan sistem lainnya dengan cara dijalankan pada sebuah ruang kernel yang besar. Untuk keunggulan utamanya berada diperforma yang tinggi karena seluruh layanan ikut bekerja langsung didalam ruang kernel tanpa banyaknya overhead saat berkomunikasi antarproses. Permintaan layanan dapat diubah secara langsung, sehingga operasi sistem menjadi lebih efisien dan responsif. Hal ini membuat model monolitik cocok untuk sistem yang membutuhkan kinerja cepat dan beban kerja intensif I/O.  

Namun, kelemahannya adalah risiko stabilitas. Karena banyak komponen berjalan di ruang kernel, kerusakan satu modul dapat menyebabkan crash pada seluruh sistem. Proses pemeliharaan dan pembaruan lebih sulit karena integrasi antar komponennya sangat erat. Meskipun konsep desainnya sederhana, implementasinya tetap kompleks. Linux, Unix klasik, dan MS-DOS merupakan sistem operasi dengan model monolitik.

Microkernel memiliki pendekatan yang lebih minimalis. Hanya fungsi inti seperti manajemen memori dasar dan interprocess communication (IPC) yang ditempatkan di dalam kernel. Komponen lain seperti driver, sistem berkas, dan jaringan dijalankan di user space. Stabilitas dan keamanan yang lebih tinggi karena adanya isolasi antar layanan merupakan keunggulan dari model ini. Apabila salah satu komponen gagal, maka tidak akan langsung berdampak kepada kernel inti.  

Tetapi, microkernel memiliki kinerja yang lebih rendah dibandingkan monolitik sebab setiap interaksi antar layanan diperlukan komunikasi melalui mekanisme message passing atau IPC. Kompleksitas desainnya juga tinggi, sebab memerlukan koordinasi antarkomponen yang berjalan secara terpisah. Sistem operasi yang menggunakan pendekatan ini antara lain Minix, QNX, dan versi hybrid dari macOS.

Layered Architecture membagi sistem operasi ke dalam beberapa lapisan (layers), di mana setiap lapisan memiliki tanggung jawab khusus dan hanya berinteraksi dengan lapisan di atas atau di bawahnya. Struktur ini memberikan modularitas dan kemudahan pemeliharaan yang lebih baik karena perubahan pada satu lapisan tidak langsung memengaruhi lapisan lainnya. Keamanan juga meningkat berkat isolasi fungsi antarlapisan.  

Meski begitu, jika jumlah lapisan terlalu banyak atau desain antarmukanya tidak efisien, kinerja sistem dapat menurun dan pengembangannya menjadi lebih kompleks. Contoh sistem operasi dengan model ini adalah THE OS dan MULTICS.

---

### Beberapa Analisis Umum

**Performa vs Modularitas:** Monolithic Kernel unggul dalam performa, tetapi kurang modular dan berisiko tinggi terhadap kegagalan. Microkernel menonjolkan modularitas dan keamanan dengan sedikit pengorbanan performa. Layered Architecture mencoba menyeimbangkan keduanya melalui struktur berlapis.  

**Keamanan dan Stabilitas:** Microkernel paling kuat dalam isolasi kegagalan, Monolithic Kernel rentan terhadap kerusakan lintas komponen, sementara Layered Architecture bergantung pada batasan lapisan untuk menjaga keamanan.  

**Contoh Sistem:** Linux/Unix (Monolithic), Minix/QNX (Microkernel), dan THE OS/MULTICS (Layered).

---

### Model yang Paling Relevan untuk Sistem Modern

Model yang paling relevan untuk sistem operasi modern adalah Hybrid Kernel, dengan konsep Monolithic Kernel dan Microkernel yang di gabungkan. Kedua model ini mengombinasikan kinerja tinggi dari kernel monolitik dengan keamanan dan modularitas dari microkernel.  

Dalam sistem modern seperti Windows NT, macOS (XNU), dan Android (Linux kernel yang dimodifikasi), pendekatan hybrid digunakan agar sistem tetap cepat namun juga lebih stabil dan aman. Komponen penting seperti manajemen memori dan proses tetap berada di ruang kernel untuk efisiensi, sementara layanan non-esensial seperti device driver tertentu, file system tambahan, atau layanan jaringan berjalan di user space agar lebih mudah diperbarui dan tidak merusak sistem inti bila terjadi kegagalan.  

Selain itu, arsitektur hybrid lebih mudah dikembangkan untuk teknologi baru seperti virtualisasi, cloud computing, dan containerization (Docker, Kubernetes) karena struktur modularnya mendukung isolasi proses dan efisiensi sumber daya. 

---

## Quiz
1. [Sebutkan tiga fungsi utama sistem operasi!]  
   **Jawaban:**  Mengatur sumber daya komputer (CPU, memori, I/O), mengelola proses dan multitasking, mengatur file serta komunikasi perangkat I/O.
2. [Jelaskan perbedaan antara kernel mode dan user mode!]  
   **Jawaban:**  Untuk Kernel mode hak aksesnya penuh dengan tujuan menjalankan fungsi inti OS sedangkan User mode haknya terbatas, tujuannya menjalankan aplikasi pengguna.
3. [Sebutkan contoh OS dengan arsitektur monolithic dan microkernel!]  
   **Jawaban:**  Untuk Monolithic terdapat Linux, Unix, MS-DOS dan Microkernel terdapat Minix, QNX, macOS (hybrid).

---

## Refleksi Diri
Saya belajar tentang perbedaan arsitektur Monolithic Kernel, Microkernel, dan Layered Architecture, serta bagaimana masing-masing memiliki kelebihan dan kekurangan dalam hal kinerja, keamanan, dan modularitas.

Kesulitan terdapat pada memahami cara kerja setiap arsitektur secara teknis, terutama bagaimana komponen saling berinteraksi di dalam kernel.

Cara menyelesaikannya adalah dengan membaca ulang materi, mencari ilustrasi diagram arsitektur dari berbagai sumber, serta membandingkan contoh sistem operasi nyata agar lebih mudah memahami konsep dan perbedaannya.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
