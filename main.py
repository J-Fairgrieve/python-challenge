#Import the relevant modules
import os
import csv

# Outline the path where the budget csv file is located
budget_path = os.path.join("Resources", "budget_data.csv")

with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    csvreader

    # Reset the variables
    prev_pl = None
    new_value = 0
    difference = []
    pl_data = {}

    for row in csvreader:

        # Get the list of differences for each month, if this is the first iteration, prepare for the next row
        if prev_pl is None:
            prev_pl = row[1]
            pl_data.update({row[0]: int(row[1])})  
        else:
            new_value = int(row[1]) - int(prev_pl)
            difference.append(new_value)
            prev_pl = row[1]
            pl_data.update({row[0]: int(row[1])})

avg_diff = sum(difference) / len(difference)

# Print the values that are produced from the above
print("----------------------------\nFinancial Analysis\n----------------------------")
print("Total months: %d" %len(pl_data))
print("Total Profit: $%d" %sum(pl_data.values()))
print(str("Average Change: $" + format(sum(difference) / len(difference), ".2f")))
print("Greatest Increase in Profits:", max(pl_data, key=pl_data.get), "($%d)" %max(pl_data.values()))
print("Greatest Decrease in Profits:", min(pl_data, key=pl_data.get), "($%d)" %min(pl_data.values()))
print("----------------------------\n\n\n")

budget_write = os.path.join("Analysis", "Budget_Analysis.txt")
budget_lines = ["----------------------------",
"Financial Analysis",
"----------------------------",
    "Total months: %d" %len(pl_data),
    "Total Profit: $%d" %sum(pl_data.values()),
    str("Average Change: $" + format(sum(difference) / len(difference), ".2f")),
    "Greatest Increase in Profits: " , max(pl_data, key=pl_data.get), "($%d)" %max(pl_data.values()),
    "Greatest Decrease in Profits: " , min(pl_data, key=pl_data.get) , " ($%d)" %min(pl_data.values()),
    "----------------------------"]

budget_lines

with open(budget_write, "w") as f:
    for line in budget_lines:
        f.writelines(str(line))
        f.writelines("\n")

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
    print(candidates)
    print(total_votes, winner)
    print("----------------------------\nElection Results\n----------------------------")
    print("Total Votes: %d\n----------------------------"%total_votes)
    for key in candidates:
        print(key + ":",
        str(format(candidates[key] / total_votes * 100, ".3f")) +"%",
        "(" + str(candidates[key]) + ")")
    print("----------------------------\nWinner: %s\n----------------------------"%winner)