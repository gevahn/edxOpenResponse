import sanitize
from bow_classifier import score

responses = []
grades = []
f = open('responses.txt')
for line in f:
    s = line.split(':')
    grades.append(int(s[0]))
    responses.append(s[1])
f.close()
print grades
bags = [sanitize.bag_of_words(response) for response in responses]

print "What is entropy?"
trial = raw_input()
print
print

trial_bag = sanitize.bag_of_words(trial)
print trial_bag
print
scores = []
for i in range(len(bags)):
    scores.append(score(bags[i], trial_bag))


sorter = sorted(range(len(scores)), key = lambda k: scores[k])
sorter = sorter[::-1]

for i in range(len(bags)):
    print scores[sorter[i]],":  ", responses[sorter[i]]
#print responses[sorter[0]]
