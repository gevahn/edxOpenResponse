#!/usr/bin/python

import nltk
import nltk.stem
import json
import StringIO

responses_txt = """2: Entropy is a measure of randomness, disorder. Substances tend to prefer higher entropy, more disordered states.
2: Entropy is a measure of the disorder in a system.
2: Entropy is a measure of disorder.
2: Entropy is the amount of disorder in a system.
1: Entropy is the disorder caused by a chemical reaction.
0: Entropy is the change in energy due to heat gained and/or lost in a spontaneous chemical process.
2: Entropy is a measure of the amount of chaos in something.
2: Entropy is a measure of disorder or chaos. 
2: Entropy is the chaos, randomness, lack of order in a system.
1: Entropy is like the randomness of a reaction -- it describes how likely things are to react.
1: Entropy is disorder.
1: Entropy is a measure of thermodynamic stability.
0: Entropy is related to the work done by the system.
1: Entropy is related to the heat released by the system.
0: Entropy is a measure of how fast a reaction goes.
0: Entropy is the amount of energy in the system.
1: Entropy is the tendency of systems to be in the most probable state.
0: Entropy is a measure of the amount of energy in a system.
1: Entropy will cause the heat death of the universe.
1: Entropy tells us if a process is spontaneous or not.
0: Entropy is order.
2: Entropy is the quantity that should spontaneously increase over time in an isolated system (as per Second Law of Thermodyanmics).
1: Entropy is the quantity that should spontaneously decrease over time in an isolated system (as per Second Law of Thermodyanmics).
0: Entropy is a measure of the average particle kinetic energy in a system.
0: Entropy is energy removed from a system per Kelvin.
1: Entropy is a measure of the floppiness of a bond.
1: The concept that disorder in a system will tend to increase and that this process is favorable.
2: Entropy is a measure of irreversibility."""

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

def score(a,b):
    s = 0.0
    a_tot = 0.0
    b_tot = 0.0
    for k in a.keys():
        a_tot += a[k]
    for k in b.keys():
        b_tot += b[k]

    for k in a.keys():
        if k in b:
            s += 1#a[k]*b[k]
    
    return s#/(a_tot*b_tot)

responses = []
grades = []
#f = open('responses.txt')
f = StringIO.StringIO(responses_txt)
for line in f:
    s = line.split(':')
    grades.append(int(s[0]))
    responses.append(s[1])
f.close()

bags = [bag_of_words(response) for response in responses]

def best(ans):
    bow = bag_of_words(ans) 
    best_score = 0
    best_res = ""
    for response in bags:
        s = score(bow, response)
        if s>best_score:
            best_score = s 
            best_res = response

    return best_res

def hint_fn(answer_ids, student_answers, new_cmap, old_cmap):
    aid = answer_ids[0]
    ans = str(student_answers[aid])
    
    hint = best(ans)

    hint = "&lt;font color='blue'&gt;{0}&lt;/font&gt;".format(hint)
    new_cmap.set_hint_and_mode(aid,hint,'always')

def init(ans):
    #ans = ans.strip("'")
    #ans = ans.strip('"')
    #
    #ret
    return best(ans)

if __name__ == '__main__':
    ans = 'disorder'
    print( init(ans) );

