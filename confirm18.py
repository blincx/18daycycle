#!/usr/bin/env python3

# confirm18.py

# script to double check 18daycycle.py
import sys, copy, logging
from datetime import datetime,timedelta

#def setup(birthd=sys.argv[1]):
#    birthday = datetime.strptime(birthd, "%Y-%m-%d")
#    # very important to replace seconds and microseconds with 0
#    today = clean_today()
#    # the above line is VERY, VERY IMPORTANT
#    return (birthday,today)


def clean_today():
    return datetime.now().replace(second=0, microsecond=0,minute=0,hour=0)

def format_date(datetime_obj):
    return datetime_obj.strftime("%Y/%m/%d")

def datetime_obj_from_string(date1):
    date_date = datetime.strptime(date1, "%Y-%m-%d")
    return date_date

def simple_loop_method(birthday,today):
    diff = (today - birthday).days
    newday = copy.copy(birthday)
    CYCLE_DAY = 1
    for i in range(1,diff+2):
        #print(newday)
        #print(today)
        if (newday==today):
            date_nice = format_date(newday)
            logging.debug(f"simple_loop_method returned: {date_nice}, {CYCLE_DAY}")
            return (date_nice, CYCLE_DAY)
        # increment
        newday = newday + timedelta(days=1)
        #print(i)
        if (CYCLE_DAY==18):
            CYCLE_DAY = 1
        else:
            CYCLE_DAY = CYCLE_DAY + 1
    logging.error("simple_loop_method failed") 
    raise "You triggered: The Apocalypse."       


def simple_subtraction_method(birthday,today):
    diff = (today - birthday).days # 234
    daytotal = copy.copy(diff)
    while (daytotal >= 18):
        daytotal = daytotal - 18
    # ok, doing a today - birthday operation
    # gives the amount of days between two days
    # non-inclusive - because it gets you from the END
    # of the first day to the START of the lasty day.
    # that is actually 1 day less than the entire span. 
    # hence, adding 1
    CYCLE_DAY = daytotal + 1 # think through this
    logging.debug(f"simple_subtraction_method returned: {CYCLE_DAY}")
    return CYCLE_DAY





#def main():
    #birthday,today = setup()
    #data = simple_loop_method(birthday,today)
    #data2 = simple_subtraction_method(birthday,today)
    #print(data)
    #print(data2)
    #return data
    
    #print(current_day_position)

#main()





    
