import os
import csv

budget_file = "Resources/budget_data.csv"

months = 0             #initial value for months is 0
total = 0              #initial value for total profits/losses is 0
priormonth = 0         #initial value for calculating change
monthprofit = 0        #initial value for the profit of each month
monthlychange = []     #empty list to store monthly change in profits
gincrease = 0          #initial value of the greatest increase in profits
gdecrease = 0          #initial value of the greatest decrease in profits
gincmonth = ""         #initial value of the month of greatest increase in profits
gdecmonth = ""         #initial value of the month of greatest decrease in profits


with open(budget_file) as csvfile:                        #open csv file
    
    csvreader = csv.reader(csvfile)                       #read csv file
    
    pybank_header = next(csvreader)                       #skips past the header which says [month, profits]
    
    for row in csvreader:                                 #for loop to count over all months
        months += 1                                       #count up one month
        monthprofit = int(row[1])                         #making the variable for the month's profit
        total = total + monthprofit                       #total is the sum of all months changes
        if months >= 2:                                   #this line is to keep track of changes, but we don't want changes for the first month from 0, only changes after that
            change = monthprofit - priormonth             #change between months' profits
            monthlychange.append(change)                  #append the change to the list
        priormonth = monthprofit                          #change the month's profit to the prior month for the next loop
        if monthprofit > gincrease :                      #if statement to see if the profit is the greatest increase
            gincrease = monthprofit                       #change the increase to become greatest
            gincmonth = row[0]                            #change the month to become the month of greatest increase
        if monthprofit < gdecrease :                      #if statement to see if the profit is the greatest decrease
            gdecrease = monthprofit                       #change the decrease to become greatest
            gdecmonth = row[0]                            #change the month to become the month of greatest decrease
    
    avgchange = round(sum(monthlychange) / len(monthlychange), 2) #average of the changes, rounded to the penny's place (code for average from classmate Cody)

    #make a text statement with our desired variables
    text = ( 
          "Financial Analysis \n" +
          "-------------------------------------------------------------------- \n" +
          "Total months: " + str(months) + "\n" +
          "Total : $" + str(total) + "\n" +
          "Average Change: $" + str(avgchange) + "\n" +
          "Greatest Increase in Profits: " + gincmonth + " ($" + str(gincrease) + ") \n" +
          "Greatest Decrease in Profits: " + gdecmonth + " ($" + str(gdecrease) + ")"
    )
    
#print the text to the terminal
print(text)

#include text in a file in the analysis folder (code from https://datagy.io/python-write-text-file/)
analysis_file = "Analysis/Analysis_of_PyBank.txt"

with open(analysis_file, 'w') as text_file:
    text_file.write(text)
