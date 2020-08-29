# Backtracking search

## Intuition

### General pattern

In general, a good way to think about backtracking problems is to see it as a form of tree traversal.

```python

result = []
def backtrack(path, options):
    if condition_satisfied:
        result.add(path)
        return

    for option in options:
            results.append(option)
            backtrack(path, options)
            results.remove(option)
```
