from flask import Flask, request, jsonify, abort
from flask_cors import CORS, cross_origin
from models.recommend_fragrance import recommend_perfumes

app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api')
@cross_origin()
def home():
    return "Let's build a perfume recommendation API!"

# create a route that recommends perfume based on the liked perfumes
# the param should be liked_perfumes

@app.route('/api/recommend', methods=['POST'])
@cross_origin()
def recommend():
    """
    Endpoint for recommending perfumes based on user's liked perfumes.

    Returns:
        A JSON response containing the recommended perfumes.
    """
    if not request.json or 'liked_perfumes' not in request.json:
        abort(400, description="Invalid input: 'liked_perfumes' is required in the request body.")
    
    liked_perfumes = request.json['liked_perfumes']
    
    if not isinstance(liked_perfumes, list) or not liked_perfumes:
        abort(400, description="Invalid input: 'liked_perfumes' should be a non-empty list.")
    
    try:
        recs = recommend_perfumes(liked_perfumes)
    except Exception as e:
        abort(500, description=str(e))
    
    return jsonify(recs), 200

if __name__ == '__main__':
    app.run(debug=True)