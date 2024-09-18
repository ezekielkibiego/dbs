import pymongo
import csv
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
            
            # convert documents to a list in the collection
            data = list(documents)
            
            client.close() 
            
            return data
            
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None

def write_to_csv(data, csv_file_name):
    if data:
        try:
           keys = data[0].keys()
           with open(csv_file_name, 'w', newline = '', encoding= 'utf-8') as csvfile:
               writer = csv.DictWriter(csvfile, fieldnames=keys)
               writer.writeheader()
               writer.writerows(data)
               
               print(f"Data written to {csv_file_name} successfully")
               
           
        except Exception as e:
            print(f"Error writing to csv file: {e}")
            return None

if __name__ == "__main__":
    db_name = 'usa'
    collection_name = 'people'
    csv_file_name = 'mongo_people_data.csv'
    
    data = retrieve_all_data(db_name, collection_name)
    write_to_csv(data, csv_file_name)
    