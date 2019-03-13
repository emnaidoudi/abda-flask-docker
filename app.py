from flask import Flask, jsonify
import nltk
from emna import sayHi


nltk.download('punkt')
app = Flask(__name__)

#w = nltk.word_tokenize("hello here")

@app.route("/api/<string:sentence>")
def basic(sentence):
    x=sayHi()
    return  jsonify({"response":nltk.word_tokenize(sentence),"say-hi":x})  

    

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")