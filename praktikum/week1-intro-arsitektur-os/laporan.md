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
