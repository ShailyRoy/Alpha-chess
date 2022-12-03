# chess

Proper attribution and link to any existing code used in project:
We are planning to implement this code in our code: https://github.com/aStieber/Chess960/blob/master/README.md

For monte carlo implementation, we took help from https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/

To use the pychess library : https://python-chess.readthedocs.io/en/latest/

Installation :
We used python code. To run the code we need to install the dependencies: 
Write "pip install chess" in command prompt to install the chess library



Explanation to run interactive domain program:


Explanation of how to run the computer experiments:
The board is randomized as per chess960 rules, it can also be customized based on the programmer's choice using the command:
chess.Board("all the positions that you want")

The game is Ai and human based. 
After you run the code, AI will give the first move and you will be the second player. 
human needs to give two input each time. First one is where they want their piece to go and second one is the row and colum of which piece they want to move. here row is from a to h and colum is from 1 to 8.
If you choose invalid move, game will be over that time.
