#!/usr/bin/env python3
# 18 day cycle
from datetime import datetime,timedelta
import yaml, sys, json
import pprint
import logging

DEBUG = False
if DEBUG:
    logging.basicConfig(filename='logs/18daycycle.log', level=logging.DEBUG)
else:
    logging.basicConfig(filename='logs/18daycycle.log', level=logging.INFO)


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
        if sys.argv[1]=="help":
            helptext = """Please call cycle18 with the relevant birthdate in the following format: YYYY-MM-DD, adding 'json' as a second argument if you want output in JSON."""
            print(helptext)                    
            sys.exit(0)
        birfdae = sys.argv[1]
        json_flag = False
    elif len(sys.argv) == 3:
        birfdae = sys.argv[1]
        json_flag = (sys.argv[2].lower() == 'json')
    logging.debug(f"get_args returned: birfdae={birfdae} json_flag={json_flag}")
    return (birfdae, json_flag)


def check_date(birthday):
    StartDate = datetime.strptime(birthday, "%Y-%m-%d")
    logging.debug(f"received date: {birthday}")
    return StartDate


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
        raise "You broken the calculation machinery!"

    first_day_1_last_month = date_to_check
    logging.debug(f"cycle_up returned {first_day_1_last_month}")
    return first_day_1_last_month


def build_final_cycles_calendar_data(day1):
    logging.debug("calling build_final_cycles_calendar_data")
    today = None
    two_weeks_in_future = datetime.now() + timedelta(days=14)
    calendar_data = [] # for json_flag output
    day_collector = [] # for text stdout output
    day_collector.append(("DATE","DAY IN CYCLE"))
    loop_date = day1
    day_of_cycle = 1
    while loop_date < two_weeks_in_future:
        calendar_data.append((loop_date.year,loop_date.month,loop_date.day,day_of_cycle))
        day_collector.append((loop_date.strftime("%B %d"),day_of_cycle))
        # if today, populate var with day_of_cycle
        if loop_date.day==datetime.now().day and loop_date.month==datetime.now().month:
            today = day_of_cycle
        if day_of_cycle==18:
            day_of_cycle=1
        else: 
            day_of_cycle = day_of_cycle + 1
        loop_date = loop_date + timedelta(days=1)
    return (today,calendar_data,day_collector)



def print_to_screen(data):
    prettybar = "=========================="
    print(f"\n{prettybar}")
    print(f"DAY - DAY IN CYCLE\n{prettybar}")
    for day,day_in_cyc in data[-16:-12]:
        print(f"{day} - {day_in_cyc}")
    print(f"{prettybar}")



def main():
    birthday, json_flag = get_args()
    startdate = check_date(birthday)
    first_day_1_last_month = cycle_up_to_last_month(startdate)
    today,calendar_data,day_collector = build_final_cycles_calendar_data(first_day_1_last_month)
    # today 
    logging.debug(f"returned vars: today={today};\ncalendar_data={calendar_data};")
    if not json_flag:
        print_to_screen(day_collector)
    elif json_flag:
        #abba = json.dumps({"today": today, "caldata":calendar_data,"daydata":day_collector[-15:-2]})
        abba = json.dumps({"today": today, "caldata":calendar_data,"daydata":day_collector[-15:-2]})
        print(abba) # this is necessary
    logging.info(f"script called with args: {sys.argv}; birthday={birthday}; json_flag={json_flag}; startdate={startdate}; first_day_1_last_month={first_day_1_last_month}; today={today};")
    sys.exit(0)


main()


