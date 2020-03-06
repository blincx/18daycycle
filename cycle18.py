# 18 day cycle
from datetime import datetime,timedelta

StartDate0 = "07/28/84"
StartDate = datetime.strptime(StartDate0, "%m/%d/%y")

def cycle_up(first_date,multiple):
    new_first_date = first_date + timedelta(days=(18*multiple))
    # nota bene: go one day beyond, to start the new cycle
    print(repr(new_first_date))

cycle_up(StartDate,722) # already experienced this many cycles


