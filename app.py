from flask import Flask, make_response,request
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import ngrams
from nltk.tokenize import word_tokenize
from string import punctuation

app = Flask(__name__)

stop = stopwords.words('portuguese')
ltext = []
vec = {}

@app.route('/')
def index():
    return "Hello! Send text to: 'site address'/request" \
           "Get vector from: /response/<ngram>" \
           "ngram can be null, 1 or 2"

@app.route('/test')
def testPost():
    return '<form action="/request/" method="post">' \
           '<input type="text" value="Falar é fácil. Mostre-me o código.">'\
           '<input type="submit" value="text">' \
           '</form>'

# request
@app.route('/request/', methods=['POST'])
def request():
    text = request.form['text']
    ltext.append(text)

    return make_response("Text successfully added", 201)

# response
@app.route('/response/<ngram>', methods=['GET'])
def response(ngram):
    for text in ltext:
        tokenize(text,ngram)
        vector(text)

    return vec

# cleaning
def cleaning(text):
    text = text.lower()
    ilist = []
    for p in punctuation:
        text = text.replace(p,' ')
    ilist = []
    for w in text.split():
        if w not in stop:
            ilist.append(w)

    text = " ".join(ilist)
    return text

# generate token
def tokenize(text,ngram):
    n = 1
    if ngram == None:
        n = 1
    else:
        n = ngram

    for word in get_ngrams(text, n):
        try:
            vec[word] = 0
        except:
            pass

def vector(text):
    for word in vec:
        vec[word] += text.count(word)

def get_ngrams(text, n ):
    print(n)
    n_grams = ngrams(word_tokenize(text), n)
    return [' '.join(grams) for grams in n_grams]

if __name__ == '__main__':
    app.run()

