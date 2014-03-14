import sys
import os
from os import listdir
from os.path import isfile, join


""" We don't need this function to remove formatting use Pandoc instead...."""
def remove_formatting(text):
	ignore = ['_','{','}',',','-','\'','^','[',']','|']
	unformatted = ''
	for i in range(len(text)):
		if text[i] not in ignore:
			unformatted += text[i]
	return unformatted		


if len(sys.argv)<3:
	print "Argument missing in the command line. Usage python main_content.py <page name> , <dir moinmoin>" 
else:
	# argv[2] is where moinmoin is installed and where the wiki goes
	if os.path.exists(sys.argv[2]):
		loc = sys.argv[2] + "/wiki/data/pages/" + sys.argv[1] + "/revisions"
		if os.path.exists(loc): # get most recent file, file names are like 001,002,003...
			files = [ f for f in listdir(loc) if isfile(join(loc,f)) ]
			latest_file = sorted(files,reverse=True)[0] # first argument of sorted list (highest number)
			try:
				f = open(join(loc,latest_file), 'r')
				contents = f.read()
				output_loc = sys.argv[2] + "/wiki/data/output"  
				# save results in /output/ .rst if the directory /output does not exit, create it
				if not os.path.exists(output_loc):
					os.makedirs(output_loc)
				output_filename = output_loc + "/" + sys.argv[1] + ".wiki" #.rst
				fo = open(output_filename, "wb")
				fo.write(contents)
				fo.close()
				#print contents
				f.close()
   			except IOError:
   				print "File" + latest_file + "does not exist."
		else:
			print "cannot see wiki"
	else:
		print "Error path - check where Moinmoin has been installed"

