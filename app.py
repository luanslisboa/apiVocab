from flask import Flask, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ngrams
from string import punctuation

app = Flask(__name__)

stop = stopwords.words('portuguese')
ltext = []

# first page
@app.route('/')
def index():
    return "Hello! Send text to: /sendText/<br>" \
           "Get vector from: /response/ngram<br>" \
           "ngram can be 1 or 2<br>" \
           "<br>Use for post: " \
           '<form action="/sendText" method="post">' \
           '<input type="text" name="text" value="">' \
           '<input type="submit" value="Send">' \
           '</form>' \
           '<br>Obs.: One text per time.'

# request
@app.route('/sendText/', methods=['POST'])
def sendText():
    text = request.form['text']
    #text = request.form.get('text')
    text = cleaning(text)
    ltext.append(text)

    return "Text successfully added"

# response
@app.route('/response/<ngram>', methods=['GET'])
def response(ngram):
    ngram = int(ngram)
    vec = {}

    if ngram is not None:
        for text in ltext:
            vec = tokenize(text, ngram, vec)

        for text in ltext:
            vec = vector(text, vec)

        return vec

    else:
        return 'error'

# cleaning
def cleaning(text):
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, ' ')
    ilist = []
    for w in text.split():
        if w not in stop:
            ilist.append(w)

    text = " ".join(ilist)
    return text

# generate token
def tokenize(text, ngram, vec):
    for word in get_ngrams(text, ngram):
        try:
            vec[word] = 0
        except:
            pass

    return vec

# separate in grams
def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    return [' '.join(grams) for grams in n_grams]

# count occurrences
def vector(text, vec):
    for word in vec:
        vec[word] += text.count(word)

    return vec

if __name__ == '__main__':
    app.run()