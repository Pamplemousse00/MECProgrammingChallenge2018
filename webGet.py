from flask import Flask, render_template, jsonify


#if get tildae, run predictions.flushPredictions

word1 = "test1"
word2 = "test2"
word3 = "test3"
word4 = "test4"
word5 = "test5"

dictSend = {'word1': word1, 'word2': word2, 'word3': word3, 'word4': word4, 'word5': word5}

app = Flask(__name__)

@app.route('/')

def index():
	return render_template('test.html')

@app.route("/getData", methods=['GET'])
def getData():
	return jsonify(dictSend)

if __name__ == '__main__':
	app.run(host='0.0.0.0')