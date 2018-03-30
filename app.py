"""app"""
import test

from flask import Flask, jsonify, request, Response

import predict_soil

app = Flask(__name__)


@app.route("/update", methods=['GET'])
def update():
    temp = request.args.get('field1')
    humidity = request.args.get('field2')
    moisture = request.args.get('field3')
    # self learning
    with open("soil_dataset.csv", "a") as f:
        f.write('%s,%s,%s,%s\n' % (temp, -1, humidity, moisture))
    test.test()
    predict_soil.train()
    prediction = predict_soil.predict((temp, -1, humidity, moisture))
    with open("Predictions.txt", "a") as f:
        f.write("Prediction Category:" + prediction + '\n')
    return jsonify({"Success": True, "Prediciton": prediction})


@app.route("/getclusterCSV", methods=["GET"])
def get_data():
    with open("newset.csv", "r") as f:
        csv = f.read()
    csv = "Soil Temperature,Air Temperature,Humidity,Moisture,Cluster\n" + csv
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=clustered_data.csv"})


if __name__ == "__main__":
    app.run()
