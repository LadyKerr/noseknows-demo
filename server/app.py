from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from models.recommend_fragrance import recommend_perfumes

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api')
@cross_origin()
def home():
    return "Let's build a perfume recommendation API!"


if __name__ == '__main__':
    app.run(debug=True)