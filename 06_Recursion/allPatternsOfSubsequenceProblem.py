#                   PRINT ALL THE SUBSEQUENCES WHOSE SUM = K

def subsequence(indx,nums,subs,curr_sum,k):
    n = len(nums)
    # BASE CASE
    if indx == n:
        if curr_sum == k:
            print(subs)
        return

    # PICK ELEMENT
    subs.append(nums[indx])
    curr_sum += nums[indx]
    subsequence(indx+1,nums,subs,curr_sum,k)

    #BACK TRACKING
    subs.pop()
    curr_sum -= nums[indx]

    # NOT PICK ELEMENT
    subsequence(indx+1,nums,subs,curr_sum,k)

nums = [1,2,1]
k = 2
subsequence(0,nums,[],0,k)



#                           TYPE 2: PRINT ANY ONE SUBSEQUENCE WITH SUM = K

def subsequence(indx,nums,subs,curr_sm,k):
    n = len(nums)
    # BASE CASE
    if indx == n:
        if curr_sm == k:
            print(subs)
            return True
        return False
    
    # PICK ELEMENT
    subs.append(nums[indx])
    curr_sm += nums[indx]
    if subsequence(indx+1,nums,subs,curr_sm,k):
        return True

    # BACK TRACK
    subs.pop()
    curr_sm -= nums[indx]

    # NOT PICK ELEMENT
    if subsequence(indx+1,nums,subs,curr_sm,k):
        return True
    return False

nums = [1,2,1]
k = 2
subsequence(0,nums,[],0,k)



#                           TYPE 3: COUNT THE NUMBER OF SUBSEQUENCES WITH SUM = K
#                       WE DON'T NEED TO STORE SUBSEQUENCES HERE. JUSR KEEP A CHECK ON CURRENT SUM

def subsequence(indx,nums,curr_sm,k):
    n = len(nums)
    #ASE CASE
    if indx == n:
        if curr_sm == k:
            return 1
        return 0
    
    
    # PICK ELEMENT
    curr_sm += nums[indx]
    left = subsequence(indx+1,nums,curr_sm,k)

    # BACK TRACK
    curr_sm -= nums[indx]

    # NOT PICK ELEMENT
    right = subsequence(indx+1,nums,curr_sm,k)

    # RETURN COUNT
    return left + right

nums = [1,2,1]
k = 2
print(subsequence(0,nums,0,k))