Problem 1 – Merge Sort, Quick Sort, Insertion Sort

For this part I implemented three sorting algorithms: Merge Sort, Quick Sort, and Insertion Sort.
I created three input files (small, medium, large) and used run_q1.py to run all of them.

Main ideas of each algorithm:

Insertion Sort
I scan the array from left to right and insert each value into its correct position in the already-sorted part.
It’s simple but slow for big inputs (worst case O(n**2)).

Merge Sort
I use divide-and-conquer: split the list, sort each half, and merge them back.
The merge step is the key.
It always runs in O(n log n).

Quick Sort
I pick a pivot, split the array into smaller/equal/greater parts, and recursively sort the sides.
It’s usually very fast, but can be O(n**2) if the pivot is bad.

How to run:

cd q1
python run_q1.py


The script prints both the original input and the sorted results.

Problem 2 – Radix Sort

In this problem I implemented an LSD Radix Sort for non-negative integers.
I process the array digit by digit (ones → tens → hundreds), place numbers into 0–9 buckets based on the current digit, and rebuild the list after each pass.

Radix Sort doesn’t compare numbers directly, so it can be very fast when the digit lengths are similar.
Time is roughly O(d · (n + k)), where d is the number of digits.

How to run:

cd q2
python run_q2.py


The program loads the three input files and prints the original values and the sorted output.

Problem 3 – Gale–Shapley Stable Matching

I implemented the classic Gale–Shapley algorithm (men-proposing version).
There are n men and n women, and each person has a full preference list.

How the algorithm works:

All men start free.

A free man proposes to the next woman on his list.

A woman accepts if she is free, or compares the new proposer with her current match.

She keeps the one she prefers, and the rejected man becomes free again.

Repeat until no men are free.

This guarantees a stable matching (no two people prefer each other over their current partners).

I tested my code using the professor’s files: marraige_ten.txt, marriage_hundred.txt, and marraige_thousand.txt.
My script saves the full output to a new *_output.txt file so the entire result can be viewed easily.

How to run:

cd q3
python run_q3.py marraige_ten.txt
python run_q3.py marriage_hundred.txt
python run_q3.py marraige_thousand.txt


Each run generates an output file containing the input preferences and the final stable matching.