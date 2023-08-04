from flask import render_template, request, redirect, url_for
from models.messageModel import Message
from utils import MessageUtils

def index():
    messages = Message.query.all()
    return render_template("index.html", messages=messages)

def message(id):
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
            Message.update_from_object(message, values)
            message_id = Message.insert_or_update(message)
            return redirect(url_for("blueprint.message", id=message_id))

    return render_template('message_form.html', message=message)

def delete(id):
    message = Message.query.get_or_404(id)
    Message.delete_message(message)
    return redirect(url_for('blueprint.index'))