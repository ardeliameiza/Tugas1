# Tugas 1 - Pengembangan Sistem Backend  
Nama : Ni kadek Ardelia Meiza
Nim : 230030593
Kelas : CB243

Tugas ini mengimplementasikan dua class diagram menggunakan bahasa Python tanpa framework seperti Django atau Flask.  
Setiap studi kasus dibuat dalam folder terpisah dan dijalankan melalui file main.py.  
Tugas ini menerapkan konsep OOP seperti Encapsulation, Inheritance, Polymorphism, dan Abstraction.


## 📂 Struktur Folder

Tugas1/
│
├── StudiKasus1/
│   ├── address.py
│   ├── person.py
│   ├── student.py
│   ├── professor.py
│   └── main.py
│
├── StudiKasus2/
│   ├── author.py
│   ├── book.py
│   ├── libraryitem.py
│   ├── librarymember.py
│   └── main.py
│
└── dokumentasi

Cara Menjalankan Program

Studi Kasus 1

cd StudiKasus1
python main.py

Studi Kasus 2

cd StudiKasus2
python main.py


Studi Kasus 1 – Ringkasan Program

| Class     | Deskripsi                                                                 |
| --------- | ------------------------------------------------------------------------- |
| Address   | Menampung data alamat dan validasi kode pos                               |
| Person    | Class dasar berisi data umum seperti nama, email, dan alamat              |
| Student   | Turunan dari Person, memiliki atribut studentNumber dan averageMark       |
| Professor | Turunan dari Person, memiliki atribut staffNumber, salary, dan supervises |

Fungsi Utama:

✔ Menampilkan informasi mahasiswa dan profesor
✔ Validasi kode pos alamat
✔ Cek eligibility student untuk enroll
✔ Simulasi supervisi oleh professor

Studi Kasus 2 – Ringkasan Program

| Class         | Deskripsi                                             |
| ------------- | ----------------------------------------------------- |
| Author        | Menyimpan identitas penulis                           |
| Book          | Menyimpan informasi buku dan keterkaitannya ke Author |
| LibraryItem   | Item perpustakaan seperti buku/jurnal                 |
| LibraryMember | Anggota perpustakaan yang bisa meminjam item          |

Fungsi Utama:

✔ Menampilkan detail buku dan penulis
✔ Peminjaman dan pengembalian item perpustakaan
✔ Relasi antara LibraryMember dan LibraryItem

Konsep OOP yang Diterapkan

| Konsep OOP    | Implementasi                                     |
| ------------- | ------------------------------------------------ |
| Encapsulation | Atribut dibuat privat dan diakses melalui method |
| Inheritance   | Student dan Professor mewarisi dari Person       |
| Polymorphism  | Method showInfo() di-override oleh subclass    |
| Abstraction   | Pemisahan logika dalam class modular             |
| Modularitas   | Pemisahan setiap class dalam file terpisah       |

Dokumentasi Penggunaan AI (Prompt–Response)

**Prompt 1:**
*Bantu saya membenarkan error yang terjadi*

**Response (AI):**
AI memberikan beberapa arahan tentang huruf besar dan huruf kecil yang berpengaruh

**Prompt 2:**
*Bagaimana cara membuat README.md rapi sesuai instruksi tugas?*

**Response (AI):**
AI memberikan template README lengkap berisi identitas, struktur folder, cara menjalankan, dokumentasi OOP, dan prompt-response.

> Awalnya program saya tidak bisa jalan karena error import dan file tidak terbaca. Setelah diskusi dengan AI, saya paham bahwa Python sensitif terhadap nama file, struktur folder, dan huruf besar-kecil. Dari sini saya merasa paham lebih dalam konsep OOP dan project struktur.

dokumentasi(ss) ada di folder dokumentasi

Melalui tugas ini, saya memahami:
✔ Cara mengimplementasikan OOP dalam Python
✔ Cara menjalankan program menggunakan entry point main.py
✔ Cara mendokumentasikan kode dan membuat README.md
