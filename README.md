# chess

Proper attribution and link to any existing code used in project:

We are planning to implement this chess960 version in our code: https://github.com/aStieber/Chess960/blob/master/README.md instead of using the library

For monte carlo implementation, we took help from https://www.geeksforgeeks.org/ml-monte-carlo-tree-search-mcts/

To use the pychess library : https://python-chess.readthedocs.io/en/latest/

Installation :
We used python code. To run the code we need to install the dependencies: 
Write "pip install chess" in command prompt to install the chess library



Explanation of how to run the computer experiments:

The board is randomized as per chess960 rules, it can also be customized based on the programmer's choice using the command:
chess.Board("all the positions that you want")
There will be 16 pieces for each players. There will be 8 pawns, 2 bishops, 2 knights, 2 rooks, 1 queen, and 1 king.
White side will have first letters of all the pieces with small letter (p,b,k,r,q,k) and human will have all the pieces with capital letter (P,B,K,R,Q,K).

The game is Ai and human based. 

After you run the code, AI will give the first move and you will be the second player. 
human needs to give two input each time. First one is where they want their piece to go and second one is the row and colum of which piece they want to move. here row is from a to h and colum is from 1 to 8.
If you choose invalid move, game will be over that time.
