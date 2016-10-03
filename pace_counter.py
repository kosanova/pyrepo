#!/usr/bin/python

# TODO list
#
# implement option negativesplit
# learn how to parse an xml file in the best way
# parse several tcx files, think of chart framework to visualize the progress (all of them already downloaded into dropbox)
# https://tapiriik.com/
# refactor project, maybe OOP?
# web presentation - Django!
#
# last and the hardest task - try to login into endomondo and download all tcx files OR just navigate through the site and store time and distance info

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--distance", help = "The distance to run", type = float)
parser.add_argument("time", help = "Goal time, possible formats: hh:mm:ss, mm:ss")
parser.add_argument("-m", "--marathon", help = "The marathon distance", action = "store_true")
parser.add_argument("-hm", "--halfmarathon", help = "The half-marathon distance", action = "store_true")
args = parser.parse_args()

if args.marathon:
    DISTANCE = 42.195
elif args.halfmarathon:
    DISTANCE = 21.0975
else:
    DISTANCE = args.distance
    
TIME = args.time

# returns time in seconds
def parse_time(str_time):

    t = str_time.split(':')
    
    if len(t) == 3:
        return int(t[0]) * 60 * 60 + int(t[1]) * 60 + int(t[2])
    elif len(t) == 2:
        return int(t[0]) * 60 + int(t[1])
    else:
        print "Wrong time format!\n"
        return -1 

# returns formatted pace time
def convert_time(ts):
    minutes = str(ts / 60)
    seconds = str(ts % 60)
    if int(seconds) < 10:
        seconds = "0" + seconds
    return minutes + ":" + seconds

# returns pace time in seconds  
def count_pace():
    t = parse_time(TIME)
    return int(float(t) / DISTANCE)

def summary():
    print "Distance:", str(DISTANCE) + "km"
    print "Time:", TIME
    pace = count_pace()
    print "Pace:", convert_time(pace)

summary()
