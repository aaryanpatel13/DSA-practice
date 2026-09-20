# Binary Search

Binary search finds the position of a target value in a **sorted** array by repeatedly dividing the array into two parts and eleminating the non-required part.

- **Time:** O(log n)
- **Space:** O(1) iterative, O(log n) recursive (call stack)
- **Requirement:** the data must be sorted (or monotonic with respect to the predicate you're testing)

---

## How It Works

Maintain two pointers, `low` and `high`, that mark the current search range.

1. Set `low = 0` and `high = n - 1`.
2. Compute the middle index: `mid = low + (high - low) // 2`.
3. Compare `arr[mid]` with the target:
   - `arr[mid] == target` → found, return `mid`
   - `arr[mid] < target` → eleminate the left half, `low = mid + 1`
   - `arr[mid] > target` → eleminate the right half, `high = mid - 1`
4. Repeat while `low <= high`.
5. If the loop ends without a match, the target is not in the collection — return `-1`.

### Walkthrough

Searching for `13` in `[1, 3, 5, 8, 13, 21, 34]`:

| Step | low | high | mid | arr[mid] | Action |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 6 | 3 | 8 | `8 < 13` → search right, `low = 4` |
| 2 | 4 | 6 | 5 | 21 | `21 > 13` → search left, `high = 4` |
| 3 | 4 | 4 | 4 | 13 | match → return `4` |

---

## Iterative Approach

The loop keeps shrinking the range until the target is found or the range becomes empty. It uses no extra stack frames, so memory stays constant.

### Python Code

```python
def binary_search(arr, target):
    """Return the index of target in sorted arr, or -1 if absent."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example
arr = [1, 3, 5, 8, 13, 21, 34]
print(binary_search(arr, 13))   # 4
print(binary_search(arr, 7))    # -1
```

---

## Recursive Approach

The same logic, expressed by having the function call itself on the surviving half. The base case is an empty range (`low > high`), which means the target is absent.


### Python Code

```python
def binary_search_rec(arr, target, low=0, high=None):
    """Recursive binary search. Returns the index of target, or -1."""
    if high is None:
        high = len(arr) - 1

    if low > high:                 # base case: empty range
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, high)
    else:
        return binary_search_rec(arr, target, low, mid - 1)


# Example
arr = [1, 3, 5, 8, 13, 21, 34]
print(binary_search_rec(arr, 34))   # 6
print(binary_search_rec(arr, 2))    # -1
```

---
### Comparison with Linear Search

| n | Linear search (worst) | Binary search (worst) |
| --- | --- | --- |
| 100 | 100 | 7 |
| 1,000 | 1,000 | 10 |
| 1,000,000 | 1,000,000 | 20 |
| 1,000,000,000 | 1,000,000,000 | 30 |