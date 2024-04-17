from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from models.recommend_fragrance import recommend_perfumes
import warnings
import logging

warnings.filterwarnings("ignore", category=UserWarning)

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
    """
    Endpoint for recommending perfumes based on user's favorite perfumes.

    Returns:
        A JSON response containing the recommended perfumes.
    """
    data = request.get_json()

    if not data:
        abort(400, description="No data provided.")

    fav_perfumes = data.get('fav_perfumes', [])

    if not isinstance(fav_perfumes, list):
        abort(400, description="Favorite perfumes should be a list.")

    if not all(isinstance(perfume, str) for perfume in fav_perfumes):
        abort(400, description="Each item in favorite perfumes should be a string.")

    if not fav_perfumes:
        abort(400, description="Please provide a list of favorite perfumes.")

    try:
        recs = recommend_perfumes(fav_perfumes)
    except Exception as e:
        logging.error(f"Failed to get recommendations: {e}")
        abort(500, description="Failed to get recommendations.")

    return jsonify(recs)

if __name__ == '__main__':
    app.run(debug=True)