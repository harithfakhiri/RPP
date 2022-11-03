from flask import Flask, render_template, request, redirect, url_for
from dummy import *
import sys

app = Flask(__name__)
pred = -1

@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        global pred
        if pred == 0:
            pred_result = "M"
        elif pred == 1:
            pred_result = "B"
        else:
            pred_result = " Belum melakukan prediksi"
        return render_template("index.html", prediction=pred_result)
    
    if (request.method == 'POST'):
        inputs = []
        res = request.form.to_dict()
        
        for key, value in res.items():
            inputs.append(float(value))
        arr_input = [inputs]

        # print(arr_input, file=sys.stdout)
        pred = prediction('./predictflask/envpredict/finalized_model.sav', arr_input)
        # print(pred, file=sys.stdout)
    return redirect(url_for('index'))

@app.route('/')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(debug=True)