from pymongo import MongoClient

def get_mongo_database(db_name,host="localhost",port=27017,username=None,password=None):
    if username and password :
        mongo_uri = "mongodb//%s:%s@%s/%s" %(username,password,host,db_name)
        connection = MongoClient(mongo_uri)
    else :
        connection = MongoClient(host,port)
    return connection[db_name]

DB_NAME = "simple_chat_database"
db = get_mongo_database(DB_NAME)
collection = db["simple_chat"]

messages = [
    {"time":1579236522,"name":"foo","payload":"Hello bar!"},
    {"time":1579236661,"name":"bar","payload":"Hello foo!"},
]


def get_messages(query=None):
    if query :
        return collection.find(query)
    return collection.find()

def add_message(username,post_time,payload):
    message = {"time":int(post_time),"name":username,"payload":payload}
    collection.insert(message)

def main():
    # データを消す
    collection.drop()

    # テストデータを挿入
    for msg in messages :
        collection.insert(msg)



if __name__ == "__main__":
    main()