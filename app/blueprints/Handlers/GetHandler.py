from app.blueprints.Handlers.RequestHandler import RequestHandler
from flask import render_template
from peewee import PeeweeException
from app.models.KeyValuePair import KeyValuePair

class GetHandler(RequestHandler):
    def handle(self, request):
        if request.method == "GET":
            return render_template("get.html")
        if request.method == "POST":
            requested_key = request.form.get("key", None)
            if requested_key is None:
                return "Key should contain a value", 400
            try:
                requested_object = KeyValuePair.get(key=requested_key)
                if requested_object is None:
                    return "NotFound", 404 
            except PeeweeException as e:
                return "NotFound", 404
            except Exception as e:
                raise e
            return render_template("get.html", results=requested_object.value)
        else:
            return "Request method not allowed", 400