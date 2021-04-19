# Big O Notation

- O(1): constant
- O(n): touch every element in a list once

# Arrays vs. Linked Lists

- Arrays allow fast reads and random access.
- Linked lists allow fast inserts and deletes but only sequential access.

# Selection sort

- O(n^2): going through a list of n items n times
- E.g. pushing most played songs into a new sorted array
- Repeatedly finds the min/max element and putting it at the beginning

# Recursion

- Function calls itself
- Recursive case and base case (to avoid stack overflow)
- May take up a lot of memory, function calls go onto the call stack

# Quicksort

- O(n log n): average case (stack size is O(log n))
- O(n^2): worst case (stack size is O(n))
- Picking a _random_ pivot and recursively calling quicksort on the two sub-arrays created
- Faster than merge sort (smaller constant)

# Merge sort

- Divide and conquer
- O(n log n)

# Hash tables

- O(1) time
- Takes up extra space

# Graphs

- Consists of nodes and edges
- Can use BFS if unweighted
- Topological sort: ordered list from graph i.e. A depends on B
- Directed graph: unilateral edge/relationship
- Undirected graph: bilateral (a cycle)

# Breadth-First-Search (BFS)

- Check if there is a path and find the shortest path (smallest number of nodes) in an unweighted graph
- Runtime is O(V+E)
- The queue's runtime is O(n); searching the entire graph is at least O(E)

# Stacks

- First in LAST out
- Push and pop
- E.g. matching brackets problem

# Queues

- First in FIRST out
- Enqueue and deque

# Trees

- Basically a graph where all edges point one-way only e.g. family tree

# Djikstra's Algorithm

- Find the fastest path in a weighted graph
- Only works on directed acyclic graphs (DAGs)
- Cannot be used with negative-weight edges (use Bellman-Ford)

# Greedy Algorithms

- At each step, pick the locally optimal solution, in the end you're left with the globally optimal solution
- E.g. scheduling problem - pick the event that ends the earliest, pick the event that starts after the first event and ends the earliest.
- Good for approximation algorithms: when calculating the optimal solution will take too much time.

# NP-complete problems

- Problems with no fast algorithmic solution
- How to tell if a problem might be NP-complete:
  1. "All combinations" or "every possible version"
  2. Involves a sequence or a set
  3. Can be restated as the 'traveling salesman' or 'set-covering' problem
  4. Runs quickly with few items but really slowly with more items
