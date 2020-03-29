#!/usr/bin/env python3
# 18 day cycle
from datetime import datetime,timedelta
import yaml, sys, json
import pprint
import logging
from confirm18 import simple_loop_method, simple_subtraction_method
from confirm18 import clean_today, readable_date, datetime_obj_from_string
from confirm18 import date_string_from_obj, forward_ten


DEBUGSWITCH = False # change if you want to turn it on from script

DEBUG = ("debug" in sys.argv) or DEBUGSWITCH
if DEBUG:
    logging.basicConfig(format='%(asctime)s %(message)s',filename='logs/18daycycle.log', level=logging.DEBUG)
else:
    logging.basicConfig(format='%(asctime)s %(message)s', filename='logs/18daycycle.log', level=logging.ERROR)

logging.basicConfig()


def loadconfig():
    with open(r'birthday.yaml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return str(data["birthdate"])


def get_args():
    birfdae = None
    json_flag = None
    if len(sys.argv)==1:
        # for personal use, set birthday.yaml:birthdate
        # and call with no args
        birfdae = loadconfig()
        json_flag = False
    elif len(sys.argv)==2:
        if ("help" in sys.argv):
            helptext = """Please call 18daycycle with the relevant birthdate in the following format: YYYY-MM-DD, adding 'json' as a second argument if you want output in JSON."""
            print(helptext)                    
            sys.exit(0)
        if ("-" in sys.argv[1]):
            birfdae = sys.argv[1]
        json_flag = False
    elif len(sys.argv) == 3:
        birfdae = sys.argv[1]
        json_flag = ("json" in sys.argv)
    logging.debug(f"get_args returned: birfdae={birfdae} json_flag={json_flag}")
    return (birfdae, json_flag)



def cycle_up(first_date,multiple):
    new_first_date = first_date + timedelta(days=(18*multiple))
    # nota bene: go one day beyond, to start the new cycle
    return new_first_date


def cycle_up_to_last_month(first_date):
    date_to_check = first_date
    # first day of last month
    fdlm = (datetime.today().replace(day=1) - timedelta(days=1)).replace(day=1)

    # loop through adding 18 days until date_to_check hits prior month
    while fdlm.year != date_to_check.year:
        # loop up 18 days
        date_to_check = cycle_up(date_to_check, 1)

    while fdlm.month != date_to_check.month:
        date_to_check = cycle_up(date_to_check, 1)

    totaldays = (date_to_check-first_date).days

    # check if its cleanly divisible by 18, remainder should = 0
    if (totaldays % 18) != 0:
        logging.error(f"we cycled up and got a number that doesn't divide cleanly by 18: {totaldays}")
        raise Exception("You broken the calculation machinery!")

    first_day_1_last_month = date_to_check
    logging.debug(f"cycle_up returned {first_day_1_last_month}")
    return first_day_1_last_month


def build_final_cycles_calendar_data(day1):
    logging.debug("calling build_final_cycles_calendar_data")
    today = None
    two_weeks_in_future = clean_today() + timedelta(days=14)
    day_collector = [] # for text stdout output
    day_collector.append(("DATE","DAY IN CYCLE"))
    loop_date = day1
    day_of_cycle = 1
    while loop_date < two_weeks_in_future:
        day_collector.append((loop_date.strftime("%B %d"),day_of_cycle))
        # if today, populate var with day_of_cycle
        if loop_date.day==clean_today().day and loop_date.month==clean_today().month:
            today = day_of_cycle
        if day_of_cycle==18:
            day_of_cycle=1
        else: 
            day_of_cycle = day_of_cycle + 1
        loop_date = loop_date + timedelta(days=1)
    return day_collector



def print_to_screen(data):
    prettybar = "=========================="
    print(f"\n{prettybar}")
    print(f"DAY - DAY IN CYCLE\n{prettybar}")
    for day,day_in_cyc in data:
        print(f"{day} - {day_in_cyc}")
    print(f"{prettybar}")


def main():
    birthday0, json_flag = get_args()
    birthday = datetime_obj_from_string(birthday0)
    today = clean_today()
    todayconfirm,CYCLE_DAY = simple_loop_method(birthday,today)
    CYCLE_DAYconfirm = simple_subtraction_method(birthday,today)
    if (CYCLE_DAYconfirm != CYCLE_DAY):
        logging.error(f"Wrench apocalypse 1! simple_loop_method returned {CYCLE_DAY} and simple_subtraction_method returned {CYCLE_DAY}!")
        raise Exception("Apocalyptic errors! - Get into heaven you bastards!")

    daydata = forward_ten(CYCLE_DAY,today)
    logging.debug(f"returned vars: today={today};\ndaydata={daydata};")
    if not json_flag:
        if DEBUG:
            print("Hey! You're in DEBUG mode!")
        print_to_screen(daydata)
    elif json_flag:
        abba = json.dumps({"today": CYCLE_DAY,"daydata":daydata})
        print(abba) # this is necessary
    logging.info(f"script called with args: {sys.argv}; birthday={birthday}; json_flag={json_flag}; today={today};")
    logging.info(f"resulting output: cycle_day={CYCLE_DAY} daydata={daydata}")




def old_main():
    print("AND ALSO, BY ANOTHER METHOD OF CALCULATION:\n")
    birthday, json_flag = get_args()
    startdate = datetime_obj_from_string(birthday)
    first_day_1_last_month = cycle_up_to_last_month(startdate)
    day_collector = build_final_cycles_calendar_data(first_day_1_last_month)
    # today 
    today = clean_today()
    logging.debug(f"returned vars: today={today};day_collector={day_collector};")
    if not json_flag:
        print_to_screen(day_collector[-14:-3])
    elif json_flag:
        abba = json.dumps({"today": today, "daydata":day_collector[-15:-2]})
        print(abba) # this is necessary
    logging.info(f"script called with args: {sys.argv}; birthday={birthday}; json_flag={json_flag}; startdate={startdate}; first_day_1_last_month={first_day_1_last_month}; today={today};")

if __name__ == '__main__':
    main()
    #print("\n")
    #old_main()

