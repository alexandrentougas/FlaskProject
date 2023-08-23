from flask import render_template, request, redirect, url_for, current_app
from models.messageModel import Message
from utils import MessageUtils

def index():
    for doc in current_app.config["my_mongo_db"]["messages"].find():
        print(doc)
    messages = Message.query.all()
    return render_template("index.html", messages=messages)

def message(id):
    print(current_app.config["my_mongo_db"]["messages"].find_one({"messageId": id}))
    message = Message.query.get_or_404(id)
    return render_template('message.html', message=message)

def create():
    values = dict(Message.default_values)

    if request.method == 'POST':
        if request.form["name"] or request.form["email1"]:
            return redirect(url_for("result", values="[]"))
        
        invalid = MessageUtils(request.form, values).purify()
        
        if invalid:
            return render_template('message_form.html', message=values)
        else:
            current_app.config["my_mongo_db"]["messages"].insert_one(values)
            message = Message.create_message(values)
            message_id = Message.insert_or_update(message)
            return redirect(url_for("blueprint.message", id=message_id))

    else:
        return render_template('message_form.html', message=values)
    
def edit(id):
    message = Message.query.get_or_404(id)

    if request.method == 'POST':
        values = {}

        invalid = MessageUtils(request.form, values).purify()

        if invalid:
            return render_template('message_form.html', message=values)
        else:
            current_app.config["my_mongo_db"]["messages"].update_one({"messageId": id}, { "$set": values })
            Message.update_from_object(message, values)
            message_id = Message.insert_or_update(message)
            return redirect(url_for("blueprint.message", id=message_id))

    return render_template('message_form.html', message=message)

def delete(id):
    current_app.config["my_mongo_db"]["messages"].delete_one({"messageId": id})
    message = Message.query.get_or_404(id)
    Message.delete_message(message)
    return redirect(url_for('blueprint.index'))