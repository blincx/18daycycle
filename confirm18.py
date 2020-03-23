#!/usr/bin/env python3

# confirm18.py

# script to double check 18daycycle.py
import sys, copy
from datetime import datetime,timedelta

def setup():
    birthd = sys.argv[1]
    birthday = datetime.strptime(birthd, "%Y-%m-%d")
    # very important to replace seconds and microseconds with 0
    today = datetime.now().replace(second=0, microsecond=0,minute=0,hour=0)
    # the above line is VERY, VERY IMPORTANT
    totaldays = (today - birthday).days
    return (birthday,today,totaldays)



def format_date(datetime_obj):
    return datetime_obj.strftime("%Y/%m/%d")

def simple_loop_method(birthday,today):
    diff = (today - birthday).days
    newday = copy.copy(birthday)
    CYCLE_DAY = 1
    for i in range(1,diff+2):
        #print(newday)
        #print(today)
        if (newday==today):
            return (format_date(newday), CYCLE_DAY)
        # increment
        newday = newday + timedelta(days=1)
        #print(i)
        if (CYCLE_DAY==18):
            CYCLE_DAY = 1
        else:
            CYCLE_DAY = CYCLE_DAY + 1
    raise "You triggered: The Apocalypse."       




def main():
    birthday,today,totaldays = setup()
    test = simple_loop_method(birthday,today)
    print(test)
    
    assert(newdiff ==(today - birthday).days - daydiff_until_last_day_18);
    new_modulo = newdiff%18
    print(new_modulo)
    assert(new_modulo==0)
    print("if you got here, it worked")




    #current_day_position = get_current_day_position_in_cycle_modulo_method(birthday,today,totaldays)
    #print(current_day_position)

main()





    
