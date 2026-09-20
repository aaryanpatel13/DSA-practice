#Input: nums1 = [1,2,3,4], nums2 = [1,2,7]
#Output: [1,2,3,4,7]
#                                       GIVEN ARRAYS ARE ALREADY SORTED 
#                                       BRUTE FORCE APPROACH
def findUnion(nums1, nums2):
    st = set()
    for i in range(len(nums1)):
        st.add(nums1[i])
    for i in range(len(nums2)):
        st.add(nums2[i])
    result = sorted(st)
    return result



#                                       OPTIMAL APPROACH
def findUnion(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i,j = 0,0
    result = []
    while i < n and j < m:
        if nums1[i] <= nums2[j]:
            if not result or result[-1] != nums1[i]:
                result.append(nums1[i])
            i += 1
        else:
            if not result or result[-1] != nums2[j]:
                    result.append(nums2[j])
            j +=1
    while i < n:
        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    while j < m:
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1 
    return result



# EXAMPLE CASE
nums1 = [1,2,3,5]
nums2 = [3,4]
print(findUnion(nums1, nums2))

