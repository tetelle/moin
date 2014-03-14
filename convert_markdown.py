from pandocfilters import toJSONFilter, Emph, Para, Str
from os import listdir
from os.path import isfile, join
import os
import sys
import subprocess

def behead(key, value, format, meta):
  if key == 'Header' and value[0] >= 2:
    return Para([Emph(value[2])])
# call this function toJSONFilter(behead)

def convert (filename,path):
	print "Converting...",path,filename 
	#options = ['pandoc', '-t', 'native',path+"/"+filename]
	name = filename[0:len(filename)-5] # without the extension .wiki
	options = ['pandoc','-f','mediawiki','-t','markdown','-s',join(path,filename),'-o',join(path,name + ".md")]
	print options
	subprocess.call(options)
	print "Done"


if len(sys.argv)<2:
	print "You need to pass an argument in the comand line"
else:
	if os.path.exists(sys.argv[1]):
		# find all files in this directory
		files = [ f for f in listdir(sys.argv[1]) if isfile(join(sys.argv[1],f)) ]
		print files
		print "****"
		for i in range(len(files)):
			if files[i].endswith(".wiki"):
				convert(files[i],sys.argv[1])
	else:
		print "Sorry this path doesn\'t exist."

