import os
import csv
file_to_output = os.path.join('Analysis','budget_analysis.txt')
csvpath = os.path.join('Resources','budget_data.csv')
dates=[]
profits_losses=[]

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
 
    for row in csvreader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

    total_months = 0
    net_profit_loss = 0
    previous_month_profit_loss = 0
    monthly_profit_change = 0
    monthly_profit_changes = []
    greatest_increase_date = ""
    greatest_increase_amount = 0
    greatest_decrease_date = ""
    greatest_decrease_amount = 0

num_months = len(dates)
net_total = sum(profits_losses)
changes = [profits_losses[i+1] - profits_losses[i] for i in range(len(profits_losses)-1)]


average_change = sum(changes)/ len(changes)

max_increase= max(changes)
max_increase_index = changes.index(max_increase)
max_increase_date = dates[max_increase_index + 1]
max_increase_amount = changes[max_increase_index]

max_decrease= min(changes)
max_decrease_index= changes.index(max_decrease)
max_decrease_date = dates[max_decrease_index +1]
max_decrease_amount = changes[max_decrease_index]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

results = ( f"Financial Analysis\n"   
                    f"----------------------------\n"   
                    f"Total Months: {total_months}\n"    
                    f"Total: ${net_total}\n"    
                    f"Average Change: ${average_change:.2f}\n"    
                    f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"    
                    f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")
with open(file_to_output, 'w') as f:
    f.write(results)