from flask import Flask, render_template, request, flash, redirect, url_for
import json
import re

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=('GET', 'POST'))
def index():
    invalid = False
    values = {
            "firstname" : "",
            "lastname" : "",
            "emailabcd" : "",
            "country" : "belgium",
            "gender" : "male",
            "subject" : "other",
            "message" : ""
        }
    honeyfields = ["name", "email"]

    if request.method == 'POST':
        if request.form["name"] or request.form["email"]:
            return redirect(url_for("result", values="[]"))
        
        sanitization_regex = "<script>|</script>"

        for fieldName in request.form:
            if fieldName not in honeyfields:
                values[fieldName] = re.sub(sanitization_regex, "", request.form[fieldName])

        for field in request.form:
            if not request.form[field] and field not in honeyfields:
                flash('is required', field)
                invalid = True

        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(email_regex, request.form["emailabcd"]) == None:
            flash('is invalid', "emailabcd")
            invalid = True
        
        if invalid:
            return render_template('index.html', values=values)
        else:
            return render_template("result.html", values=values)    

    else:
        return render_template('index.html', values=values)
    
""" @app.route('/result/')
def result():
    return render_template('result.html', values=json.loads(request.args["values"])) """