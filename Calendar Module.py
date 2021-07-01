import calendar
# print(calendar.TextCalendar(firstweekday=5).formatyear(2021))

m, d, y = map(int, input().split())
days = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY', 4: 'FRIDAY', 5: 'SATURDAY', 6: 'SUNDAY'}
print(days[calendar.weekday(y, m, d)])
