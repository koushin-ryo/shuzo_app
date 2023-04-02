from flask import Flask, jsonify, Response, make_response, request, send_from_directory
import json
import random
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, origins="*", allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"], supports_credentials=True)

# 松岡修造の名言リスト
quotes = [
    "まず疑うな、信じろ。そうすれば成功する。",
    "どんなに辛くても、絶対に歩みを止めてはいけない。",
    "もしも失敗したら、すぐに叩きつけてくる現実に逆らって、もう一度チャレンジすることだ。",
    "無謀だと言われることがある。それは自分の可能性を信じきれない人たちが言うことだ。",
    "君がやりたいことがあるなら、周りの人に言わないで実行してみろ。",
]
@app.route("/", methods=["GET"])
def index():
    return send_from_directory("static", "index.html")


@app.route('/api/random_quote', methods=['GET'])
@cross_origin()
def random_quote():
    quote = random.choice(quotes)
    response = make_response(json.dumps({"quote": quote}, ensure_ascii=False))
    response.headers['Content-Type'] = 'application/json;charset=utf-8'
    return response



if __name__ == '__main__':
    app.run(debug=True)
