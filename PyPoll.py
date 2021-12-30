# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Declare a list of candidate options
candidate_options = []

# Create a dictionary to store the candidate names/votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Increment the total votes by 1
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add candidate name to options list if first time coming across name
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Start tracking votes for the candidate
            candidate_votes[candidate_name] = 0
            
        # Add votes as you cycle through the rows
        candidate_votes[candidate_name] += 1

#save results in a text file
with open(file_to_save, "w") as txt_file:         
 #Final resuls to be printed to txt file
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Print to text file
    txt_file.write(election_results)

    # Determine percentage of votes for each candidate
    # 1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count per candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = ( f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print results
        print(candidate_results)
        # Write results by candidate to text file
        txt_file.write(candidate_results)

        # Determine if the vote count is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name

    # Write format for winning candidate summary        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save winning_candidate_summary to text_file
    txt_file.write(winning_candidate_summary)
   

   