from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://shawsamir667_db_user:5c2VnQNzJRMIkq4Q@cluster0.kn3xehp.mongodb.net/?appName=Cluster0"


client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)