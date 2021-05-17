# Analysis of the Election Audit

## Overview of Election Audit
The purpose of the election analysis audit was to help Seth and Tom to find additional information requested by the election commission by analyzing the given data set. We have been given a starter code to find the candidates, the total vote count, each candidate's vote count, and the winner of the election. However, the election commission wanted additional analysis on the counties and requested us to find the voter turnout for each county, the percentage of votes from each county, and the county with the highest turnout. In addition to that, we were also requested to save our results on the **election_analysis.txt** file. 

## Election Audit Results
![Election results](/resources/Election_analysis_results.png)
<br />
The results of the election is shown in the picture above. The total votes for this particular election is 369,711 votes and our analysis showed that the county with the highest turnout, with 82.8% of the total votes, came from Denver (306,055 votes), and following Denver is Jefferson with 10.5% of the total votes (38,855 votes), and last is Arapahoe with 6.7% of the total votes (24,801 votes). Our analysis also found that the winner of the election is Diana DeGette, whom recieved 73.8% of the total vote (272,892 votes). The two other candidates: Charles Casper Stockham and Raymon Anthony Doane recieved 23.0% (85,213 votes) of the total votes and 3.1% (11,606 votes) of the total votes respectively. 


## Elcetion Audit Summary
We have shown that the code was successful in analyzing the given data set. However, other data sets might have the columns ordered differently and our code will obviously be unsuccessful in analyzing the data, for example, in this data set, the 3rd column has the cadidates that were voted by the particular voter and with the code that we developed, we were able to find the number of votes each candidate recieved by specifying that the third column contained the names of the candidates. If other data sets did not put the names of the candidates being voted for on the third column, our code will obviously won't work. Hence, we will need to modify our code so that it is able to differentiate between the columns and know which column is used for counting the candidates votes.
