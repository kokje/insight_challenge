#!/usr/bin/env bash
python ./src/wordcount.py ./tweet_input ./tweet_output ./src/wordcount.ini

#Minimum number of unique words in a tweet is 1 and maximum number of unique words in a tweet is 140. Therefore we can represent count of uniques words in an in-memory hashtable
python ./src/median.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt