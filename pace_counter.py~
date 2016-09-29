#!/usr/bin/python

#add options like halfmarathon, marathon, negativesplit - use a proper library

import sys
import argparse

script_name, distance, time = sys.argv

parser = argparse.ArgumentParser()
parser.parse_args()


#returns time in seconds
def parseTime(str_time):
    delimiter_right_idx = str_time.rfind(':')
    delimiter_left_idx = str_time.find(':')
    
    hours = str_time[:delimiter_left_idx]
    minutes = str_time[delimiter_left_idx+1:delimiter_right_idx]
    seconds = str_time[delimiter_right_idx+1:]
    
    #print delimiter_right_idx, delimiter_left_idx 
    #print hours, minutes, seconds
    return int(hours)*60*60 + int(minutes)*60 + int(seconds)
  
#return pace time in seconds  
def countPace():
    return int(float(parseTime(time)) / float(distance))
    
#returns formatted pace time
def convertTime(ts):
    minutes = str(ts / 60)
    seconds = str(ts % 60)
    if int(seconds) < 10:
        seconds = "0" + seconds
    return minutes + ":" + seconds

def summary():
    print "Distance:", distance + "km"
    print "Time:", time
    print "Pace:", convertTime(countPace())

summary()
