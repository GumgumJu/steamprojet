import pandas as pd
from flask_pymongo import PyMongo
from flask import Flask,jsonify,render_template,request
import numpy as np
from flask.json import JSONEncoder
import pymongo
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
import re


app=Flask(__name__)
##Importez le texte des données du crawler.
client = MongoClient('mongodb://localhost:27017/')
database = client['steamgame']
collection = database['steam']
df_json = pd.read_json("data5.json")
collection.insert_many(df_json.to_dict(orient='records'))

mongo=mongo = PyMongo(app, uri="mongodb://localhost:27017/steamgame")

@app.route('/',methods=["GET", "POST"])
def index():
    limit = request.form.get("limit")
    page = request.form.get("page")
    content = request.form.get("content")
    if not limit:
        limit = 50
    if not page:
        page = 1
        count = mongo.db.steam.find({})
        online_steam = mongo.db.steam.find({}, {"_id": 0}).limit(int(limit)).skip((int(page) - 1) * int(limit))
        table_result = {"code": 0, "msg": None, "count": count, "data": list(online_steam)}
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8050)
