## Rotate Array Problem
Array can be rotated in two ways:
`Left rotation` and `Right Rotation`

## Left rotation:
``` 
Example

Input: nums = [1, 2, 3, 4, 5, 6], k = 2  ; Here k means rotate the array by k steps
Output: nums = [3, 4, 5, 6, 1, 2]

```

## Right rotation:
``` 
Example

Input: nums = [1, 2, 3, 4, 5, 6], k = 2 ; Here k means rotate the array by k steps
Output: nums = [5,6,1,2,3,4]

```
## Brute Force Method
```
Time Complexity for brute force method: O(n+k)
Space Complexity for brute force method: O(k)

Here we use a temp array to store the value whihc is going to be shifted later.
```
```python

def rotateArray(nums,k): 
    n = len(nums)
    k = k % n
    temp = []
    i= 0
    while i <= k:
        temp.append(nums[i])
        i += 1
    #Shifting
    for i in range(k,n):
        nums[i-k] = nums[i]

    # j = 0   this can be written as  i-(n-k)
    for i in range(n-k,n):  # i = [n-k = 4] to n = 7 
            nums[i] = temp[i-(n-k)]
            
    return nums
```


## Optimal mehtod by using slicing
```
Time Complexity for brute force method: O(2n)
Space Complexity for brute force method: O(1)

Here we do not use any temp array to store the value whihc is going to be shifted later.
We do the changes right there in the given array.
```
```python
def rotateArray(nums,k):
    n = len(nums)
    k = k%n
    first = nums[:n-k]  #We are slicing it
    first.reverse()

    second = nums[n-k:]
    second.reverse()

    result = first + second
    result.reverse()
    
    nums[:] = result
```
## Optimal mehtod by using Reverse() method

```python
def reverse(nums,start,end):
    n = len(nums)
    while start < end:
        temp = nums[start]
        nums[start] = nums[end-1]
        nums[end-1] = temp
        start += 1
        end -= 1
    return nums
def rotateArray(nums,k):
    n = len(nums)
    k = k % n

    reverse(nums,0,n-k)
    reverse(nums,n-k,n)
    reverse(nums,0,n)

```

```python
#EXAMPLE
k = int(input("Enter the value for rotation: "))
nums = [1,2,3,4,5,6,7]
rotate = rotateArray(nums,k)
print(rotate)

```