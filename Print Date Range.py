from datetime import date, timedelta

start_date = date(2008, 8, 15)
end_date = date(2008, 9, 15)
delta = end_date - start_date   # returns timedelta
date_list = []

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    date = day.strftime("%Y%m%d")
    print(date)
    date_list.append(date)
print(date_list)