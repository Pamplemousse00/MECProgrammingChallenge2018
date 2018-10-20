from flask import Flask, render_template, jsonify


#if get tildae, run predictions.flushPredictions

word1 = "yousef"


dictSend = {'word1': word1}

app = Flask(__name__)

@app.route('/')

def index():
	return render_template('test.html')

@app.route("/getData", methods=['GET'])
def getData():
	return jsonify(dictSend)

if __name__ == '__main__':
	app.run(host='0.0.0.0')