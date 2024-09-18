import pymongo
from decouple import config

mongo_client = config("MONGO_CLIENT")

def connect_to_mongodb():
    try:
        client = pymongo.MongoClient(mongo_client)
        print("Connected to MongoDB successfully")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
    
    
# connect_to_mongodb()

def retrieve_all_data(db_name, collection_name):
    client = connect_to_mongodb()
    if client:
        try:
            # access database and collecton
            db = client[db_name]
            collection = db[collection_name]
            
            # Retrieve all documents
            documents = collection.find()
            
            # print each document
            for doc in documents:
                print(doc)
            
            client.close() 
            
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None


def retrieve_data_by_id(db_name, collection_name, id_number):
    client = connect_to_mongodb()

    if client:
        try:
            
            db = client[db_name]
            collection = db[collection_name]
            record = collection.find_one({"id_number": id_number})
            if record:
                print(record)
            else:
                print(f"No record found with id_number: {id_number}")
        except Exception as e:
            print(f"Error retrieving data: {e}")
        

if __name__ == "__main__":
    db_name = 'usa'
    collection_name = 'people'

    # retrieve_all_data(db_name, collection_name)
    
    print("Data for id_number = 2")
    retrieve_data_by_id(db_name, collection_name, 2)
    