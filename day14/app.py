from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/hello')
def hello():
    return jsonify({
        'message': 'Hello'
    })


@app.route('/add_comment', methods=['POST'])
def addComment():
    comment = request.json.get('comment', '')
    return jsonify({
        'new_comment': "New comment: " + comment
    })


app.run(debug=True)
