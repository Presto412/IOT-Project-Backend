"""app"""
import test
import thingspeak_data

from flask import Flask, jsonify, request, Response

import predict_soil

app = Flask(__name__)


@app.route("/update", methods=['GET'])
def update():
    data = thingspeak_data.get_data()
    temp = data['field1']
    humidity = data['field2']
    moisture = data['field3']
    # self learning
    test.test()
    predict_soil.train()
    prediction = predict_soil.predict((temp, -1, humidity, moisture))
    with open("soil_dataset.csv", "a") as f:
        f.write('%s,%s,%s,%s\n' % (temp, -1, humidity, moisture))
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
