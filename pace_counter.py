#!/usr/bin/python

#add options like halfmarathon, marathon, negativesplit - use a proper library

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--distance", help = "The distance to run", type = float)
parser.add_argument("time", help = "Goal time")
parser.add_argument("-m", "--marathon", help = "The marathon distance", action = "store_true")
parser.add_argument("-hm", "--halfmarathon", help = "The half-marathon distance", action = "store_true")
args = parser.parse_args()

if args.marathon:
    distance = 42.195
elif args.halfmarathon:
    distance = 21.0975
else:
    distance = args.distance
    
time = args.time

#returns time in seconds
def parseTime(str_time):
    delimiter_right_idx = str_time.rfind(':')
    delimiter_left_idx = str_time.find(':')
    
    hours = str_time[:delimiter_left_idx]
    minutes = str_time[delimiter_left_idx+1:delimiter_right_idx]
    seconds = str_time[delimiter_right_idx+1:]

    return int(hours)*60*60 + int(minutes)*60 + int(seconds)

#returns pace time in seconds  
def countPace():
    return int(float(parseTime(time)) / distance)

#returns formatted pace time
def convertTime(ts):
    minutes = str(ts / 60)
    seconds = str(ts % 60)
    if int(seconds) < 10:
        seconds = "0" + seconds
    return minutes + ":" + seconds

def summary():
    print "Distance:", str(distance) + "km"
    print "Time:", time
    print "Pace:", convertTime(countPace())

summary()
