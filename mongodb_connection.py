import pymongo ,os

url = os.environ.get('MONGODB_LOCAL_URL')

client = pymongo.MongoClient(url)

db =  client['test_db']