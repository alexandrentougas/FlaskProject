from flask import flash
import re

class MessageUtils():
    def __init__(self, form, values):
        self.email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        self.sanitization_regex = "<script>|</script>"
        self.honeyfields = ["name", "email1"]
        self.form = form
        self.values = values

    def sanitization(self):
        for fieldName in self.form:
            if fieldName not in self.honeyfields:
                self.values[fieldName] = re.sub(self.sanitization_regex, "", self.form[fieldName])

    def validation(self):
        invalid = False

        for field in self.form:
            if not self.form[field] and field not in self.honeyfields:
                flash('is required', field)
                invalid = True

        if re.fullmatch(self.email_regex, self.form["email"]) == None:
            flash('is invalid', "email")
            invalid = True

        return invalid
    
    def purify(self):
        self.sanitization()
        return self.validation()
                