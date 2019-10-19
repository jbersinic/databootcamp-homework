# Module for reading CSV files
import csv
import os 

csvpath = "budget_data.csv"

# Open the CSV, Improved Reading using CSV module
with open(csvpath, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first 
    csv_header = (next(csvreader))

    # Define counters & lists
    total_months = 0
    total_PL = 0
    PL_list1 = []
    PL_list2 = []
    months_list = []

    # Count the months & PL
    for row in csvreader:
        total_months +=1
        total_PL = total_PL + int((row[1]))

        # Create lists to store data
        months_list.append(str((row[0])))
        PL_list1.append(int((row[1])))
        
        # Shift new list to start 'down' by 1
        PL_list2 = PL_list1[1:]
    
    # Make both lists the same length 
    PL_list1 = PL_list1 [:(len(PL_list1)-1)]
    
    # Evaluate the difference between the two lists 
    PL_change = list(map(int.__sub__, (PL_list2), (PL_list1)))
    
    # Sum the P&L & apply the math
    average_change = sum(PL_change)/ len(PL_change)
    greatest_increase_PL = str(months_list[PL_change.index(max(PL_change))+1])+ " ($"+str(max(PL_change))+")"
    greatest_decrease_PL = str(months_list[PL_change.index(min(PL_change))+1]) + " ($"+str(min(PL_change))+")"

# Output totals & findings
print("Financial Analysis")
print("---------------------------------")    
print(f"Total Months: {total_months}")
print(f"Total: ${total_PL}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits:{greatest_increase_PL}")
print(f"Greatest Decrease in Profits:{greatest_decrease_PL}")

# Write analysis to text file
print("Financial Analysis"+"\n---------------------------------" + f"\nTotal Months: {total_months}" 
+ f"\nAverage Change: ${round(average_change,2)}" 
+ f"\nGreatest Increase in Profits:{greatest_increase_PL}" + f"\nGreatest Decrease in Profits:{greatest_decrease_PL}",
file=open('textPyBank.txt','w'))

