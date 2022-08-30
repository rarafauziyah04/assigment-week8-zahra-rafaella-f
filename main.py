import pymongo # meng-import library pymongo yang sudah kita install
from datetime import datetime
client = pymongo.MongoClient("mongodb+srv://rara0406:rara0406@cluster0.e3zc6ay.mongodb.net/?retryWrites=true&w=majority")
db = client['zahra'] # ganti sesuai dengan nama database kalian
my_collections = db['fauziyah']


data = {"kecepatan": 90,
    "latitude": 6.2088,
    "longitude": 106.8456,
    "Timestamp": datetime.now()}


results = my_collections.insert_many([data])
print(results.inserted_ids) # akan menghasilkan ID dari data yang kita masukkan