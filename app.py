from flask import Flask, send_from_directory
from flask_cors import CORS # <-追加
from app1.main import app1
import os

SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
CORS(app)


"""React(Webフロント用のapi)"""
app.register_blueprint(app1, url_prefix='/CPSLAB-API-V1')

@app.route('/')
def index():
    return {"message":"HI"}

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(SAVE_DIR, path)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=port,threaded=True,debug=True)
