## Game of Chess  


                                             Introduction

Using the lichess dataset we plan to create a dropdown function to sort by different aspects of data. Some aspects that we plan to use are the player rating(how good a player is), opening moves(what standard chess openings were played), win type(checkmate, resign, timeout), and game result(white win, black win, draw). 

The user will be able to interact with these different identifiers to find out more about how the games are influenced by these factors. For example: the user could use our tool to figure out how player rating impacts the win type or frequency of different openings. Most of our data will be visualized in bar charts or pie charts that are able to demonstrate differences in the data. 

We will be using dynamic query for our project. The reason for our choice of dynamic query is that we believe it will facilitate the user in searching for their topics of interest. We also plan to use bar charts and pie charts interchangeably to fit the data that is being shown. For some, for example player rating, bar charts would be easier to interpret data like the average rating of all players. For others, like player vs player win data, it would be easier to see a pie chart for a ratio between two players.



                                           Problem and Motivations

The motivation for our project was our interest in chess, and how different factors would impact the outcome of online chess matches. We wanted to take into consideration things like rating, white vs. black, number of moves, game time, and how it relates to the outcome of the game. This is worth addressing because it can give some insight into one of the most popular strategy games of all time.


                                           Definitions
                                           
Turns: How many turns the game took to resolve

Victory Status: What caused the game to end (out of time, resign, checkmate, draw)

Rating: A player's matchmaking rank for online chess. Higher rating typically means the player's skill is higher. For Lichess, the average player is at around 1500 rating.

Average Rating: The average rating of the 2 players on white and black

Moves: The moves that occurred during the entire game’s playtime






                                             Visualizations
 1. Average Game Length - This graph shows the average number of moves for a game at 4 different skill levels. As we can see, there is a positive correlation between skill and longer game length. 
                        
![Graph 1](docs/assets/1.jpg)


2. Game length by the opening with variation - This graph shows some different openings and how the many moves the resulting games take on average. It shows that opening can impact game length quite heavily.

![Graph 2](docs/assets/2.jpg)


3. Missing Title - This graph shows how often a game ends a certain way. It shows that most games end by resignation of one player, and very few games end in a draw. 

![Graph 3](docs/assets/3.jpg)


4. Victorious Color - This graph shows the outcome of games at different skill levels. An interesting takeaway is that white has a distinct advantage at all levels, and that draws are much more likely at the pro level.

![Graph 4](docs/assets/4.jpg)


5. Victory Status by the Game Rating - This graph shows how likely a certain a game ending is a different skill levels. It shows that checkmate is relatively unlikely at pro level relative to other levels of play. 

![Graph 5](docs/assets/5.jpg)


6,7. Win by Opening and Level - These two graphs show how likely a win is in a certain openings, filtered by skill levels. It shows that some opening are better at different skill levels. 

![Graph 6](docs/assets/6.jpg)

![Graph 7](docs/assets/7.jpg)


8. Winner by the Opening with Variation in % - This graph shows the likelihood of an outcome for different openings. With this graph you can see which openings are better for which color, and which result in more draws. 

![Graph 8](docs/assets/8.jpg)

9,10. Winner by Opening and Level - These two graphs show the likelihood of an outcome for different openings. With these graphs you can see which openings are better for which color, and which result in more draws.

![Graph 9](docs/assets/9.jpg)

![Graph 10](docs/assets/10.jpg)



![Graph 11](docs/assets/11.jpg)



![Graph 12](docs/assets/12.jpg)



![Graph 13](docs/assets/13.jpg)






                                              Group Roles
                                                                  
During our project the work has been split up this way so far:

John - Creating the filtering system

Peter - Working on the charts

Mudit - Creating the website

Isaac - Interpreting data and creating writeups

                                                                  
                                               Challenges
                                               
Some of the challenges that we had to overcome during the process of creating our project were:
Interpreting vague or obscure data from the csv file.
Solving bugs in our interface
Working through scheduling differences during finals time.
                                                                  
                                                                  
                                                                  
                                                                  
                                                                  
