import flask
import sklearn
from flask import render_template
from tensorflow import keras

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html' )
        
    if flask.request.method == 'POST':
        model_loaded = keras.models.load_model("model/matrix_mlp")

        f01 = float(flask.request.form['f01'])
        f02 = float(flask.request.form['f02'])
        f03 = float(flask.request.form['f03'])
        f04 = float(flask.request.form['f04'])
        f05 = float(flask.request.form['f05'])
        f06 = float(flask.request.form['f06'])
        f07 = float(flask.request.form['f07'])
        f08 = float(flask.request.form['f08'])
        f09 = float(flask.request.form['f09'])
        f10 = float(flask.request.form['f10'])
        f11 = float(flask.request.form['f11'])
        f12 = float(flask.request.form['f12'])

        exp = [f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12]

        temp = model_loaded.predict([exp])
        return render_template('main.html', result = temp)

if __name__ == '__main__':
    app.run()