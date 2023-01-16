import csv, os, sys
from csv import DictReader

d = []
with open("Resources/election_data.csv") as csv_file:
    c_dict = DictReader(csv_file)
    d.extend(list(c_dict))
total_number_rows = len(d) 
print(f"Total Numbe of  votes: {total_number_rows}")
results_per_candidate = {}
for i in d:
    results_per_candidate[i["Candidate"]] = results_per_candidate.setdefault(i["Candidate"], 0) + 1
max_candidate , max_val = 0, 0
for candidate, no_of_votes in results_per_candidate.items():
    if no_of_votes > max_val:
        max_candidate , max_val = candidate, no_of_votes
    print(f"{candidate}: {round(100*no_of_votes/total_number_rows, 2)} ({no_of_votes}) ")
    
print(f"Winner is {max_candidate} with  {max_val} votes")
    