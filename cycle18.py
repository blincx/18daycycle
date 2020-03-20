#!/usr/bin/env python
# 18 day cycle
from datetime import datetime,timedelta
import yaml, sys
import pprint



def loadconfig():
    with open(r'birthday.yaml') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

        return data["birthdate"]


def get_args():
    birfdae = None
    json = None
    print(f"len of sys.argv = {len(sys.argv)}")
    if len(sys.argv)==1:
        # for personal use, set birthday.yaml:birthdate
        # and call with no args
        birfdae = loadconfig()
        json = False
        print("A01")
    elif len(sys.argv)==2:
        if sys.argv[1]=="help":
            helptext = """Please call cycle18 with the relevant birthdate in the following format: MM-DD-YY, adding 'json' as a second argument if you want output in JSON."""
            print(helptext)                    
            print("A02")
            sys.exit(0)
        birfdae = sys.argv[1]
        print("A0333")
        json = False
    elif len(sys.argv)==3:
        birfdae = sys.argv[1]
        json = (sys.argv[2].lower()=='json')
        print("A03")
    print(f"birfdae is {birfdae}")
    print(f"json is {json}")
    return (birfdae, json)


def check_date(birthday):
    try:
        StartDate = datetime.strptime(birthday, "%m-%d-%y")
        return StartDate
    except Exception as e:
        raise e


def cycle_up(first_date,multiple):
    new_first_date = first_date + timedelta(days=(18*multiple))
    # nota bene: go one day beyond, to start the new cycle
    return new_first_date



def cycle_up_to_last_month(first_date):
    date_to_check = first_date 
    fdlm = first_day_of_last_month = (datetime.today().replace(day=1) - timedelta(days=1)).replace(day=1)

    # loop through adding 18 days until date_to_check hits prior month
    while fdlm.year != date_to_check.year:
        # loop up 18 days
        date_to_check = cycle_up(date_to_check,1)

    while fdlm.month != date_to_check.month:
        date_to_check = cycle_up(date_to_check,1)

    totaldays = (date_to_check-first_date).days

    # check if its cleanly divisible by 18, remainder should = 0
    if (totaldays % 18) != 0:
        raise "You broken the calculation machinery!"

    first_day_1_last_month = date_to_check
    return first_day_1_last_month


def build_final_cycles_calendar_data(day1):
    two_weeks_in_future = datetime.now() + timedelta(days=14)
    calendar_data = []
    loop_date = day1
    day_of_cycle = 1
    while loop_date < two_weeks_in_future:
        calendar_data.append((loop_date.year,loop_date.month,loop_date.day,day_of_cycle))
        if day_of_cycle==18:
            day_of_cycle=1
        else: 
            day_of_cycle = day_of_cycle + 1
        loop_date = loop_date + timedelta(days=1)
    return calendar_data  


def main():
    birthday, json = get_args()
    startdate = check_date(birthday)
    print(startdate)
    first_day_1_last_month = cycle_up_to_last_month(startdate)
    aa = build_final_cycles_calendar_data(first_day_1_last_month)
    print(aa)
    sys.exit(1)


main()

fast_forward_to_recent_first_day = datetime.now()
# days from first day of 722 cycle to now
num_of_days_to_label = (datetime.now() - fast_forward_to_recent_first_day).days + 1 # + 1 because it needs to round up


day_collector = []
start_loop = fast_forward_to_recent_first_day
day_collector.append(("DATE","DAY IN CYCLE"))
counter = 1
day_collector.append((start_loop.strftime("%d/%m"), counter))
for dayindex in range(1,num_of_days_to_label):
    if counter==18: counter = 0 # reset
    counter += 1
    new_day = start_loop + timedelta(days=1)
    start_loop = new_day
    day_collector.append((new_day.strftime("%d/%m"),counter))
    todays_value_in_cycle = counter

prettybar = "=========================="
print(f"\n{prettybar}")
print(f"DAY - DAY IN CYCLE\n{prettybar}")
for day,day_in_cyc in day_collector[-10:]:
    print(f"{day} - {day_in_cyc}")
print(f"{prettybar}")


