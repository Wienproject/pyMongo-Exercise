import pymongo

dburl = 'mongodb://localhost:27017' #url server mongodb yg nanti untuk konek
# untuk konekin ke mongodb
myMongo = pymongo.MongoClient(dburl)
# ini untuk liat list database
dbs = myMongo.list_database_names()

Kampus = myMongo['Kampus'] #nama database penjualan. (baru)
Col_Dosen = Kampus['Dosen'] # ini sama dg fungsi db.createcollection. tp ini jg bisa akses collection lama
Col_Mahasiswa = Kampus['Mahasiswa']
print(dbs)

#Add user
user1 = Kampus.add_user('andi','anditopsecret',roles=['dbAdmin','readWrite'])
user2 = Kampus.add_user('budi','buditopsecret',roles=['readWrite'])

#Input data dosen
Data_Dosen=[{'nama':"Caca",
'usia':28,
'asal':"Jakarta",
'bidang':"Fisika Astrologi",
'titel':"S2",
'status':"Honorer",
'nip':123,
'matkul':["Metrologi","Kosmologi","Kalkulus"]},
{'nama':"Dedi",
'usia':29,
'asal':"Yogyakarta",
'bidang':"Fisika Terapan",
'titel':"S3",
'status':"PNS",
'nip':456,
'matkul':["Instrumentasi","Elektronika","Fisika Dasar"]},
{'nama':"Euis",
'usia':30,
'asal':"Bandung",
'bidang':"Fisika Teoretik",
'titel':"S1",
'status':"Honorer",
'nip':789,
'matkul':["Fisika Dasar","Fisika Modern","Kalkulus"]}]
Col_Dosen.insert_many(Data_Dosen)
print("data dosen sudah masuk")

#Input data Mahasiswa
Data_Mahasiswa=[{'nama':"Faza",
'usia':19,
'asal':"Aceh",
'prodi':"Fisika",
'angkatan':2017,
'nim':123},
{'nama':"Gilang",
'usia':20,
'asal':"Semarang",
'prodi':"Fisika",
'angkatan':2017,
'nim':456},
{'nama':"Hanafi",
'usia':20,
'asal':"Makassar",
'prodi':"Fisika",
'angkatan':2017,
'nim':789},
{'nama':"Dini",
'usia':20,
'asal':"Bekasi",
'prodi':"Fisika",
'angkatan':2017,
'nim':str('004')}]
Col_Mahasiswa.insert_many(Data_Mahasiswa)
print("data mahasiswa sudah masuk")

#Cek hasil sementara
for i in Col_Dosen.find():
    print(f'Dosen: \n {i}')
print ('='*100)
for i in Col_Mahasiswa.find():
    print(f'Mahasiswa: \n {i}')

#HAPUS Property Faza
Col_Mahasiswa.delete_one({"nama" : "Faza"})
print("Berhasil hapus data Faza")
print('='*100)
for i in Col_Mahasiswa.find():
    print(f'Mahasiswa: \n {i}')

#Insert Dodi dan data2nya
Dodi={'nama':"Dodi",
'usia':27,
'asal':"Surabaya",
'bidang':"Computer Science",
'titel':"S2",
'status':"PNS",
'nip':998,
'matkul':["Data Analysis","AI","NLP"]}
Col_Dosen.insert_one(Dodi)
print('Berhasil menambahkan Dodi')
print('='*100)
for i in Col_Dosen.find():
    print(f'Dosen: \n {i}')

#Mengubah nama Hanafi dan umurnya
Data = {"nim" : 789} # kondisi data yg nanti akan d update
Info_baru = {"$set": {"nama": 'Ahmad Hanafi',"usia": 22}}
Col_Mahasiswa.update_one(Data,Info_baru)
for i in Col_Mahasiswa.find() : 
    print(i)

# Mengubah nama property 'asal' > 'Kota_asal' : 
Data = {} 
new_val ={"$rename": {'asal' : 'Kota_asal'}}
Col_Dosen.update_many(Data,new_val)
print('Collection Dosen berhasil diubah')
Col_Mahasiswa.update_many(Data,new_val)
print('Collection Mahasiswa berhasil diubah')

# Mengubah prodi menjadi Matematika, untuk kondisi usia=20
Data = {'usia':20} 
new_val ={"$set": {'prodi' : 'Matematika'}} 
Col_Mahasiswa.update_many(Data,new_val)
print('Collection Mahasiswa berhasil diubah')

# Print Hasil akhir
for i in Col_Dosen.find():
    print(f'Dosen: \n {i}')
print ('='*100)
for i in Col_Mahasiswa.find():
    print(f'Mahasiswa: \n {i}')