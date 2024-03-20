Pythagorean Expectation Model for IPL 2018

The project aims to analyze the performance of teams in the Indian Premier League (IPL) cricket tournament for the year 2018 using a statistical model known as the Pythagorean Expectation. The IPL is played in the Twenty20 (T20) format, where each team has a limited number of balls (120) to score as many runs as possible.
The Pythagorean Expectation model, originally developed for baseball, predicts a team's winning percentage based on the number of runs scored and allowed. In this project, the model is adapted for cricket, considering the runs scored and conceded by each team in the IPL matches.

Methodology:
1.	Data Collection: Match data for the IPL 2018 season is imported, containing information such as team names, match outcomes, runs scored, and other relevant statistics.
2.	Data Preprocessing: The data is processed to calculate key metrics such as runs scored by home and away teams, wins, and games played for each team.
3.	Pythagorean Expectation Calculation: The Pythagorean Expectation formula is applied to estimate each team's expected winning percentage based on their runs scored and allowed.
   ![Screenshot (149)](https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/49ec972a-94ba-411d-b99f-bbb32dccab2d)

4.	Data Visualization: The relationship between the actual winning percentage and the Pythagorean Expectation is visualized using scatter plots.
![Screenshot (150)](https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/2d1df9aa-4376-4959-815f-bc0eeb7788c2)
5..	Statistical Analysis: Regression analysis may be performed to evaluate the effectiveness of the Pythagorean Expectation model in predicting team performance.
   
Findings:
•	The analysis reveals insights into how closely a team's actual winning percentage aligns with the predicted values from the Pythagorean Expectation model.
•	It provides valuable information for team management, fans, and cricket enthusiasts to assess team performance and make informed predictions for future matches.
![Screenshot (148)](https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/b01123ff-c441-4288-9e18-e433f0afe317)


Conclusion:
The project demonstrates the applicability of the Pythagorean Expectation model in cricket analytics, offering a systematic approach to evaluating team performance and predicting match outcomes in the IPL cricket tournament.



The project focuses on analyzing cricket matches from the Indian Premier League (IPL) 2018 season to understand the relationship between runs scored and match outcomes. It involves data preprocessing, visualization, and analysis using Python and various libraries such as pandas, numpy, and matplotlib.
Key Steps:
1.	Data Loading and Preprocessing:
•	The project begins by importing necessary libraries such as pandas, numpy, and matplotlib.
•	Data is loaded from an Excel file containing IPL 2018 match results (IPL2018_results.xlsx).
2.	Exploratory Data Analysis (EDA):
•	Initial EDA involves examining the distribution of runs scored in each innings using histograms.
•	The distribution of runs scored by winning and losing teams is compared using histograms to understand their differences.
3.	Detailed Analysis of a Specific Game:
•	A specific IPL 2018 game between the Mumbai Indians and the Chennai Super Kings is selected for detailed analysis.
•	Ball-by-ball data for the selected game (MIvCSKadj.xlsx) is loaded and visualized to analyze the progress of each team in terms of runs scored and wickets lost.
•	The analysis includes plotting the runs scored and wickets lost by each team over the course of the game.
![Screenshot (151)](https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/d59bf6f9-9118-4d20-8098-259851d7d568)
5.	Function Definitions for Comparative Analysis:
•	Two functions are defined to facilitate comparative analysis of multiple IPL games:
•	plot_runs_wickets: This function plots the runs and wickets for each team in a specified game.
![Screenshot (154)](https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/e45280d1-0a46-4b60-817a-41536e3f6ad7)

•	plot_runs_wickets_multi_game: This function allows plotting runs and wickets for multiple games simultaneously.
![Screenshot (152)](https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/0ad95d06-0ee3-44a5-8812-f625d2e82bc5)


Conclusion: The project aims to provide insights into the performance of IPL teams based on runs scored and wickets lost, both at the individual game level and through comparative analysis across multiple games. Through data visualization and analysis, the project seeks to uncover patterns and trends that may influence match outcomes in the IPL 2018 season.


Overview: The project aims to analyze the relationship between cricket player performance and salary in the context of the Indian Premier League (IPL) using statistical methods. By examining various performance metrics and their impact on player salaries, we seek to gain insights into the factors influencing player compensation in one of the world's most prestigious cricket leagues.

Approach:
1.	Data Acquisition and Exploration:
•	Import cricket player data from the IPL18Player.csv dataset.
•	Conduct exploratory data analysis (EDA) to understand the structure of the dataset, identify missing values, and gain initial insights into player statistics.
2.	Feature Engineering:
•	Create dummy variables to categorize players based on their roles, such as batsman, bowler, and wicketkeeper.
•	Calculate performance metrics, including batting average, batting strike rate, bowling average, and bowling strike rate, to quantify player performance.
3.	Regression Analysis:
•	Utilize multiple regression models to examine the relationship between player performance metrics and salary.
•	Explore different combinations of independent variables, such as runs scored, number of wickets taken, and batting/bowling averages, to assess their impact on player salaries.
•	Evaluate the regression models using statistical measures such as coefficients, p-values, and R-squared values to understand the predictive power of player performance metrics on salary determination.
![image](https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/dee2d554-cbff-46bd-8612-8806d1e9ba81)

<img width="516" alt="salary~runs+bowls+not_outs" src="https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/0e0b7683-4d7b-4eb6-9220-1e8a8ae0890d">

<img width="510" alt="salary~batting_avg+batting_strike" src="https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/9fd6315a-ea3a-4d5b-8ad1-57cd64ac335a">

<img width="510" alt="salary~runs_conceded" src="https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/c437f197-c7c7-4cde-a6e2-85ea9bb87667">

<img width="528" alt="salary~bowling_Avg+bowling_strike" src="https://github.com/Vishwajeet0830/CricAnalysis/assets/73867969/06ab28f6-867a-495b-880b-6d5e3a45f047">


Key Findings:
•	Identification of significant performance metrics influencing player salaries in the IPL.
•	Insights into the relative importance of batting and bowling performance in determining player compensation.
•	Understanding the nuances of player valuation in professional cricket leagues and potential implications for team management and player recruitment strategies.

Conclusion: The analysis provides valuable insights into the relationship between player performance and salary in the IPL, shedding light on the factors driving player compensation in the cricketing landscape. By leveraging statistical techniques, the project contributes to a deeper understanding of the dynamics governing player valuation and aids decision-making processes for teams and stakeholders in the cricket industry.

