from flask import Flask
from flask.json import JSONEncoder
from datetime import datetime, date
from handlers import  post

app = Flask(__name__)
app.register_blueprint(post.app)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return JSONEncoder.default(self, obj)
#  替换默认的json编码器
app.json_encoder = CustomJSONEncoder


