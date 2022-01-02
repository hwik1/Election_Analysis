# Election Analysis
Module 3 Python polling repository and challenge analysis, completed by Hannah Wikum - January 2022

## Resources
- Data Source: election_results.csv (provided)
- Software: Python 3.9.9, Visual Studio Code 1.63.2, Git Bash 2.34.1.windows.1

___

## Overview of Election Audit
This project was completed to assist Tom and Seth, two employees of the Colorado Board of Elections, to audit the results of a recent election for a US Congressional precinct. The data was provided in a CSV file, which included ballot ID, county, and selected candidate for 369,711 ballots. I was tasked with automating the audit using Python in Visual Studio Code.

For the module work, I calculated the following metrics:

  * Total votes cast
  * Number of votes per candidate
  * Percent of total votes per candidate
  * Winner of the election based on the popular vote

For the challenge, I added to the initial analysis to provide a more comprehensive analysis that included county-level information. The election commission requested the following information:

  * Voter turnout by county
  * Percentage of votes (out of the total cast) from each county
  * County with the highest voter turnout

The final results were printed to a text file. The code and text results were committed to a Git Hub repository.

## Module Summary
After building code to analyze the data, a summary of the results was written to a text file, as pictured below:

![image](https://user-images.githubusercontent.com/93058069/147860131-67e53eeb-33f0-49d1-8ce1-d7730c80ee75.png)

The total votes of 369,711 matched the number of rows (plus header) from the CSV file. There were three candidates who received votes: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. Raymon received only 3.1% of the vote, which put him in third. Charles received 23.0% of the vote for second place. Diana received 73.8% of the vote (272,892 votes), which makes her the clear winner. Because Diana had the most votes, her name, vote count, and vote percentage were printed at the bottom of the election results summary to clearly confirm the results.

___

## Challenge
### Challenge Methodology
To provide the requested information for challenge, I started by creating an outline of all the information I would need to code to find the results. This included the following  steps:

  1. Get a list of all counties from the CSV file
  2. Count the number of votes by county
  3. Determine the county with the highest number of votes (highest turnout)
  4. Calculate the percentage of votes from each county compared to the total votes
  5. Write the results to the text file

In the first part of the analysis for the module, the county data existed in the CSV, but it was not used in the code. Writing the outline made it pretty clear that I could use similar code from calculating the votes, percentage, and winner _by candidate_, but update the code to reference the _county_ instead.

#### Steps to Building the Code
Here is a summary of the steps I followed to build the code for the challenge, including learnings or explanations of why I built the code how I did:

  1. Created a county_list list and county_votes dictionary (both were empty because the for loop would fill them in as it read through the rows of the CSV later)
  2. Defined variables largest_county to get the name of the county with the most votes and county_voter_turnout to get the number of votes for that county
  3. In the for loop, added county_name = row[1] to get the county name from each row
  
     **Note:** County is the second column of the CSV (ballot ID, county, candidate), but I used one as the index above because the index of columns start at 0 (ballot ID: index 0, county: index 1, candidate: index 2)
     
  4. Added an if statement to determine if the county_name was not already in the county_list

     **Note:** Used "not in" logical operator because if it is true that the county name is not in the list, then I want to add it. If it is false, then the second part of the  code that adds the county name to the list wouldn't activate, which avoids duplicates
     
 5. If my statement from 4 was true (county_name not in county_list), then I added county_list.append(county_name) to add the county to the list I defined in step 1
 6. If my statement from 4 was true and the county name was added to the list for the first time, I wrote code to begin tracking the votes for that county by setting the vote count equal to zero. This is the end of the if statement.
 7. Added one to the vote count for that county
 
    **Note:** If this is the first time the loop encounters this county name, that will mean the county has one vote after going through the if statement (1+0). If the county was already in the list, then it will skip the if statement, but add one to the previous count.
    
8. Created a for loop to get the count of votes and percentage of total votes for each county, which I then printed/saved to the text file in a similar format to the candidate results

   i.e. county name: percentage of total votes to the tenth (total county votes with comma formatting)
   **or** Jefferson: 10.5% (38,855)
   
9. Wrote an if statement to figure out which county had the largest voter turnout using if(total_county_votes > county_voter_turnout) and setting largest_county equal to county_name and county_voter turnout equal to total_county_votes

   **Note:** Since this is in the for loop and the county_voter_turnout starts at zero, the first time the code runs on Jefferson, the new county_voter_turnout would be set to Jefferson's total county votes of 38,855 because that is greater than 0. The next time through on Denver, county_voter_turnout would reset to 306,055, which is Denver's voter turnout because it is greater than Jefferson's. On the third time through, Arapahoe's 24,801 turnout is smaller than the current county_voter_turnout, so the if statement is not activated and Denver remains as the largest_county and county_voter_turnout.
   
10. Created a summary of the largest turnout county name with formatting using f-strings in the same style as the winning candidate and printed/wrote to the text file
    
#### Issues Encountered
Although the code was fairly easy to replicate for counties instead of candidates, I did run into a few challenges:

  * When I downloaded and saved the PyPoll_Challenge code, I saved it in the wrong 'Resources' folder from the earlier VBA challenge. That caused the IOError described in module 3.4.3 because that version of the Resources folder didn't have an Analysis folder. I had to rewrite the file_to_save path in line 11 with the direct path to a new election_results.txt file instead of the relative path because I couldn't get it to work otherwise.

 * There were a lot of variables being used by the end of the code where I needed to write the if statement to determine the county with the highest voter turnout and the vote count and I started to get confused. At first, I thought I could use total_county_votes > winning_count (using the same variable as the candidate with the most votes), but that gave me an incorrect output. As you can see in the first picture below, that code said Arapahoe county had the highest turnout with 24,801 votes, but I could see that Denver had the most with 306,055. After troubleshooting the error, I updated the if statement to read if total_county_votes > county_voter_turnout because that was the variable I had previously defined to hold the votes for the largest turnout county and that corrected the issue, as seen in the second picture below.

_Incorrect if statement output_

![image](https://user-images.githubusercontent.com/93058069/147861982-bae083e2-a2b0-4115-8f54-c87ba65e411f.png)

_Corrected if statement output_

![image](https://user-images.githubusercontent.com/93058069/147862026-ae4f63ef-811c-4cbc-953a-248bd35a0ba7.png)

### Election-Audit Results
After the election audit for the challenge was complete, here is a summary of the outcomes of the election (see Steps to Building code above for detail on how each was determined):
 * Total votes: 369,711
 * Percent of total votes / vote count by county:
       * Jefferson: 10.5% / 38,855
       * Denver: 82.8% / 306,055
       * Arapahoe: 6.7% / 24,801
 * County with the largest number of votes: Denver
 * Percent of total votes / vote count by candidate:
       * Charles Casper Stockham: 23.0% / 85,213
       * Diana DeGette: 73.8% / 272,892
       * Raymon Anthony Doane: 3.1% / 11,606
 * Winning candidate: Diana Degette (73.8% of total vote / 272,892 votes) 

### Election-Audit Summary
This election audit successfully demonstrated a workable Python script that can read tabulated vote data from a CSV and print an analysis to a text file, which includes results for total votes and vote percentage by candidate and county, as well as the winning candidate and county with the largest voter turnout. (Note: for this analysis, voter turnout is defined by absolute number of voters per county - not number of votes compared to the eligble voter population.) This script could be used for any election with slight modifications to fit the scenario, like the two options described below:
 1. If you want to use this script for a country-wide election, like the result of the popular vote for the Presidential election, then you would likely want to modify the code to analyze by state instead of by county. The candidate calculations could stay the same, but there would be so many county results with the current script and it wouldn't be meaningful for a national election. You would not only need to modify your script, but would also need to ensure that the CSV file has state information.
 2. If you had an election with ranked choice voting, then you would need to modify the script to add up the total votes by candidate for only the first ranked choice and then divide that by the total number of votes. If a candidate gets more than 50% of the vote, then you could declare a winner. If not, you would need the script to eliminate the candidate with the lowest amount of votes and pull in their second choices before re-running the votes per candidate and percentages. Check if any candidate has a majority over 50% and repeat if necessary.
