#!/usr/bin/env python3
# confirm18.py
# script to double check 18daycycle.py


import sys, copy, logging
from datetime import datetime,timedelta

logging.basicConfig(format='%(asctime)s %(message)s',filename='logs/18daycycle.log', level=logging.DEBUG)


def clean_today():
    return datetime.now().replace(second=0, microsecond=0,minute=0,hour=0)

def date_string_from_obj(datetime_obj):
    return datetime_obj.strftime("%Y/%m/%d")

def readable_date(datetime_obj):
    return datetime_obj.strftime("%B %d")

def datetime_obj_from_string(datestring):
    date_date = datetime.strptime(datestring, "%Y-%m-%d")
    return date_date

def simple_loop_method(birthday,today):
    diff = (today - birthday).days
    newday = copy.copy(birthday)
    CYCLE_DAY = 1
    # diff above non-inclusive
    for i in range(1,diff+2):
        if (newday==today):
            date_nice = date_string_from_obj(newday)
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



def forward_ten(cycle_day,today):
    ten_forward = []
    ten_forward.append((readable_date(today),cycle_day))
    
    for i in range(1,11): #1-10
        if (i==1):
            newday = today + timedelta(days=1)
        else:
            newday = newday + timedelta(days=1)
        if (cycle_day==18):
            cycle_day = 1
        else:
            cycle_day = cycle_day + 1
        ten_forward.append((readable_date(newday),cycle_day))
    return ten_forward










    
