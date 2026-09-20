# ⚡ Quick Sort Algorithm

![Algorithm](https://img.shields.io/badge/Algorithm-Quick%20Sort-blue)
![Average Time](https://img.shields.io/badge/Average%20Time-O(n%20log%20n)-green)
![Worst Time](https://img.shields.io/badge/Worst%20Time-O(n²)-red)
![Space](https://img.shields.io/badge/Space%20Complexity-O(log%20n)-yellow)

---

## 📌 About
**Quick Sort** is a fast and efficient **divide-and-conquer** sorting algorithm.

It works by selecting a **pivot element** and rearranging the array such that:
- elements smaller than the pivot are placed on the left
- elements greater than the pivot are placed on the right

This process is recursively applied to both subarrays until the entire array is sorted.

---

## 🧠 How Quick Sort Works
1. Choose a pivot element from the array
2. Partition the array around the pivot
3. Place the pivot in its correct sorted position
4. Recursively sort the left and right subarrays

---

## 🪜 Algorithm Steps
1. If the array has 0 or 1 element, return
2. Select a pivot element
3. Rearrange elements based on the pivot
4. Recursively apply Quick Sort on both sides

---

## 📊 Example
**Input:**
```text
nums = [10, 7, 8, 9, 1, 5]
Pivot = 5
After partition → [1, 5, 10, 7, 8, 9]
Final sorted array → [1, 5, 7, 8, 9, 10]
```
## 🧩 Implementation (Python – Hoare Partition)

```python
def partition(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while (i<j):
        while nums[i] <= pivot and i <= high -1:
            i = i+1
        while nums[j]> pivot and j >= low +1:
            j = j-1
        if (i<j):
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]

    return j


def quick_sort(nums,low,high):
    #base case
    if low >= high:
        return
    p= partition(nums,low,high)
    quick_sort(nums,low,p-1)
    quick_sort(nums,p+1,high)

    return nums

#Example usage

nums = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(nums,0,len(nums)-1)
print(f"Sorted array is : {sorted_array}")





