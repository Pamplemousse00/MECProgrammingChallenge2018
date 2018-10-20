from flask import Flask, render_template, jsonify, request
import predictions



#if get tildae, run predictions.flushPredictions
words = predictions.startup()


dictSend = {'word1': words[0], 'word2': words[1], 'word3': words[2], 'word4': words[3],'word5': words[4]}

app = Flask(__name__)

@app.route('/')

def index():
	return render_template('test.html')

@app.route("/getData", methods=['GET'])
def getData():
	return jsonify(dictSend)

@app.route('/api', methods = ['POST'])
def api():
  data = request.get_json()
  result = ''
  predictions.makePrediction(str(data));

if __name__ == '__main__':
	app.run(host='0.0.0.0')