from flask import Flask, render_template, request, redirect, url_for
from dummy import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        return render_template("index.html")
    
    if (request.method == 'POST'):
        arr_input = request.form.get('text')
        prediction("./finalized_model.sav", arr_input)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()