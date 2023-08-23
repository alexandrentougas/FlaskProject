from flask import Flask
from sqlalchemy_utils import database_exists, create_database
from db import db, mongoConnection
from routes.messageRoutes import blueprint

app = Flask(__name__)
app.config.from_object('config')

app.config["my_mongo_db"] = mongoConnection(app.config["MONGO_URI"], app.config["MONGO_DB_NAME"])

db.init_app(app)

with app.app_context():
    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])
        db.create_all()

app.register_blueprint(blueprint, url_prefix='/messages')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)