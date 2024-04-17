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

# create a route that returns perfume recommendations based on the user input
# the function accepts 1 param, fav_perfumes, which is a list of the user's favorite perfumes

@app.route('/api/recommend', methods=['POST'])
@cross_origin()
def recommend():
    if not request.json or 'fav_perfumes' not in request.json:
        return jsonify({'error': 'No fav_perfumes in the request'}), 400

    fav_perfumes = request.json['fav_perfumes']

    # Validate fav_perfumes here if necessary
    if not isinstance(fav_perfumes, list):
        return jsonify({'error': 'fav_perfumes should be a list'}), 400

    if not fav_perfumes:
        return jsonify({'error': 'fav_perfumes should not be empty'}), 400

    try:
        recs = recommend_perfumes(fav_perfumes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'status': 'success', 'recommendations': recs}), 200


if __name__ == '__main__':
    app.run(debug=True)