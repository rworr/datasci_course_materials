import sys
import json

hash_freq = {}
tweets = []

def main():
    global hash_freq, tweets
    with open(sys.argv[1], 'r') as tweet_file:
        for line in tweet_file:
            tweets.append(json.loads(line))
    for tweet in tweets:
        key = u'entities'
        if key in tweet:
            hashkey = u'hashtags'
            if hashkey in tweet[key]:
                for hashtag in tweet[key][hashkey]:
                    if hashtag[u'text'] not in hash_freq:
                        hash_freq[hashtag[u'text']] = 0
                    hash_freq[hashtag[u'text']] += 1
    sortedHash = [(k, hash_freq[k]) for k in sorted(hash_freq, key=hash_freq.get, reverse=True)]
    for hashcount in sortedHash[:10]:
        print hashcount[0], hashcount[1]

if __name__ == '__main__':
    main()
