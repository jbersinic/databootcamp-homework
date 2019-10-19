# Module for reading CSV files
import csv 
import os 

# Location of the file 
csvpath = "election_data.csv"

# Open the CSV, Improved Reading using CSV module
with open(csvpath, 'r', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first 
    csv_header = (next(csvreader))

    # Define variables & lists
    total_votes = 0
    Candidate_list = []
    Khan_votes = 0
    Correy_votes = 0 
    Li_votes = 0 
    OTooley_votes = 0 

    # Count total votes 
    for row in csvreader:
        total_votes +=1
        
        # Identify all unique candidates  
        if row[2] not in Candidate_list:
            Candidate_list.append(row[2])
        
        # Count the amount of votes for each candidate
        if row[2] == "Khan":
            Khan_votes +=1
        if row[2] == "Correy":
            Correy_votes +=1
        if row[2] == "Li":
            Li_votes +=1
        if row[2] == "O'Tooley":
            OTooley_votes +=1

    # Apply the math for percentages
    Khan_Percent_Vote = (Khan_votes/total_votes)*100
    Correy_Percent_Vote = (Correy_votes/total_votes)*100
    Li_Percent_Vote = (Li_votes/total_votes)*100
    OTooley_Percent_Vote = (OTooley_votes/total_votes)*100

    # Store votes in dictionary to get maximum
    votes = { 
    "Khan": Khan_votes,
    "Corrrey": Correy_votes,
    "Li": Li_votes,
    "O'Tooley": OTooley_votes
    }
    
    # Return maximum vote to get winner 
    winner = max(votes, key=votes.get)  

# Output totals & findings
print("Election Results:")
print("---------------------------------")    
print(f"Total Votes: {total_votes}")
print("---------------------------------")   
print(f"Khan: {Khan_Percent_Vote:.3f}%" + f" ({Khan_votes})")
print(f"Correy: {Correy_Percent_Vote:.3f}%" + f" ({Correy_votes})")
print(f"Li: {Li_Percent_Vote:.3f}%" + f" ({Li_votes})")
print(f"O'Tooley: {OTooley_Percent_Vote:.3f}%" + f" ({OTooley_votes})")
print("---------------------------------")   
print(f"Winner: {winner}")
print("---------------------------------")   

# Write results to text file
print("Election Results:"+"\n---------------------------------" 
+ f"\nTotal Votes: {total_votes}"
+ f"\n---------------------------------"
+ f"\nKhan: {Khan_Percent_Vote:.3f}%" + f" ({Khan_votes})" 
+ f"\nCorrey: {Correy_Percent_Vote:.3f}%" + f" ({Correy_votes})"
+ f"\nLi: {Li_Percent_Vote:.3f}%" + f" ({Li_votes})"
+ f"\nO'Tooley: {OTooley_Percent_Vote:.3f}%" + f" ({OTooley_votes})"
+ f"\n---------------------------------"
+ f"\nWinner: {winner}"
+ f"\n---------------------------------"
,file=open('textPyBank.txt','w'))

