import sys
import json

term_freq = {}
tweets = []

def main():
    global term_freq, tweets
    with open(sys.argv[1], 'r') as tweet_file:
        for line in tweet_file:
            tweets.append(json.loads(line))
    for tweet in tweets:
        key = u'text'
        if key in tweet:
            words = tweet[key].split()
            for word in words:
                if word not in term_freq:
                    term_freq[word] = 0
                term_freq[word] += 1
    for term in term_freq:
        print term, term_freq[term]

if __name__ == '__main__':
    main()
