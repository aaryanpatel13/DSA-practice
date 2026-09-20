# 🫧 Bubble Sort Algorithm

![Algorithm](https://img.shields.io/badge/Algorithm-Bubble%20Sort-blue)
![Time](https://img.shields.io/badge/Time%20Complexity-O(n²)-red)
![Space](https://img.shields.io/badge/Space%20Complexity-O(1)-green)

---

## 📌 About
## In Bubble sort algorithm, adjacent elements are compared and swapped if they are in the wrong order.  
With each pass, the **largest element "bubbles up" to the end** of the array.

---

## 🧠 How Bubble Sort Works
1. Start from the **first element**
2. Compare it with the **next adjacent element**
3. Swap them if the current element is greater
4. Continue this process till the end of the array
5. Repeat for remaining elements until the array is sorted

---

## 🪜 Algorithm Steps
1. Repeat for `i = 0` to `n-1`
2. Set a flag `swapped = False`
3. Compare adjacent elements from `j = 0` to `n - i - 2`
4. If `arr[j] > arr[j+1]`, swap them and set `swapped = True`
5. If no swaps occur in a pass, break the loop (array is sorted)

---

## 📊 Example
**Input:**
```text
nums = [5, 1, 4, 2]

Step-by-step execution:
Pass 1: [1, 5, 4, 2]
        [1, 4, 5, 2]
        [1, 4, 2, 5]

Pass 2: [1, 2, 4, 5]

Pass 3: No swaps → Array sorted
```

## IMPLEMENTATION
```python
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        
        if not swapped:
            break
    
    return nums

