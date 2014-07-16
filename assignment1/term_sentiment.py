import sys
import json

known_scores = {}
term_scores = {}
term_freq = {}
tweets = []

def main():
    global known_scores, term_scores, term_freq, tweets
    with open(sys.argv[1], 'r') as sent_file:
        for line in sent_file:
            term, score = line.split('\t')
            known_scores[term] = int(score)
    with open(sys.argv[2], 'r') as tweet_file:
        for line in tweet_file:
            tweets.append(json.loads(line))
    for tweet in tweets:
        key = u'text'
        if key in tweet:
            score = 0
            words = tweet[key].split()
            for word in words:
                if word in known_scores:
                    score += known_scores[word]
            for word in words:
                if word not in known_scores:
                    if word not in term_scores:
                        term_scores[word] = 0.0
                        term_freq[word] = 0
                    term_scores[word] += float(score)/len(words)
                    term_freq[word] += 1
    for term in term_scores:
        print term, term_scores[term] / term_freq[term]

if __name__ == '__main__':
    main()
