import sys

uniquewordcounts = [0] * 140

def readTweets(inputfile, outputfile):
	""" Read tweets and use a hashmap with entries as count of unique words to determine median """
	try:
		f = open(inputfile, 'r')
		o = open(outputfile, 'w')
		count = 0
		for tweet in f:
			#Read tweets and use a set to get count of unique words
			words = set(tweet.split())
			numuniquewords = len(words)
			#Add this count to the hashtable
			uniquewordcounts[numuniquewords] += 1
			#Keep a count of number of tweets so far
			count += 1
			getMedian(count, o)
	except IOError:
		print "Unexpected error"
	f.close()
	o.close


def getMedian(count, o):
	""" Compute median value from the frequency hashtable for total number of tweets n """
	sum = 0
	medianval = int(count / 2) + 1
	# Need to know previous non zero value when n is even
	prevval = 0
	for i in range(1, 20):
		sum += uniquewordcounts[i]
		# If n is even, median is avg of n/2 and n/2 + 1
		if count % 2 == 0:
			if sum >= medianval:
				if uniquewordcounts[i] == 1:
					median = float(prevval + i) / 2
					o.write("%.2f\n" % median)
					break
				else:
					o.write("%.2f\n" % i)
					break
			if uniquewordcounts[i] != 0:
				prevval = i
		# If n is odd, median is n/2 + 1
		else:
			if sum >= medianval:
				o.write("%.2f\n" % i)
				break


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Insufficient input parameters"
	readTweets(sys.argv[1],sys.argv[2])
