from flask import Flask, render_template, jsonify
import predictions
from predictions import *

predictions.startup();


predictions.makePredictions('f');



word1 = "test1"
word2 = "test2"
word3 = "test3"

dictSend = {'word1': word1, 'word2': word2, 'word3': word3}

app = Flask(__name__)

@app.route('/')

def index():
	return render_template('./test.html')

@app.route("/getData", methods=['GET'])
def getData():
	return jsonify(dictSend)

if __name__ == '__main__':
	app.run(host='0.0.0.0')