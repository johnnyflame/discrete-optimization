# Local Search

## Intuition

The key idea behind local search is to start from a complete by suboptimal configuration, often randomly initialized, to a more optimal configuration by making moves locally. This is fundamentally different from constraint programming, where the key aim is to look for feasible extensions to existing feasible partial solutions.

## Key terminology

- Neighborhoods
- States

## How Local Search approaches various kinds of problems

- Constraint satisfaction problems
- Optimization problem
- Constraint satisfaction problem

## Topics

- Min/Max violation
- Swap neighborhood
- Optimization
- Optimality vs feasibility
- Complex neighborhood

## Min/Max violation

### Eight queen problem demonstration

## Swap neighborhood

### Solving the Car sequencing problem with swapping

- We first generate an arbitrary configuration of cars
- Then we count the number of violations using a sliding window
- Then we swap configurations causing violations with each other, until eventually all violations have been resolved.

It's natural to ask why do we want to swap configurations with each other instead of assignment. The key reason is that in the context of this car sequencing problem, there is actually a hard constraint, which is the number of cars that must be produced. This constraint should be satisfied at all times, which is what swapping allows us to do.

Key takeaway: swapping is used where there are constraints that are "hard" and cannot change. We keep them fixed by creating an initial state that satisfies these, then using swap to satisfy other constraints while keeping the hard constraint satisfied at all times.

## Optimization, warehouse locations, TSP

- 2-opt/k-opt algorithm used to solve TSP

This is a method to define local neighborhood.

### Optimality vs feasibility, graph coloring

## Complex neighborhoods, sports scheduling

## Escaping local minima

## Connectivity

Connectivity is important because if the solution space is disconnected, it may not be possible to find the global optimum (because you simply cannot reach it). This is not to say you'll definitely

### How can we test connectivity?

A simple algorithm exists to test this property.
