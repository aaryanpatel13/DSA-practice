# 📌 Merge Sort Algorithm

![Algorithm](https://img.shields.io/badge/Algorithm-Merge%20Sort-blue)
![Time](https://img.shields.io/badge/Time%20Complexity-O(n%20log%20n)-red)
![Space](https://img.shields.io/badge/Space%20Complexity-O(n)-green)

---

## 📌 About
## Merge Sort is a divide-and-conquer based sorting algorithm

In this algorithm, the array is:
- **divided** into smaller subarrays
- each subarray is **sorted recursively**
- sorted subarrays are **merged** to form the final sorted array

Merge Sort is known for its **consistent performance** and **stability**.

---

## 🧠 How Merge Sort Works
1. Divide the array into two halves
2. Recursively sort the left half
3. Recursively sort the right half
4. Merge the two sorted halves
5. Repeat until the entire array is sorted

---

## 🪜 Algorithm Steps
1. If the array has 1 or 0 elements, it is already sorted
2. Find the middle index
3. Split the array into two halves
4. Recursively apply merge sort on both halves
5. Merge the sorted halves into one sorted array

---

## 📊 Example
**Input:**
```text
nums = [5, 1, 4, 2]
Split: [5, 1] | [4, 2]
Split: [5] [1] | [4] [2]

Merge: [1, 5] | [2, 4]
Final Merge: [1, 2, 4, 5]
```


## 💻 Implementation

```python
def merge_arr(left,right):
    result = []
    i = j = 0
    n = len(left)
    m = len(right)

    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    if i<n:
        while i<n:
            result.append(left[i])
            i += 1
    if j<m:
        while j<m:
            result.append(right[j])
            j +=1
    return result

def Merge_sort(nums,low,high):
    #Base case
    if low >= high:
        return [nums[low]]

    #Recursive case
    mid  = (low+high)//2
    left = Merge_sort(nums,low,mid)
    right = Merge_sort(nums,mid+1,high)
    sorted_array = merge_arr(left,right)
    
    return sorted_array

```

