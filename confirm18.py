#!/usr/bin/env python3

# confirm18.py

# script to double check 18daycycle.py
import sys, copy
from datetime import datetime,timedelta

def setup():
    birthd = sys.argv[1]
    birthday = datetime.strptime(birthd, "%Y-%m-%d")
    today = datetime.now()
    totaldays = (today - birthday).days
    return totaldays

def get_current_day_position_in_cycle_modulo_method(today,totaldays):
    daycount = copy.copy(totaldays)   
    while (daycount % 18): # exits when 18th day is hit
        daycount = daycount - timedelta(days=1)
    last_day_1 = birthday + timedelta(days=(daycount+1))
    loop_day = copy.copy(last_day_1)
    
    day_list = []
    counter = 1
    finalcounter = None
    while (loop_day <= today):
        # add to list
        day_list.append({"date":loop_day,"cycleposition":counter})
        #increment day
        loop_day = loop_day + timedelta(days=1)
        #increment counter
        if counter==18: # shouldn't ever happen
            raise "Something is frigged. Get on my level."
        else:
            counter = counter + 1
   
   current_day_in_cycle = day_list[-1]["cycleposition"] # last entry=today

   return current_day_in_cycle

