import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('../RF_price_predicting_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    For rendering results on HTML GUI
    """
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    price = request.form.get("price")
    data[0] = int(price)
    distance = request.form.get("distance")
    data[1] = int(distance)
    owner = int(request.form.get("owner"))
    data[2] = owner
    seats = float(request.form.get("seats"))
    data[3] = seats
    mileage = float(request.form.get("mileage"))
    data[4] = mileage
    engine = float(request.form.get("engine"))
    data[5] = engine
    power = float(request.form.get("power"))
    data[6] = power
    location = request.form.get("location")
    if location == 'Bangalore':
        data[7] = 1
    elif location == 'Chennai':
        data[8] = 1
    elif location == 'Coimbatore':
        data[9] = 1
    elif location == 'Delhi':
        data[10] = 1
    elif location == 'Hydrabad':
        data[11] = 1
    elif location == 'Jaipur':
        data[12] = 1
    elif location == 'Kochi':
        data[13] = 1
    elif location == 'Kolkata':
        data[14] = 1
    elif location == 'Mumbai':
        data[15] = 1
    elif location == 'Pune':
        data[16] = 1
    fuel = request.form.get("fuel")
    if fuel == "CNG":
        pass
    elif fuel == "Diesel":
        data[17] = 1
    elif fuel == "LPG":
        data[18] = 1
    elif fuel == "Petrol":
        data[19] = 1

    transmission = int(request.form.get("transmission"))
    data[20] = transmission
    # v = [int(x) for x in request.form.values()]
    # int_features = [2015, 41000, 1, 5.0, 19.67, 1582.0,
    #                 126.20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    final_features = [np.array(data)]
    # v_f = [np.array(v)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=' You can sell the car for {} lakhs'.format(output))
    # return render_template('index.html', prediction_text=data)


if __name__ == "__main__":
    app.run(debug=True)
