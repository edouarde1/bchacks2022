import math
import sys
import json

negWords = []
posWords = []
with open('negative-words.txt', 'r') as file:
    negWords = file.read().splitlines()
with open('positive-words.txt', 'r') as file:
    posWords = file.read().splitlines()

def score(str):
	count = 0
	negCount = 0
	posCount = 0
	neg = []
	pos = []
	for word in str.split():
		word = word.lower()
		count += 1
		if word in posWords:
			posCount += 1
			pos.append(word)
		elif word in negWords:
			negCount += 1
			neg.append(word)
	if count == 0:
		w = 0
	else:
		w = (posCount - negCount) / math.sqrt(count) * 100
	return {
    	"score" : posCount - negCount,
    	"weightedScore" : w,
    	"posWords" : pos,
		"negWords" : neg,
	}

print(json.dumps(score(sys.argv[1])))
sys.stdout.flush()




