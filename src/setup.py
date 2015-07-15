import sys
import os
import ConfigParser

class Setup:
	""" This class does the setup for our wordcount process """
	def __init__(self, path, configfile):
		self.path = path
		self.configfile = configfile

	def cleanOutputFiles(self):
		""" Removes output files and intermediate directories from previous runs """
		for root, dirs, files in os.walk(self.path, topdown=False):
			for name in files:
				os.remove(os.path.join(root, name))
			for name in dirs:
				os.rmdir(os.path.join(root, name))

	def createShards(self):
		""" Create shards for intermediate output stage based on specifications in the config file """
		dirstructure= os.path.join(self.path,'intermediate')
		if not os.path.exists(dirstructure):
			os.makedirs(dirstructure)
		config = ConfigParser.RawConfigParser()
		config.read(self.configfile)
		numshards = config.getint('Shards','numshards')
		for i in range(0,numshards):
			nameshard = 'shard'+str(i)
			dirstructure =os.path.join(self.path, 'intermediate', config.get('Shards', nameshard))
			if not os.path.exists(dirstructure):
				os.makedirs(dirstructure)

if __name__=='__main__':
	if len(sys.argv) != 3:
		print "Insufficient input parameters"
	setup = Setup(sys.argv[1], sys.argv[2])
	setup.cleanOutputFiles()
	setup.createShards()