from flask import Flask, request, jsonify
from prediction import predict

def flask_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def server_is_up():
        return 'Welcome to the Mtcars MPG prediction API!'

    @app.route('/predict', methods=['POST'])
    def start():
        to_predict = request.json
        print(to_predict)
        y_pred = predict(to_predict)
        return jsonify({"mpg_prediction": y_pred})

    return app

if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0', port=8080)
