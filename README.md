# pyMongo-Exercise

MongoDB - Exercise


Dosen & Mahasiswa
Buatlah sebuat file Python MongoDB untuk membuat sebuah database NoSQL (Document Store) dengan spesifikasi sebagai berikut:

Terdapat sebuah database dengan nama "Kampus".

Database "Kampus" memiliki 2 buah user:

User pertama adalah admin database bernama "andi", dengan password "anditopsecret".
User kedua bukanlah admin, namun tetap dapat memasukkan & membaca data dari database. User kedua bernama "budi", dengan password "buditopsecret".
Database "Kampus" memiliki 2 buah collection: "Dosen" dan "Mahasiswa".

Masukkan 3 buah data berikut ke collection "Dosen":

{nama:"Caca",
usia:28,
asal:"Jakarta",
bidang:"Fisika Astrologi",
titel:"S2",
status:"Honorer",
nip:123,
matkul:["Metrologi","Kosmologi","Kalkulus"]}

{nama:"Dedi",
usia:29,
asal:"Yogyakarta",
bidang:"Fisika Terapan",
titel:"S3",
status:"PNS",
nip:456,
matkul:["Instrumentasi","Elektronika","Fisika Dasar"]}

{nama:"Euis",
usia:30,
asal:"Bandung",
bidang:"Fisika Teoretik",
titel:"S1",
status:"Honorer",
nip:789,
matkul:["Fisika Dasar","Fisika Modern","Kalkulus"]}
Masukkan 4 buah data berikut ke collection "Mahasiswa":

{nama:"Faza",
usia:19,
asal:"Aceh",
prodi:"Fisika",
angkatan:2017,
nim:123}

{nama:"Gilang",
usia:20,
asal:"Semarang",
prodi:"Fisika",
angkatan:2017,
nim:456}

{nama:"Hanafi",
usia:20,
asal:"Makassar",
prodi:"Fisika",
angkatan:2017,
nim:789}

{nama:"Dini",
usia:20,
asal:"Bekasi",
prodi:"Fisika",
angkatan:2017,
nim:004}
Kemudian Hapus Nama Faza Dari Collection Mahasiswa

Tambahkan data Dodi ke dalam Collection Dosen berikut rincian data Dodi

{nama:"Dodi",
usia:27,
asal:"Surabaya",
bidang:"Computer Science",
titel:"S2",
status:"PNS",
nip:998,
matkul:["Data Analysis","AI","NLP"]}
Ubah Nama Hanafi menjadi Ahmad Hanafi dan Usia nya menjadi 22 (Mahasiswa)

Ubah semua Prodi Mahasiswa yang berusia 20 menjadi Matematika (Mahasiswa)

Ubah field asal menjadi Kota_asal (Mahasiswa)

Hasil akhir Collection Mahasiswa menjadi :

{nama:"Gilang",
usia:20,
kota_asal:"Semarang",
prodi:"Matematika",
angkatan:2017,
nim:456}

{nama:"Ahmad Hanafi",
usia:22,
kota_asal:"Makassar",
prodi:"Fisika",
angkatan:2017,
nim:789}

{nama:"Dini",
usia:20,
kota_asal:"Bekasi",
prodi:"Matematika",
angkatan:2017,
nim:004}
Buat Menu CRUD

file dikirimkan via email : khumaeni@purwadhika.com
