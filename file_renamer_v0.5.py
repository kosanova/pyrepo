#!/usr/bin/python

#	File Renamer version 0.5
#	Michal Kosinski
#	Last modifcation: 14/10/2015

#   ./file_renamer.py dir_src file_type wanted_file_type base_name inc_begin
#   file_type, wanted_file_type - can be "all" (all in directory) instead of "xxx"
#   currently all arguments are expected

#   TODO windows version

#   for i in $(seq 1 25); do touch file${i}.txt; done #bash file make

import sys
import os
import datetime, time

t0 = time.time()

#   sys.argv[0] is a script name
script_name, dir_src, extension, new_extension, new_name, inc_begin = sys.argv # unpacking

def printTimeStamp():
    return " [" + str(datetime.datetime.now()) + "] "

def changeFileName(changed_name):
    os.rename(dir_src + file_name, dir_src + changed_name)
    print "%sFile %s has successfuly changed name to %s" % (printTimeStamp(), file_name, changed_name)

print "Executing %s..." % script_name.replace("./", "") 

file_counter = int(inc_begin)
dot_index = 0

if(os.path.exists(dir_src)):
    pass
else:
    print "Path doesn't exist!"
    quit()

print "Changing file names in %s\n" % dir_src

for file_name in os.listdir(dir_src):
    dot_index = file_name.rfind(".")
    if(dot_index > 0):
	    if((file_name[dot_index+1:] == extension or extension == "all") and new_extension != "all"): # change whole name
		    changed_name = new_name + str(file_counter) + "." + new_extension
		    file_counter += 1
		    changeFileName(changed_name)
	    elif(extension == "all" and new_extension == "all"): # change only name and counter
		    changed_name = file_name.replace(file_name[:dot_index], new_name + str(file_counter))
		    file_counter += 1
		    changeFileName(changed_name)
	    else:
	        print "%sSkipping file %s" % (printTimeStamp(), file_name)

    elif(dot_index == 0): # only for linux version
	    print "%sSkipping hidden file %s" % (printTimeStamp(), file_name)
    else:
        print "%sFile %s has no extension" % (printTimeStamp(), file_name)

print "\n***Finished in %.3fs***" % round(time.time() - t0, 3)
