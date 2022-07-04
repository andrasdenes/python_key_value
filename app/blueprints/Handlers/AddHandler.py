from flask import render_template
from peewee import PeeweeException
from app.models.KeyValuePair import KeyValuePair
from app.blueprints.Handlers.RequestHandler import RequestHandler

class AddHandler(RequestHandler):
    def handle(self, request):
        if request.method == "GET":
            return render_template("add.html")

        if request.method == "POST": 
            desired_key = request.form.get("key", None)
            desired_value = request.form.get("value", None)
            if desired_key is None or desired_value is None:
                return "Every field should contain values", 400
            try:
                pair = KeyValuePair()
                pair.key = desired_key
                pair.value = desired_value
                affected_records = pair.save()
                if affected_records < 1:
                    return "Error", 400
            except PeeweeException as e:
                return "Error", 500
            except Exception as e:
                raise e
            return render_template("add.html", results=[desired_key, desired_value]) 
        else:
            return "Request method not allowed", 400