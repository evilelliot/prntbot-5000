from tinydb import TinyDB, Query
class Database:
    def add_entry(data):
        db = TinyDB('database.json')
        db.insert({'char': data})
    