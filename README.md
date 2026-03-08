Simple Math Game
----------------------------------------------------------------
HackBU 2026 Submission 
Created by Ian Porto, Ryan Zhang, Alston Zhang, and Jason Seng

Program Purpose
----------------------------------------------------------------
The purpose of our program is to create an engaging way to practice math problems, mainly algebra and calculus. 

Program Functionality
----------------------------------------------------------------
The program works by prompting the user to select a difficulty - the more difficult, the more enemies and obstacles there are. The user wins by moving towards and reaching the target destination (marked by a green box on the map). In order to move, the user must answer one of the aforementioned questions. The longer the game goes on, the harder the questions become (Basic Algebra -> Advanced Calculus). 
The enemy moves using the A* Algorithm. The A* Algorithm checks all four cardinal directions, running a series of math equations to determine which one gets closest to the user. If there is a tie in judgement, a tiebreaker occurs whereby the same process is repeated for these two directions. 

AI Usage
----------------------------------------------------------------
- AI was used to debug several parts of our code to fix errors and logical errors
- AI was additionally used to create ai.py, specifically to work out the logic of the Manhattan Distance (A* Algorithm) for enemy movement