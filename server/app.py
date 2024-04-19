from flask import Flask, request
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
    """
    Endpoint for recommending perfumes based on user's favorite perfumes.

    Returns:
        A list of recommended perfumes.
    """
    data = request.get_json()
    if not data or 'fav_perfumes' not in data:
        return {"error": "Missing 'fav_perfumes' in request data"}, 400

    fav_perfumes = data['fav_perfumes']
    if not isinstance(fav_perfumes, list) or not fav_perfumes:
        return {"error": "'fav_perfumes' should be a non-empty list"}, 400

    recs = recommend_perfumes(fav_perfumes)
    return recs, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)