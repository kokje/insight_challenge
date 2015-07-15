import sys

class Count:
	""" This class takes raw input files and transforms them to dictionaries that are distributed
		across shards to enable parallel processing """
	def __init__(self, inputfile, outputpath, outputfile, seekpos):
		self.dictionary = {}
		self.inputfile = inputfile
		self.outputpath = outputpath
		self.outputfile = outputfile
		self.seekpos = seekpos

	def readTweets(self):
		""" Read batch tweets and construct a dictionary/hashtable using space delimited words """
		try:
			f = open(self.inputfile, 'r')
			f.seek(int(self.seekpos))
		except IOError:
			print 'Cannot open input file', self.inputfile 
		for line in f:
			words = line.split()
			for word in words:
				if self.dictionary.has_key(word):
					self.dictionary[word] += 1
				else:
					self.dictionary[word] = 1
		f.close()

	def writeWordCounts(self):
		""" Distribute the dictionary based on alphabetical order """
		for entry in self.dictionary:
			shard = ''
			if entry[0] == ':' or entry[0] == '@' or entry[0] == '#':
				shard = '/characters/'
			if entry[0].isdigit():
				shard = '/numbers/'
			if entry[0] >= 'a' and entry[0] <= 'j':
				shard = '/a_f/'
			if entry[0] >= 'k' and entry[0] <= 'r':
				shard = '/k_r/'
			if entry[0] >= 's' and entry[0] <= 'z':
				shard = '/s_z/'
			if (shard != ''):
				try:
					f = open(self.outputpath+shard+self.outputfile, 'a')
					f.write(entry+' '+str(self.dictionary[entry])+'\n')
					f.close()
				except IOError:
					print 'Error writing to output file', self.outputfile

if __name__=='__main__':
	if len(sys.argv) != 5:
		print "Insufficient input parameters"
	counter = Count(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	counter.readTweets()
	counter.writeWordCounts()
