import os
import csv                           #imports to read csv files

total_votes = 0                      #initial values for variables used in script
candidates_list = []
candidates_pct = []
candidates_votes = {}
candidates_string = ""
winner_votes = 0
winner = ""

poll_file = "Resources/election_data.csv"          #file where the csv comes from

with open(poll_file) as csvfile:                   #open csv file
    
    csvreader = csv.reader(csvfile)                #read csv file
    
    next(csvreader)                                #skip header
    
    for row in csvreader:                          #for loop
        
        total_votes += 1                           #increase total votes by 1 for each vote/row
        
        if row[2] not in candidates_list:          #check and see if candidate is in the list of candidates, and if not:
            candidates_list.append(row[2])         #add them to the list
            candidates_votes[row[2]] = 1           #forgot how to add value to a dictionary so used stack overflow for help, used this line of code from it
                                                   #also starting at 1 because now there is one vote for the candidate
        else:
            candidates_votes[row[2]] = candidates_votes[row[2]] + 1          #increase the vote count for said candidate by 1

for i in range(len(candidates_list)):
    person = candidates_list[i]
    candidates_pct.append(round(candidates_votes[person] / total_votes*100, 3))                   #calculate percentage of votes for each candidate
    candidates_string += (f'{person}: {candidates_pct[i]}% ({candidates_votes[person]}) \n')      #add a string so the printed out text will appear with this string
    if candidates_votes[person] > winner_votes:                                                   #finding the winning candidate by getting the greates number of votes
        winner_votes = candidates_votes[person]
        winner = person

        
text = (                                                    #make a text string with the information we desire in the string, such as votes and percentage of votes
    "Election Results \n" +
    "--------------------------------------------- \n" + 
    "Total Votes: " + str(total_votes) + "\n" +
    "--------------------------------------------- \n" +
    candidates_string +
    "--------------------------------------------- \n" +
    "Winner: " + winner
)

print(text)                                                 #print the result to the terminal

analysis_file = "Analysis/Analysis_of_PyPoll.txt"

with open(analysis_file, 'w') as text_file:                 #make the result a text file (code used from https://datagy.io/python-write-text-file/)
    text_file.write(text)
