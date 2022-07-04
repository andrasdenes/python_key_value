from flask import Blueprint, request
from app.blueprints.Handlers.GetHandler import GetHandler
get_blueprint = Blueprint("get_blueprint", __name__, url_prefix='/get')

@get_blueprint.route("/", methods=["GET", "POST"])
def get():
    return GetHandler().handle(request)