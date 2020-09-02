import nltk
from flask import Flask
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import ngrams
from nltk.tokenize import word_tokenize

app = Flask(__name__)

@app.route('/Buscardoc/<text>')

#stop = stopwords.words('portuguese')

def GetDoc(text):
    #stringbusca = [word for word in stringbusca if word not in stopwords.words('portuguese')]

    stop = stopwords.words('portuguese')
    #stop.append('oito'.upper())

    textTratado = text

    for p in stop:
        textTratado = textTratado.replace(' '+p+' ', ' ')

    tokens = nltk.tokenize.word_tokenize(textTratado)
    fdist = FreqDist(tokens)

    return fdist# str('trat: '+ textTratado + ' orig: ' + text)

@app.route('/ngram/<text>/<ngram>')

def ngram(text,ngram):

    print(text)
    print(ngram)
    #stringbusca = [word for word in stringbusca if word not in stopwords.words('portuguese')]

    stop = stopwords.words('portuguese')
    #stop.append('oito'.upper())

    textTratado = text

    for p in stop:
        textTratado = textTratado.replace(' '+p+' ', ' ')

    #tokens = nltk.tokenize.word_tokenize(textTratado)
    #fdist = FreqDist(tokens)

    print(textTratado)

    #n_grams = ngrams(word_tokenize(textTratado), ngram)

    r = get_ngrams(textTratado,int(ngram))

    #print(n_grams)

    print(r[0])

    return str(r)

def get_ngrams(text, n ):
    print(n)
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]

if __name__ == '__main__':
    app.run()

