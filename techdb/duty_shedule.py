from .models import (DutyTimetable)
import datetime


def nowDate():
    today = datetime.datetime.now()
    return today


def nowDuty():
    all_dutys = DutyTimetable.objects.all()
    now_date = nowDate().strftime("%Y-%m-%d %H:%M:%S")

    for i in all_dutys:
        print(str(i.date_start))
        print(str(now_date))
        print(str(i.date_start) < str(now_date))
        print(str(i.date_end) > str(now_date))
        if str(i.date_start) < str(now_date) and str(i.date_end) > str(now_date):
            print(i.duty)
            return i 

today_duty_object = nowDuty()
