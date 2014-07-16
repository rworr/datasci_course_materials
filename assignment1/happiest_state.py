import json
import sys

scores = {}
tweets = []
states = {}

def main():
    global scores, tweets, states
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
        tweet[u'score'] = score
    for tweet in tweets:
        key = u'place'
        if key in tweet and tweet[key]:
            if tweet[key][u'country_code'] == u'US':
                city, state = tweet[key][u'full_name'].split(',')
                state = state.strip()
                if state != u'USA':
                    if state not in states:
                        states[state] = 0
                    states[state] += tweet[u'score']
    sortedList = [k for k in sorted(states, key=states.get, reverse=True)]
    print sortedList[0]

if __name__ == '__main__':
    main()
