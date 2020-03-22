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
    return (birthday,today,totaldays)

def get_current_day_position_in_cycle_modulo_method(birthday,today,totaldays):
    daycount = copy.copy(totaldays)   
    while (daycount % 18): # exits when 18th day is hit
        daycount = daycount - 1
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
        if (counter==18): # shouldn't ever happen
            raise "Something is frigged. Get on my level."
        else:
            counter = counter + 1
   
    current_day_in_cycle = day_list[-1]["cycleposition"] # last entry=today
    return current_day_in_cycle


def test_modulo(birthday,today):
    found_last_18th_day = False
    last_18th_day = None
    loopy_day = copy.copy(today)
    # loop through days, starting with today
    while not found_last_18th_day:
        days_from_birthday = (loopy_day - birthday).days
        modulo = days_from_birthday%18
        # is it the 18th day?
        if (modulo==0):
            found_last_18th_day = True
            last_18th_day = copy.copy(loopy_day)
        else:
            # go back another day
            loopy_day = loopy_day - timedelta(days=1)
    

    last_1st_day = last_18th_day + timedelta(days=1)
    did_we_reach_today = False
    another_loopy_day = copy.copy(last_1st_day)
    CURRENT_CYCLE_DAY = 1
    # now cycle forward till we hit today
    while (did_we_reach_today==False):
        if (another_loopy_day==today):        
            did_we_reach_today = True
            return CURRENT_CYCLE_DAY
        elif (CURRENT_CYCLE_DAY==18):
            raise "You broke me. Get on my level."
        else:
            # increment day
            another_loopy_day = another_loopy_day + timedelta(days=1)
            # increment CURRENT_CYCLE_DAY
            CURRENT_CYCLE_DAY = CURRENT_CYCLE_DAY + 1

    raise "Shouldn't have gotten here. Somethings broken."


    assert(newdiff ==(today - birthday).days - daydiff_until_last_day_18);
    new_modulo = newdiff%18
    print(new_modulo)
    assert(new_modulo==0)
    print("if you got here, it worked")




def main():
    birthday,today,totaldays = setup()
    test = test_modulo(birthday,today)
    print(test)
    #current_day_position = get_current_day_position_in_cycle_modulo_method(birthday,today,totaldays)
    #print(current_day_position)

main()
