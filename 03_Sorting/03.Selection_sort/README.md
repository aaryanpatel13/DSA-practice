# 📌 Selection Sort Algorithm

![Algorithm](https://img.shields.io/badge/Algorithm-Selection%20Sort-blue)
![Time](https://img.shields.io/badge/Time%20Complexity-O(n²)-red)
![Space](https://img.shields.io/badge/Space%20Complexity-O(1)-green)

---

## 📌 About
## Selection Sort is a simple comparison-based sorting algorithm

In this algorithm, the array is divided into:
- a **sorted part**
- an **unsorted part**

The algorithm repeatedly selects the **minimum element** from the unsorted part and places it at the **beginning** of the sorted part.

---

## 🧠 How Selection Sort Works
1. Assume the **first index** as the minimum
2. Compare it with all remaining elements
3. Find the **smallest element** in the unsorted part
4. Swap it with the first unsorted element
5. Move the boundary of the sorted part one step ahead
6. Repeat until the array is sorted

---

## 🪜 Algorithm Steps
1. Repeat for `i = 0` to `n-2`
2. Set `min_index = i`
3. For `j = i + 1` to `n-1`:
   - If `arr[j] < arr[min_index]`, update `min_index`
4. Swap `arr[i]` with `arr[min_index]`

---

## 📊 Example
**Input:**
```text
nums = [5, 1, 4, 2]

Step-by-step execution:
Pass 1: [1, 5, 4, 2]
Pass 2: [1, 2, 4, 5]
Pass 3: [1, 2, 4, 5]


💻 Implementation
```python
def selection_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]
    
    return nums
