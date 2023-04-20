import os
import csv
file_to_output = os.path.join('Analysis','election_analysis.txt')
csvpath = os.path.join('Resources','election_data.csv')


total_votes = 0
candidate_votes = {}
candidates =[]
winning_candidate = ""
winning_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
 
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if  candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
with open(file_to_output, 'w') as f:
    print(f"Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    results = ( f"Election Results\n"   
                        f"----------------------------\n"   
                        f"Total Votes: {total_votes}\n"    
                        f"----------------------------\n" )
                    
    f.write(results)
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100

        max_votes = 0
        if votes > winning_votes:
            winning_votes = votes
            winner = candidate
        print(f"{candidate}: {percentage:.3f}% ({votes})\n")
        voter_output= f"{candidate}: {percentage:.3f}% ({votes})\n"
        f.write(voter_output)
    print("-------------------------")
    print(f"Winner: {winner}")  
    f.write(f"Winner: {winner}\n")
    print("-------------------------")
    



  
