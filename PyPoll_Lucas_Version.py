# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize Total vote counter
total_vote = 0

candidate_options = []

#Charles Casper Stockham vote counter
Charles_votes = 0

#Diana DeGette Votes counter
Diana_votes = 0

#Raymon Anthony Doane Votes counter
Raymon_votes = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    x = next(file_reader)
    print(x)
    for row in file_reader:
        #add total vote count.
        total_vote += 1

        #find all different candidates
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        #candidate options: ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
        
        #Find total votes for each candidate
        #Candidate1: Charles Casper Stockham
        if row[2] == 'Charles Casper Stockham':
            Charles_votes += 1

        #Candidate1: Diana DeGette
        if row[2] == 'Diana DeGette':
            Diana_votes += 1

        #Candidate1: Raymon Anthony Doane
        if row[2] == 'Raymon Anthony Doane':
            Raymon_votes += 1

print(f"Charles has {Charles_votes} votes, Diana has {Diana_votes} votes, and Raymon has {Raymon_votes} votes")
