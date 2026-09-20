# 2D Array

A **2D Array** is an array of arrays represented in the form of **rows and columns**.

Example:

```text
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Here:

- Rows = `3`
- Columns = `3`
- `arr[i][j]` → element at row `i`, column `j`

---

## 1. Creating a 2D Array

```python
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

---

## 2. Accessing Elements

```python
arr[0][0]  # 1
arr[1][2]  # 6
arr[2][1]  # 8
```

General form:

```python
arr[row][column]
```

---

## 3. Traversing a 2D Array

```python
rows = len(arr)
cols = len(arr[0])

for i in range(rows):
    for j in range(cols):
        print(arr[i][j])
```

### Time Complexity

```text
O(rows × cols)
```

---

## 4. Row-wise Traversal

```python
for i in range(rows):
    for j in range(cols):
        print(arr[i][j])
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

---

## 5. Column-wise Traversal

```python
for j in range(cols):
    for i in range(rows):
        print(arr[i][j])
```

Output:

```text
1 4 7
2 5 8
3 6 9
```

---

## 6. Taking Input

For a matrix with `n` rows and `m` columns:

```python
n = int(input())
m = int(input())

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
```

---

## 7. Sum of All Elements

```python
total = 0

for i in range(rows):
    for j in range(cols):
        total += arr[i][j]

print(total)
```

### Time Complexity

```text
O(rows × cols)
```

---

## 8. Find Maximum Element

```python
maximum = float("-inf")

for i in range(rows):
    for j in range(cols):
        maximum = max(maximum, arr[i][j])

print(maximum)
```

---

## 9. Find Minimum Element

```python
minimum = float("inf")

for i in range(rows):
    for j in range(cols):
        minimum = min(minimum, arr[i][j])

print(minimum)
```

---

# Diagonals

For a square matrix:

```text
1 2 3
4 5 6
7 8 9
```

## 10. Main Diagonal

Main diagonal:

```text
1 5 9
```

Condition:

```python
i == j
```

Code:

```python
for i in range(n):
    print(arr[i][i])
```

---

## 11. Secondary Diagonal

Secondary diagonal:

```text
3 5 7
```

Condition:

```python
i + j == n - 1
```

Code:

```python
for i in range(n):
    print(arr[i][n - 1 - i])
```

---

# Boundary Traversal

For:

```text
1 2 3
4 5 6
7 8 9
```

Boundary elements:

```text
1 2 3 6 9 8 7 4
```

Boundary consists of:

- Top
- Right
- Bottom
- Left

---

# Common Mistakes

## ❌ Wrong for Rectangular Matrix

```python
for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j])
```

This only works correctly when the matrix is **square**.

## ✅ Correct

```python
rows = len(arr)
cols = len(arr[0])

for i in range(rows):
    for j in range(cols):
        print(arr[i][j])
```

---

## Index Range

Valid row indices:

```text
0 → rows - 1
```

Valid column indices:

```text
0 → cols - 1
```

So:

```python
arr[i][j]
```

must satisfy:

```text
0 <= i < rows
0 <= j < cols
```

---

# Complexity

For a matrix of `R × C`:

| Operation | Complexity |
|---|---:|
| Access `arr[i][j]` | O(1) |
| Traverse matrix | O(R × C) |
| Search | O(R × C) |
| Find Min/Max | O(R × C) |
| Extra Matrix | O(R × C) |

---

# ⭐ Important Formulas

```text
Rows    = len(arr)
Columns = len(arr[0])

Element = arr[i][j]

Valid row index    → 0 to rows - 1
Valid column index → 0 to cols - 1

Main diagonal      → i == j
Secondary diagonal → i + j == n - 1
```
