from flask import Flask, render_template
from peewee import *
from app.models.KeyValuePair import KeyValuePair
from app.blueprints.Add import add_blueprint
from app.blueprints.Get import get_blueprint
from configuration import *

app = Flask(__name__)

db = SqliteDatabase(DB_NAME)
db.connect()
db.create_tables([KeyValuePair])

@app.route("/")
def home():
    return render_template("base.html")

app.register_blueprint(add_blueprint)
app.register_blueprint(get_blueprint)
print(app.url_map)