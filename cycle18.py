# 18 day cycle
from datetime import datetime,timedelta
import pprint

StartDate0 = "07/28/84"
StartDate = datetime.strptime(StartDate0, "%m/%d/%y")

def earliest_possible_first_day():
    today = datetime.now()
    earliest_possible_first_day = today - timedelta(days=18)
    return earliest_possible_first_day

def cycle_up(first_date,multiple):
    new_first_date = first_date + timedelta(days=(18*multiple))
    # nota bene: go one day beyond, to start the new cycle
    print(repr(new_first_date))
    return new_first_date

# 2/26/2020 - recent first day
fast_forward_to_recent_first_day = cycle_up(StartDate,721) # already experienced this many cycles

# days from first day of 722 cycle to now
num_of_days_to_label = (datetime.now() - fast_forward_to_recent_first_day).days + 1 # + 1 because it needs to round up

print(fast_forward_to_recent_first_day)
print(num_of_days_to_label)

day_collector = []
start_loop = fast_forward_to_recent_first_day
day_collector.append(("DATE","DAY IN CYCLE"))
counter = 1
day_collector.append((start_loop.strftime("%d/%m/%y"), counter))
for dayindex in range(1,num_of_days_to_label):
    counter += 1
    new_day = start_loop + timedelta(days=1)
    start_loop = new_day
    day_collector.append((new_day.strftime("%d/%m/%y"),counter))
#d.strftime("%d/%m/%y")
pprint.pprint(day_collector)






