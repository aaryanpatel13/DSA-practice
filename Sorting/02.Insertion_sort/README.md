# 🧩 Insertion Sort Algorithm

![Algorithm](https://img.shields.io/badge/Algorithm-Insertion%20Sort-blue)
![Time](https://img.shields.io/badge/Time%20Complexity-O(n²)-red)
![Space](https://img.shields.io/badge/Space%20Complexity-O(1)-green)

---

## 📌 About
## Insertion Sort is a simple sorting algorithm where we build the sorted array one element at a time

In this algorithm, the array is divided into:
- a **sorted part**
- an **unsorted part**

Elements from the unsorted part are picked one by one and placed at their **correct position** in the sorted part.


---

## 🧠 How Insertion Sort Works
1. Assume that the **first element is already sorted i.e `i = 0`**
2. Now pick second element from the array i.e `i = 1`
3. Store the element as : `key = array[i]`
4. Compare `key` with elements present before it.
5. Shift the bigger element to the right.
6. Repeat until the entire array is sorted

---

## 🪜 Algorithm Steps
1. Repeat for `i = 1` to `n-1`
2. Store `key = arr[i]`
3. Set `j = i - 1`
4. While `j >= 0` and `arr[j] > key`:
   - Shift `arr[j]` to `arr[j+1]`
   - Decrement `j`
5. Place `key` at position `j + 1`

---

## 📊 Example
**Input:**
```text
nums = [5, 1, 4, 2]

Step-by-step execution:
Pass 1: [1, 5, 4, 2]
Pass 2: [1, 4, 5, 2]
Pass 3: [1, 2, 4, 5]
```
---

**Implementation:**
```python
def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1
        
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        
        nums[j + 1] = key
    
    return nums

