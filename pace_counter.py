#!/usr/bin/python

# TODO list
#
# implement option negativesplit and visualize it on the chart
# learn how to parse an xml file in the best way
# refactor project, maybe OOP?
# web presentation - Django!
#
# last and the hardest task - try to login into endomondo and download all tcx files
# OR just navigate through the site and store time and distance info

import argparse

global DISTANCE
global TIME

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--distance", help = "The distance to run", type = float)
parser.add_argument("time", help = "Goal time, possible formats: hh:mm:ss, mm:ss")
parser.add_argument("-m", "--marathon", help = "The marathon distance", action = "store_true")
parser.add_argument("-hm", "--halfmarathon", help = "The half-marathon distance", action = "store_true")
parser.add_argument("-n", "--negativesplit", help = "Print out the negative split strategy")#, action = "store_true")
args = parser.parse_args()


if args.marathon:
    DISTANCE = 42.195
elif args.halfmarathon:
    DISTANCE = 21.0975
else:
    DISTANCE = args.distance

if args.negativesplit:
    FIRST_LAP = args.negativesplit
    
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
        exit() 

# returns formatted pace time
def convert_time(ts):
    minutes = str(ts / 60)
    seconds = str(ts % 60)
    if int(seconds) < 10:
        seconds = '0' + seconds
    return minutes + ':' + seconds

# returns pace time in seconds  
def count_pace():
    t = parse_time(TIME)
    return int(float(t) / DISTANCE)

def negative_split():
    # for testing, later as an argument
    first_lap = parse_time(FIRST_LAP)
    print "First lap", first_lap
    fake_time = first_lap * DISTANCE # 50
    print "Fake time", fake_time
    last_lap = (parse_time(TIME) - first_lap) / (DISTANCE - 1) # (45 - 5) / 10 = 4
    print "Last lap", last_lap
    diff = (first_lap - last_lap) / (DISTANCE - 1) # 6.6667
    print "Diff", diff
    table = [first_lap]
    for i in range (1,int(DISTANCE)):
        first_lap -= diff
        table.append(first_lap)

    return table;

def parse_pace_table(table):
    suma = 0
    i = 0
    for t in table:
        t = int(t)
        #print t
        i += 1
        print i, '\t', convert_time(t)
    print parse_time(TIME)
    print float(sum(table))
    print "Deviation", parse_time(TIME) - (float(sum(table)))
    
def summary():
    print "Distance:", str(DISTANCE) + "km"
    print "Time:", TIME
    pace = count_pace()
    print "Pace:", convert_time(pace)
    if args.negativesplit:
       # t = negative_split()
        print "Pace strategy:\n", parse_pace_table(negative_split())#negative_split()

summary()
