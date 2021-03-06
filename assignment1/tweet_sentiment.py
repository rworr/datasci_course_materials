import json
import sys

scores = {}
tweets = []

def main():
    global scores, tweets
    with open(sys.argv[1], 'r') as sent_file:
        for line in sent_file:
            term, score = line.split('\t')
            scores[term] = int(score)
    with open(sys.argv[2], 'r') as tweet_file:
        for line in tweet_file:
            tweets.append(json.loads(line))
    for tweet in tweets:
        key = u'text'
        if key in tweet:
            score = 0
            words = tweet[key].split()
            for word in words:
                if word in scores:
                    score += scores[word]
            print score

if __name__ == '__main__':
    main()
