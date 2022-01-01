# Election_Analysis
Module 3 Python polling repository and challenge analysis, completed by Hannah Wikum in January 2022

## Project Overview
This project was completed to assist Tom and Seth, two employees on the Colorado Board of Elections, to audit the results of a recent election for a US Congressional precinct. The data was provided in a CSV file, which included ballot ID, county, and selected candidate for 369,711 ballots. I was tasked with automating the audit using Python in Visual Studio Code to calculate the following:

  * Total votes cast
  * Number of votes per candidate
  * Percent of total votes per candidate
  * Winner of the election based on the popular vote

The final code and results were commited to a Git Hub repository.

## Resources
- Data Source: election_results.csv (provided)
- Software: Python 3.9.9, Visual Studio Code 1.63.2, Git Bash 2.34.1.windows.1

## Summary
After building code to analyze the data, a summary of the results was written to a text file, as pictured below:

![image](https://user-images.githubusercontent.com/93058069/147860131-67e53eeb-33f0-49d1-8ce1-d7730c80ee75.png)

The total votes of 369,711 matched the number of rows (plus header) from the CSV file. There were three candidates who received votes: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Raymon received only 3.1% of the vote, which put him in third. Charles received 23.0% of the vote for second place. Diana received 73.8% of the vote (272,892 votes), which makes her the clear winner. Because Diana had the most votes, her name, vote count, and vote percentage were printed at the bottom of the election results summary to clearly confirm the results.

## Challenge Overview
The challenge added on to the initial analysis to provide even more comprehensive, county-level information to complete the audit. The election commission requested the following information:
  
  * voter turnout by county
  * percentage of votes (out of the total cast) from each county
  * county with the highest voter turnout

## Challenge Methodology
To provide the requested information for challenge, I started by creating an outline of all the information I would need to code to find the results. This included the following  steps:

  1. Get a list of all counties from the CSV file
  2. Count the number of votes by county
  3. Determine the county with the highest number of votes (highest turnout)
  4. Calculate the percentage of votes from each county compared to the total votes
  5. Write the results to the text file

In the first part of the analysis for the module, the county data existed in the CSV, but it was not used in the code. Writing the outline made it pretty clear that I could use similar code from calculating the votes, percentage, and winner _by candidate_, but update the code to reference the _county_ instead.

Here are the steps I followed to build my code:
  1. Created a county_list list and county_votes dictionary (both were empty because the for loop would fill them in as it read the CSV later)
  2. Defined variables largest_county to get the name of the county with the most votes and county_voter_turnout to get the number of votes for that county
  3. In the for loop, added county_name = row[1] to get the county name from each row
  
     a. Note: County is the second column of the CSV (ballot ID, county, candidate), but I used one as the index above because the index of columns start at 0 (ballot ID index 0, county index 1, candidate index 2)
     
  4. Added an if statement to determine if the county_name was not already in the county_list

     a. Note: Used "not in" logical operator because if it is true that the county name is not in the list, then I want to add it. If it is false, then the second part of the  code to add the county name to the list wouldn't activate, which avoids duplicates
     
 5. If my statement from 4 was true (county_name not in county_list), then I added county_list.append(county_name) to add the county to the list I defined in step 1
 6. If my statement from 4 was true and after the county name was added to the list for the first time, I wrote code to begin tracking the votes for that county by setting the vote count equal to zero. This is the end of this if statement.
 7. Added one to the vote count for that county
 
    a. Note: If this is the first time the loop encounters this county name, that will mean the county has one vote after going through the if statement. If the county was already in the list, then it will skip the if statement, but add one to the previous count.
    
8.     
    
    

## Challenge Summary
