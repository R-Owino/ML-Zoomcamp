import pickle
from flask import Flask, request, jsonify

dv = 'dv.bin'
model = 'model2.bin'

# loading the models
with open(dv, 'rb') as f_in:
    dv = pickle.load(f_in)

with open(model, 'rb') as f_in:
    model = pickle.load(f_in)

# Starting the flask app
app = Flask('get_card')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    get_card = y_pred >= 0.5

    result = {
        'get_card_probability': float(y_pred),
        'get_card': bool(get_card)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4545)