#                                             GIVEN ARRAYS ARE ALREADY SORTED 
#                                             BRUTE FORCE APPROACH
def arrayIntersection(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    vis = [0]* m
    ans = []
    for i in range(n):
        for j in range(m):
            if nums1[i] == nums2[j] and vis[j] == 0:
                ans.append(nums1[i])
                vis[j] = 1
                break
                
            elif nums1[i]<nums2[j]:
                break
    return ans



#                                           OPTIMAL APPROACH
def arrayIntersection(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    i,j = 0,0
    ans = []
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            i +=1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            ans.append(nums1[i])
            i += 1
            j += 1
    return ans


nums1 = [1,2,3,3,4,5]
nums2 = [1,2,3,3,4]
print(arrayIntersection(nums1,nums2))



