"""
==========================================================
PROJECT : Student Information Exchange System
FILE    : main.py
==========================================================

TUJUAN PROJECT
--------------
Project ini dibuat untuk memahami bagaimana Python
berkomunikasi dengan dunia luar menggunakan JSON.

Alur project:

Python Object
      ↓
Convert menjadi JSON
      ↓
Simpan ke file JSON
      ↓
Baca kembali file JSON
      ↓
Convert menjadi Python Object
      ↓
Tampilkan hasil

Catatan:
Pada tahap ini kita baru sampai pada proses
mengubah Python Object menjadi JSON String.
"""

# ==========================================================
# TAHAP 0 — IMPORT MODULE
# ==========================================================
# Business Rule
 # Program membutuhkan kemampuan untuk mengubah object Python menjadi JSON.
# Mengapa menggunakan module json?
 # Karena Python tidak bisa mengubah object menjadi JSON secara otomatis.
 # Module json adalah module bawaan Python (built-in module) yang menyediakan fungsi-fungsi untuk bekerja dengan JSON.
# Mengapa import ditempatkan paling atas?
 # Sesuai praktik standar Python (PEP 8), seluruh import ditempatkan di bagian atas file 
 # agar programmer langsung mengetahui dependency yang digunakan program.
import json

# ==========================================================
# TAHAP 1 — MEMBUAT DATA MAHASISWA
# ==========================================================
# Tujuan:
 # Menyiapkan data yang nantinya akan dikonversi menjadi JSON.

# Mengapa ditempatkan di awal?
 # Karena semua proses berikutnya (convert JSON, simpan file, baca file) 
 # membutuhkan data ini terlebih dahulu.
 # Python mengeksekusi program dari atas ke bawah.

# Variabel 'students' digunakan untuk menyimpan seluruh data mahasiswa.
# Mengapa menggunakan nama 'students' (jamak)?
 # Karena data yang disimpan lebih dari satu mahasiswa.

# Mengapa menggunakan List []?
 # Karena kita memiliki kumpulan (collection) mahasiswa.
 # List cocok digunakan untuk menyimpan banyak data yang sejenis.
students = [

    # ------------------------------------------------------
    # Mahasiswa pertama

    # Mengapa menggunakan Dictionary {}?
     # Karena satu mahasiswa memiliki beberapa atribut
     # (nama, umur, jurusan, IPK, status aktif).
     # Dictionary memungkinkan setiap nilai memiliki identitas (key), sehingga data lebih mudah dipahami.
    # ------------------------------------------------------
    {
        "name": "Raquel",
        "age": 20,
        "major": "Informatics",
        "gpa": 3.75,
        "is_active": True
    },

    # Mahasiswa kedua
    {
        "name": "Anton",
        "age": 21,
        "major": "AI Engineering",
        "gpa": 3.25,
        "is_active": True
    },

    # Mahasiswa ketiga
    {
        "name": "Joxra",
        "age": 21,
        "major": "Data Science",
        "gpa": 3.51,
        "is_active": True
    }

]


# ==========================================================
# TAHAP 2 — CONVERT PYTHON OBJECT MENJADI JSON STRING
# ==========================================================
# Business Rule
 # Data mahasiswa harus diubah menjadi JSON.

# Mengapa?
 # Karena:
 # - File JSON menyimpan teks.
 # - API menerima JSON.
 # - Webhook mengirim JSON.
 # - OpenAI menerima JSON.
 #Semua proses tersebut membutuhkan JSON, bukan object Python.

# Mengapa menggunakan json.dumps()?
 # dump  = menuangkan / mengubah
 # s     = string
# Artinya: "Ubah object Python menjadi STRING JSON."

json_data = json.dumps(
    students,
    indent=4
#Kenapa indent=4?
 #agar tampilan datanya jauh lebih rapih.

# Posisi kode
 # Diletakkan setelah variabel students, karena json.dumps() membutuhkan object students.

)

# ==========================================================
# TAHAP 3 — VERIFIKASI
# ==========================================================
# Business Rule
 # Sebelum melanjutkan ke tahap penyimpanan file, kita harus memastikan bahwa proses konversi berhasil.

# Mengapa perlu verifikasi?
 # Programmer tidak boleh berasumsi.
# Kita harus membuktikan:
 # students  -> masih List
 # json_data -> sudah String
 # Verifikasi seperti ini merupakan kebiasaan yang sangat baik saat belajar maupun debugging.

# Posisi kode
 # Diletakkan setelah json.dumps(), karena variabel json_data baru dibuat pada tahap sebelumnya.

print("=" * 60)
print("VERIFIKASI TIPE DATA")
print("=" * 60)

print(f"Tipe students  : {type(students)}")
print(f"Tipe json_data : {type(json_data)}")

print()

print("=" * 60)
print("HASIL JSON")
print("=" * 60)

print(json_data)

# ==========================================================
# TAHAP 4 — MENYIMPAN/MENULIS DATA KE FILE JSON
# ==========================================================
# Business Rule
 # Data mahasiswa harus disimpan ke file student.json agar tetap ada meskipun program selesai dijalankan.

 #Sebelum tahap ini, data masih tersimpan di terminal belum ke file JSON.

# Mengapa menggunakan with open(...)?
 # Python harus membuka file (json) sebelum dapat menulis data.
 # "with" memastikan file akan ditutup secara otomatis, bahkan jika terjadi error.
 #analoginya seperti: ketika anda ingin menulis di buku. Anda harus membuka buku -> menulis -> menutup buku. Demikan juga dengan python.

# Mengapa mode "w"?
 # "w" berarti write (menulis).

# Jika file belum ada:
 # → Python akan membuat file baru.

# Jika file sudah ada:
 # → Isi file (JSON) lama akan diganti dengan data baru.

# Mengapa menggunakan json.dump()?
 # Karena tujuan kita sekarang adalah menulis/menyimpan object Python disini langsung ke file JSON.

# Posisi kode
 # Diletakkan setelah data berhasil dibuat.
 # Program harus memiliki data terlebih dahulu sebelum dapat menyimpannya.

with open("student.json", "w") as file:

    json.dump(
        students,
        file,
        indent=4
    )

print()
print("=" * 60)
print("DATA BERHASIL DISIMPAN KE student.json")
print("=" * 60)


# ==========================================================
# TAHAP 5 — MEMBACA FILE JSON
# ==========================================================
# Business Rule
 # Program harus membaca kembali file student.json yang telah dibuat pada tahap sebelumnya.
# Mengapa menggunakan with open()?
 # Karena Python harus membuka file sebelum dapat membaca isinya.
 # Dengan "with", file akan ditutup otomatis setelah selesai digunakan.

 # Mengapa mode "r"?
 # "r" berarti read (membaca).
 # Mode ini digunakan ketika kita hanya ingin mengambil isi file tanpa mengubahnya.

 # Mengapa menggunakan json.load()?
 # Karena sumber data kita adalah FILE JSON.
 # json.load() akan mengubah isi file JSON menjadi object Python.

# Posisi kode
# Diletakkan setelah proses penyimpanan file,  karena file harus sudah ada terlebih dahulu.
# ==========================================================
with open("student.json", "r") as file:
    loaded_students = json.load(file)

# ==========================================================
# TAHAP 6 — VERIFIKASI HASIL PEMBACAAN FILE
# ==========================================================
# Business Rule
 # Memastikan bahwa data yang dibaca dari file benar-benar telah berubah menjadi object Python.

# Mengapa perlu verifikasi?
 # Kita tidak boleh mengasumsikan bahwa proses pembacaan file selalu berhasil.
 # Verifikasi membantu memastikan tipe data maupun isi datanya sesuai harapan.
# ==========================================================
print()
print("=" * 60)
print("HASIL PEMBACAAN FILE JSON")
print("=" * 60)

print(type(loaded_students))

print()

print(loaded_students)

print()
print("=" * 60)
print("DATA MAHASASISWA")
print("=" * 60)

for student in loaded_students:
    print(f"Nama     : {student['name']}")
    print(f"Umur     : {student['age']}")
    print(f"Jurusan  : {student['major']}")
    print(f"IPK      : {student['gpa']}")
    print(f"Aktif    : {student['is_active']}")
    print("-" * 40)