"""app"""
import test

from flask import Flask, jsonify, request

import predict_soil

app = Flask(__name__)


@app.route("/update", methods=['GET'])
def update():
    test.test()
    temp = request.args.get('field1')
    humidity = request.args.get('field2')
    moisture = request.args.get('field3')
    prediction = predict_soil.run((temp, humidity, moisture))
    with open("Predictions.txt", "a") as f:
        f.write("Prediction Category:" + prediction + '\n')
    return jsonify({"Success": True, "Prediciton": prediction})
    # return 'Done'

if __name__ == "__main__":
    app.run()
