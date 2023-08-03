from db import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Message {self.id}>'
    
    default_values = {
        "firstname" : "",
        "lastname"  : "",
        "email"     : "",
        "country"   : "belgium",
        "gender"    : "m",
        "subject"   : "other",
        "message"   : ""
    }

    def create_message(values):
        return Message(
            firstname=values["firstname"], 
            lastname=values["lastname"],
            email=values["email"],
            country=values["country"],
            gender=values["gender"],
            subject=values["subject"],
            message=values["message"]
        )
    
    def update_from_object(message, values):
        for value in values:
            setattr(message, value, values[value]) 

    def insert_or_update(message):
        db.session.add(message)
        db.session.commit()
        return message.id
    
    def delete_message(message):
        db.session.delete(message)
        db.session.commit()