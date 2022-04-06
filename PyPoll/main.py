import os
import csv

# Creating Variables
canidates = []
votes = []
total_votes = 0


# Reading the csv file
election_csv = os.path.join("Resources/election_data.csv")

# print(election_csv)
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    num_canidates = -1
    # The total number of votes cast
    for row in csvreader:
        total_votes+=1
        
    # A complete list of candidates who received votes
    # for row in votes:
        if row[2] in canidates:
            num_canidates = canidates.index(row[2])
            votes[num_canidates]+=1
        else:
            canidates.append(row[2])
            num_canidates+=1
            votes.append(1)

# Print Statements

results = ["Election Results",
"-----------------------",
f'Total Votes: {(total_votes)}', 
"-----------------------"]
for i in range(len(canidates)):
    results.append(f'{canidates[i]}: {round(votes[i] / total_votes * 100,3)}% ({votes[i]})')
max_index = votes.index(max(votes))
results.append("-----------------------")
results.append(f'Winner: {canidates[max_index]}')
results.append("-----------------------")

for l in results:
    print(l)

with open ("Analysis/election_data.txt",'w') as a:
    for v in results:
        a.write(v)
        a.write('\n')