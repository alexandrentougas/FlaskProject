import os
from dotenv import load_dotenv
import random, string

load_dotenv()
MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_PASS=os.getenv("MYSQL_PASS")
MONGO_USER=os.getenv("MONGO_USER")
MONGO_PASS=os.getenv("MONGO_PASS")
MONGO_DB_NAME=os.getenv("MONGO_DB_NAME")

MONGO_URI = f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.capgrvv.mongodb.net/?retryWrites=true&w=majority'

SQLALCHEMY_DATABASE_URI =\
        f'mysql://{MYSQL_USER}:{MYSQL_PASS}@localhost:3306/flask_project'
#SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])