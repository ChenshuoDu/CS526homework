
Name: Chenshuo Du
Course: CS526 – Data Structures and Algorithms

q1
Tree Traversal
Preorder: A B E H F I C D G
Breadth-first: A B C D E F G H I
Postorder: H E I F B C G D A

Inorder Traversal
G, D, B, E, A, C, H, F, I

q2 – Fewest Elements Whose Sum > T

File: q2/q2.py
The idea for this problem is pretty straightforward.  
I sorted all the numbers from largest to smallest and started adding them up until the total went over T.  
Then I counted how many numbers I used.  
This greedy method makes sense because taking larger values first always reaches the target faster.  
(Time complexity: O(n log n))


q3 – Count Right Triangles

File: q3/q3.py
For this one, I used a geometry and hashing approach instead of the slow triple loop.  
I fixed one point as the corner of the right angle and looked at the direction vectors from that point to every other point.  
If two vectors are perpendicular (their dot product = 0), they form a right triangle.  
I used a hash map to count each direction and its perpendicular direction.  
This reduces the time from O(n^3) to about O(n^2), which runs fast even for 1000 points.