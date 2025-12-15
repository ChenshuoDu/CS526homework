Final Exam 

Q1 – Dam Breaking

The main challenge of this problem is deciding which crack to fix at each time unit. Since only one crack can be fixed per time unit, choosing the wrong crack may cause flooding later.

The key observation is that every unfixed crack grows by 1 unit each time unit. Because of this, older cracks always become more dangerous over time. At any given time, the crack with the largest current size contributes the most water and will continue to grow if it is not fixed.

To represent this efficiently, each crack is stored using the value:

base = initial_size − appearance_time

At time t, the actual size of a crack is:

current_size = base + t

Since all cracks increase by the same amount t, their relative order never changes. Therefore, comparing base values is sufficient.

All unfixed cracks are stored in a max heap. At each time unit, the crack with the largest base value is fixed. I also keep track of the number of unfixed cracks and the sum of their base values so the total incoming water can be computed efficiently.

This greedy strategy works because fixing the largest crack always minimizes future water accumulation. Leaving a larger crack unfixed while fixing a smaller one will always lead to more water in later time units.


Running Instructions (PowerShell):

Get-Content flood_1.txt | python q1.py

Q2 – Downhill Skier

The main difficulty of this problem is finding the longest strictly decreasing path on a grid where movement is allowed in eight directions.

The key observation is that the longest downhill path starting from a cell depends only on its neighboring cells with lower altitude. Since each move must go to a strictly lower cell, cycles are impossible.

Dynamic programming is used with the definition:

dp[r][c] = length of the longest strictly decreasing path (number of cells)
           starting from cell (r, c)

All cells are processed in ascending order of altitude. This guarantees that when computing dp[r][c], all valid lower neighbors already have their dp values computed.

For each cell, all eight neighbors are checked. Among the neighbors with lower altitude, the maximum dp value is selected and dp[r][c] is set to 1 plus that value.

The maximum value in the dp table represents the longest downhill path in terms of cells visited. The problem output expects the number of moves, so the final answer is computed as:

moves = cells − 1


Running Instructions (PowerShell):

Get-Content ski_input1.txt | python q2.py
