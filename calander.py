import calendar
from typing import Any, Union

print(calendar.weekheader(2))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2019, 3))

print(calendar.monthcalendar(2019,3))

print(calendar.calendar(2021))

day_of_the_work = calendar.weekday(2020,12,22)
print(day_of_the_work)

is_leap: Union[bool, Any] =calendar.isleap(2020)
print(is_leap)

how_many_long_days = calendar.leapdays(2000,2011)
print(how_many_long_days)
