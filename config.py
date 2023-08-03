import os
from dotenv import load_dotenv
import random, string

load_dotenv()
MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_PASS=os.getenv("MYSQL_PASS")

SQLALCHEMY_DATABASE_URI =\
        f'mysql://{MYSQL_USER}:{MYSQL_PASS}@localhost:3306/flask_project'
#SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])