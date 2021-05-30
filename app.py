import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('final_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [(x) for x in request.form.values()]
    final_features = (int_features)
    prediction = model.predict(final_features)
    prob = model.predict_proba(final_features)

    output = prediction[0]
    output2 = round(prob[0][1])

    return render_template('index.html', prediction_text='The given statement is {} and probability is {}'.format(output, output2))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([list(data.values())])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)