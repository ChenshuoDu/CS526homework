Name: Chenshuo Du  
Course: CS526 – Data Structures and Algorithms  

Problem 1 – Snowfall
The program reads how much snow fell over several days.
The first number is how many days there are, and the second line has the cumulative totals. I convert these totals into daily snow by subtracting each day’s value from the previous day’s value.
Then I slide through all 3-day windows and check if any of them add up to more than half of the total snow.  
If yes - print YES, otherwise - print NO.

Run example:
    python q1.py snowfall_input1.txt

Example output:
    1 4 10 14 15 17 17 23 solution: YES


Problem 2 – Pandemic
This program simulates the spread of infection in an N*N grid.
The first line is the grid size, and each line after that has the coordinates of infected counties (row and column).

Each day, a healthy county becomes infected if at least two of its four neighbors are infected. 
The process repeats until no new infections happen. 
Finally, it prints whether there are any healthy counties left or not.

Run example:
    python q2.py pandemic_input1.txt
    python q2.py pandemic_input2.txt

Example output:
    There are healthy counties left
    There are no healthy counties left

Problem 3 – Shopping Cart
This program finds how many items can be picked in a row when you only have two baskets. 
Each basket can only hold one category.
I use a sliding window with a counter to keep track of at most two categories at a time. 
The longest valid sequence is the answer.

Run example:
    python q3.py sc_input1.txt

Example output:
    3 items were selected


Problem 4 – Symbol Puzzle Game
This is like a Sudoku check. The input has:
1. n (board size)
2. a line of symbols separated by commas
3. n lines with the board (dots mean empty)

The program checks that each row, column, and sub-board has no duplicate symbols. 
Then it prints whether the board is valid or invalid.

Run example:
    python q4.py spg_input1.txt
    python q4.py spg_input2.txt

Example output:
    The board is valid
    The board is invalid


How to Run (for all problems)
Make sure you are inside the correct folder.
For example:
    cd q1
    python q1.py snowfall_input1.txt

All programs use Python 3 and do not need any extra libraries.
