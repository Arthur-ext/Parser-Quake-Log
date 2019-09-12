from pymongo import MongoClient
from urllib.parse import quote_plus

def conn_to_database():    
    user = "root"
    pswd = "root"
    host = "localhost:27017"
    uri = "mongodb://%s:%s@%s" % (
        quote_plus(user),
        quote_plus(pswd),
        host    
    )

    client = MongoClient(uri)
    base = client.parser_quake

    return base