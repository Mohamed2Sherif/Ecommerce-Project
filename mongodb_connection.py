from mongoengine import connect
import os

name = os.environ.get("MONGO_DB_NAME")
host = os.environ.get("MONGO_DB_HOST")
port = os.environ.get("MONGO_DB_PORT")
url = os.environ.get("MONGO_DB_CONNECTION_URL")
connect(HOST=url,db="OLA_Store")