from nltk.stem.lancaster import LancasterStemmer

def sayHi():
    stemmer = LancasterStemmer()
    x=stemmer.stem("trying")
    return x