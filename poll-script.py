#Import the relevant modules
import os
import csv

# Outline the path where the Poll csv file is located
poll_path = os.path.join("Resources", "election_data.csv")

with open(poll_path, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")

    next(csvreader)
    # Reset the variables
    winner = "none"
    candidates = {}

    for row in csvreader:

        # Assign the vote to the correct candidate; if the candidate is in the dictionary, add to their tally
        if row[2] in candidates:
            candidates[row[2]] = candidates[row[2]] + 1

        # Otherwise, add the new candidate to the dictionary with their first vote
        else:
            candidates.update({row[2]: 1})

    # Determine the end metrics from the created dictionary
    total_votes = sum(candidates.values())
    winner = max(candidates, key=candidates.get)

    # Print the results!
    print("----------------------------\nElection Results\n----------------------------")
    print("Total Votes: %d\n----------------------------"%total_votes)
    for key in candidates:
        print(key + ":",
        str(format(candidates[key] / total_votes * 100, ".3f")) +"%",
        "(" + str(candidates[key]) + ")")
    print("----------------------------\nWinner: %s\n----------------------------"%winner)


# Create the content for the .txt file
candidate_loop = []
for key in candidates:
    candidate_loop.append(key + ": " + format(candidates[key] / total_votes * 100, ".3f")
    + "% (" + str(candidates[key]) + ")")
can_print = "\n".join(candidate_loop)

poll_write = os.path.join("Analysis", "Poll_Analysis.txt")
poll_lines = ["----------------------------\nElection Results\n----------------------------",
    "Total Votes: %d\n----------------------------"%total_votes,
    can_print,
    "----------------------------\nWinner: %s\n----------------------------"%winner]


# Create the .txt file
with open(poll_write, "w") as f:
    for line in poll_lines:
        f.write(str(line))
        f.write("\n")