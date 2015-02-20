import nltk
import nltk.stem

def stem(words):
    stemmer = nltk.stem.snowball.EnglishStemmer(ignore_stopwords=True)
    return [stemmer.stem(word) for word in words]

def unstop(words):
    stop = nltk.corpus.stopwords.words('english')
    stop += [',', '.', ':', ';', ')', '(', '[', ']', '{', '}', '-', '--', '=', '#', '&']
    return [word for word in words if word not in stop]

def bag_of_words(phrase):
    sents = nltk.tokenize.sent_tokenize(phrase)
    words = []
    for sent in sents:
        words += nltk.tokenize.word_tokenize(sent)
    swords = unstop(stem(words))

    bag = {}
    for word in swords:
        if word in bag:
            bag[word] += 1
        else:
            bag[word] = 1
    return bag
