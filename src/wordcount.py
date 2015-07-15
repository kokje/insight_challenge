import subprocess
import sys
import os

def setupAndTeardown():
	try:
		subprocess.check_call('python ./src/setup.py ./tweet_output ./src/wordcount.ini',shell=True)
	except subprocess.CalledProcessError, e:
		return 1
	return 0

def countOccurences(inputfile,numprocs,seeklength):
	start = 0
	for i in range(0,numprocs):
		try:
			subprocess.check_call('python ./src/count.py '+inputfile+' ./tweet_output/intermediate out'+ str(i) +'.txt'+' '+ str(start), shell=True)
			start += seeklength
		except subprocess.CalledProcessError, e:
			print "Process", i," failed"
			return 1
	return 0

def sortIntermediates(shards):
	for shard in shards:
		try:
			subprocess.check_call('python ./src/sort.py ./tweet_output/intermediate/'+shard+' sorted_output.txt', shell=True)
		except subprocess.CalledProcessError, e:
			print "Process", i," failed"
			return 1
	return 0

def combineIntermediateOutput(shards):
	for shard in shards:
		try:
			if os.path.exists('./tweet_output/intermediate/'+shard+'/sorted_output.txt'):
				subprocess.check_call('cat ./tweet_output/intermediate/'+shard+'/sorted_output.txt >> ./tweet_output/f1.txt', shell=True)
		except subprocess.CalledProcessError, e:
			print "Process", i," failed"
			return 1
	return 0

if __name__=='__main__':
	if len(sys.argv) != 4:
		print "Insufficient input parameters"
	inputfile = sys.argv[1]
	# Use size of the input file and the number of processes to determine positions to read from in the file
	size = os.path.getsize(inputfile)
	numprocs = 3
	seeklength = size/numprocs

	#Shards are currently hardcoded
	#TODO: Incorporate dynamic shards which are setup using configuration script
	shards = ["characters","numbers","a_f","k_r","s_z"]
	assert setupAndTeardown() == 0
	assert countOccurences(inputfile,numprocs,seeklength) == 0
	assert sortIntermediates(shards) == 0
	assert combineIntermediateOutput(shards) == 0
	