import os
import csv

# Reading the csv file
budget_csv = os.path.join("Resources/budget_data.csv")
# print(budget_csv)
budget = [] 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for data in csvreader:
        budget.append(data)

# Defining the variables
    row = 0
    total = 0
    monthcount = 0 
    greatest_decrease = 0
    profits = [] 
    months = []
    greatest_increase = 0
    current_row = 0
    profit_losses = 0
    change = []
    average_change = 0


# The net total amount of profit/losses over the entire period
# Total Months
for row in budget:
    monthcount+=1
    profit_losses = profit_losses +int(row[1])

for row in budget:
    months.append(row[0])
    profits.append(row[1])
    
length_profits = len(profits)
    # print(profits)
    # The Changes in profit/losses over the entire period then average these changes
last_row = profits[0]  

for row in profits:
    # current_row = int(row[1])
    c = int(row) - int(last_row)
    change.append(c)
    last_row = row
    if current_row > greatest_increase:
        greatest_increase = current_row

sum_change = sum(change)
average_change = sum_change / (len(change) - 1)
change_one = change
months_change = list(zip(months,change_one))

# for row in change:
# The Greatest Increase in profits - The date and amount over - over the entire period 
greatest_increase = max(change)
for i in months_change:
    if i[1] == greatest_increase:
        greatest_month = i[0]
# The Greatest Decrease in profits - The date and amount over - over the entire period 
greatest_decrease = min(change)
for i in months_change:
    if i[1] == greatest_decrease:
        worst_month = i[0]


results = ["Financial Analysis",
"-----------------------",
f'Total Months: {(monthcount)}', 
f'Total: ${(profit_losses)}',
f'Average Change: ${round(average_change,2)}',
f'Greatest Increase: {greatest_month}, ${(greatest_increase)}',
f'Greatest Decrease: {worst_month}, ${(greatest_decrease)}']

for l in results:
    print(l)

with open ("Analysis/budget_data.txt",'w') as a:
    for v in results:
        a.write(v)
        a.write('\n')