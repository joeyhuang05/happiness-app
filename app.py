from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def check_server():
    #data = request.json  
    return jsonify({'server-response' : 'okay'})


@app.route('/happiness', methods=['POST'])
def calculate_happiness():
    #data = request.json  
    return jsonify({'Happinese score ': 'good'})

if __name__ == '__main__':
    app.run(debug=True)
