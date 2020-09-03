# Dynamic Programming

## Introduction

## Components

- Memoization
- Recursion
- Enumeration
- State machine
- State transitioning
- Sub problems

### Big ideas

- Top down approach
  - Recursive tree search with caching
- Bottom up approach

## Intuition

- Brute force

## Common tricks for optimization

- Loop backwards to reduce using additional space

## Beware of these pitfalls

- Getting the wrong state transition equation

## Practical tips

### When to use DP?

- Consider using DP when you have to **make choices** to arrive at the solution. Specifically, it is applicable when you can construct a solution to the given instance from solutions to smaller sub problems of the same kind.
- Optimization problems
- Decision and counting problems
  - Any problems where you can express a solution recursively in terms of the same computation of smaller sub problems

### Recursive vs iterative

Though conceptually DP often involves recursion, it is often much more efficient to build the cache **bottom up** iteratively

When DP is implemented recursively, a dynamic data structure, such as a hashtable or a BST is used to store the cached results. When implemented iteratively the cache is usually a one or multi-dimensional array

In some instances, **recursion can actually outperform a bottom-up DP solution**. Usually in these circumstances the solution is found early, or subproblems can be pruned with bounding.

### Getting to an optimal implementation

To save space, cache space may be recycled once it is known that a set of entries will not be looked up again.

### What do typical DP questions look like?

- Optimization problems
  - Maximization, minimization
    - Keywords to look out for: Longest, shortest, maximum, minimum, best, largest, smallest etc.
    - Examples:
      - Knapsack problem
      - Stock picking problems
  - Combinatorial enumeration problems
    - Find all of something, find total
    - Examples:
      - How many ways to climb a flight of stairs
      - How many ways to find a number
  -
