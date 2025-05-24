'''410. Split Array Largest Sum'''
'''Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.'''


def splitArray( nums, k) :
    def canWeAllocate(maxPages,nums):
        no_of_pages_allocated=nums[0]
        students=1
        for pages in range(1,len(nums)):
            if(nums[pages]+no_of_pages_allocated<=maxPages):
                no_of_pages_allocated+=nums[pages]
            else:
                no_of_pages_allocated=nums[pages]
                students+=1
        return students
    if(k>len(nums)):
        return -1
    low=max(nums)
    high=sum(nums)
    
    while(low<=high):
        maxPages=(low+high)//2
        if canWeAllocate(maxPages,nums)<=k:
            high=maxPages-1
        else:
            low=maxPages+1
    return low
                
nums=[7,2,5,10,8]
k=2
print(splitArray( nums, k))




