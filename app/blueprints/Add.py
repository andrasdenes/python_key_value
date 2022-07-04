from flask import Blueprint, request
from app.blueprints.Handlers.AddHandler import AddHandler
add_blueprint = Blueprint("add_blueprint", __name__,url_prefix="/add")

@add_blueprint.route("/", methods=["GET", "POST"])
def add():
    AddHandler().handle(request)