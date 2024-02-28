# Description of the project :-
•This is basically a point based game of snake, water and gun .
•The game is having two modes 1.Human vs Human / 2.Human vs Computer
•This game will ask the user to select the mode and number of rounds
•Rules of the game 
 1. Snake wins over water
 2. Water wins over Gun
 3. Gun wins over Snake

•Will play the game for number of rounds and within each round will ask players to enter choices and at the end will anounce the winner
•After tournament of game it will ask user to chose to exit or not.
•And the cycle of game repeats until user wants to quit.
•In this game whenever the user provides Invalid Input , it will ask the user to exit the game.

# Description of main.py
Functions of the game :
- main()
	Firstly, it welcomes the user in the game.
	Ask the mode and number of rounds and initiates the game.

- userinput(msg,val) : 
      Its a common or a Universal input function for all types of user input including to mode, number of rounds to play, choices for each round and to exit.
      Its parameter msg contains the message to be displayed for the user, val contains its corresponding valid values.
	  It return user inputed value.
     

- exit():
      This function allows user to exit at any given invalid input.

- play_game(md, nr):
	This function will take parameter mode(md) and number of rounds(nr) to play. 
	The game will be played according to the number of rounds .
	If the selected mode is human vs human then it will ask input for both the players
	,else if the selected mode is human vs computer then it will take one input from the player and other input will be a random choice on behalf of computer.
	It will also evaluate the winning points and return it.	

- point_checker(ch1, ch2)
	This function will compare the parameters according to the rules of the game.
	It returns 0 if it's the same parameter,1 or 2 respectively player1 or player2
	

- winner(md, res1, res2)
	This function compares the points and will return the Result of the game in string format. 