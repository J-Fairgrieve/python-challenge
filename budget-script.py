#Import the relevant modules
import os
import csv

# Outline the path where the budget csv file is located
budget_path = os.path.join("Resources", "budget_data.csv")

with open(budget_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    # Reset the variables
    prev_pl = None
    new_value = 0
    difference = []
    pl_data = {}

    for row in csvreader:

        # Prepare information for printing 
        if prev_pl is None:
            # Set the first value for calculating the differences
            prev_pl = row[1]

            # Add the row's data to the dictionary
            pl_data.update({row[0]: int(row[1])})  
        
        else:
            # Calculate the profit/loss difference between this row & the previous one
            new_value = int(row[1]) - int(prev_pl)
            difference.append(new_value)
            prev_pl = row[1]

            # Add the row's data to the dictionary
            pl_data.update({row[0]: int(row[1])})

# Calculate the average difference for printing
avg_diff = sum(difference) / len(difference)

# Print the values that are produced from the above
print("----------------------------\nFinancial Analysis\n----------------------------")
print("Total months: %d" %len(pl_data))
print("Total Profit: $%d" %sum(pl_data.values()))
print(str("Average Change: $" + format(avg_diff, ".2f")))
print("Greatest Increase in Profits: %s ($%d)" % (max(pl_data, key=pl_data.get), max(pl_data.values())))
print("Greatest Decrease in Profits: %s ($%d)" % (min(pl_data, key=pl_data.get), min(pl_data.values())))
print("----------------------------\n\n\n")

# Create the content for the .txt file
budget_write = os.path.join("Analysis", "Budget_Analysis.txt")
budget_lines = ["----------------------------",
"Financial Analysis",
"----------------------------",
    "Total months: %d" %len(pl_data),
    "Total Profit: $%d" %sum(pl_data.values()),
    str("Average Change: $" + format(avg_diff, ".2f")),
    "Greatest Increase in Profits: %s ($%d)" % (max(pl_data, key=pl_data.get), max(pl_data.values())),
    "Greatest Decrease in Profits: %s ($%d)" % (min(pl_data, key=pl_data.get), min(pl_data.values())),
    "----------------------------"]

# Create the .txt file
with open(budget_write, "w") as f:
    for line in budget_lines:
        f.write(str(line))
        f.write("\n")