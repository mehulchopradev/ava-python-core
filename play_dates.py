# date time related operations
from datetime import date, time, datetime, timedelta

today = date.today()
print(today)
print(type(today))
print(today.year)
print(today.month)
print(today.day)

print(today.weekday()) # Monday starts with 0

birthdate = date(year=1986, month=11, day=25)
# print(birthdate.strftime('%d/%m/%Y'))
print(birthdate.strftime('%d, %B %Y'))

# arithmetic operators for date comparison
print(today > birthdate)

# derive futurebirthdate from birthdate
futurebirthdate = birthdate.replace(year=today.year)
print(futurebirthdate)

print(today > futurebirthdate)
print(futurebirthdate - today)
print(today - birthdate)

now = datetime.now()
print(now.strftime('%d/%m/%Y %H:%M'))
print(type(now))
print(now.day)
print(now.month)
print(now.hour)

nowtime = datetime.time(now)
print(nowtime)
print(type(nowtime))
print(nowtime.hour)
print(nowtime.minute)
print(nowtime.second)

oneweekdelta = timedelta(weeks=1)
print(oneweekdelta)
print('One week from now will be : ')
print(today + oneweekdelta)

print('One week past date would have been : ')
print(today - oneweekdelta)

fivedaysdelta = timedelta(days=5)
print('Task will be done in : ')
print(today + fivedaysdelta)