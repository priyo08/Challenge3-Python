import csv, os, sys
from csv import DictReader
d = []
with open("Resources/budget_data.csv") as csv_file:
    c_dict = DictReader(csv_file)
    d.extend(list(c_dict))
total_number_rows = len(d) 
print(f"Total Numbe of  rows: {total_number_rows}")
total_pl = 0
pl_list = []
for row in d:
    pl_list.append(int(row['Profit/Losses']))
total_pl = sum(pl_list)
    
print(f"Total Profilt and loss val {total_pl}")
print(f"Average is {round(total_pl/total_number_rows,2)}")

# Difference

two_dates_diff = []

for ix, val in enumerate(pl_list[:-1]):
    two_dates_diff.append(pl_list[ix+1] - pl_list[ix])
    
diff_val = round(sum(two_dates_diff)/len(two_dates_diff),2)
print(f"The Diff value totaled at {diff_val}")

max_profit, max_profit_date = max(two_dates_diff), d[two_dates_diff.index(max(two_dates_diff))+1]['Date']

print(f"Max profit : {max_profit}, Max profit date is {max_profit_date}")


min_profit, min_profit_date = min(two_dates_diff), d[two_dates_diff.index(min(two_dates_diff))+1]['Date']

print(f"Max profit : {min_profit}, Max profit date is {min_profit_date}")