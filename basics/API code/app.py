from flask import flask, jsonify

app Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_message():
    """
    API endpoint to get a simple message.
    """
    message = {'message': 'Welcome to the API!'}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)