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
To provide the requested information for challenge, I started by selecting the first prompt (voter turnout by county) and then created an outline for the code I needed to write.

## Challenge Summary
