from flask import Flask, request, jsonify
from weighted_average import get_weighted_average

app = Flask(__name__)

scores = []

@app.rouse('/reset_scores', methods=['GET'])
def reset_scores():
    scores = []
    return jsonify({'reset scores to '}), 200


@app.route('/get_happinese', methods=['GET'])
def get_happinese():
    score = get_weighted_average(scores, 0.9)
    return jsonify({'score' : score}), 200


@app.route('/happiness', methods=['PUT'])
def calculate_happiness():
    # { score : number }
    data = request.json  
    scores.append(data.score)
    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
