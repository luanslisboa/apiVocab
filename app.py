from flask import Flask, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
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

# test page post
@app.route('/test')
def testPost():
    return '<form action="/sendText" method="post">' \
           '<input type="text" name="text" value="Falar é fácil. Mostre-me o código.">'\
           '<input type="submit" value="Send">' \
           '</form>'

# request
@app.route('/sendText', methods=['POST'])
def sendText():
    text = request.form.get('text')
    text = cleaning(text)
    ltext.append(text)

    return "Text successfully added"

# response
@app.route('/response/<ngram>', methods=['GET'])
def response(ngram):
    for text in ltext:
        tokenize(text, int(ngram))
        vector(text)

    return vec

# cleaning
def cleaning(text):
    text = text.lower()
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
    for word in get_ngrams(text, ngram):
        try:
            vec[word] = 0
        except:
            pass

def vector(text):
    for word in vec:
        vec[word] += text.count(word)

def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    return [' '.join(grams) for grams in n_grams]

if __name__ == '__main__':
    app.run()

