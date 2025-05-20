def searchInsert(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if(nums[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
nums=list(map(int,input().split()))
target=int(input())



'''
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''