#  153. Find Minimum in Rotated Sorted Array
'''
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''

def findMin(nums) :
    n=len(nums)
    low=0
    high=n-1
    Min=float("inf")
    while low<=high:
        mid=(low+high)//2
        if nums[low]<=nums[mid]:
            if nums[low]<Min:
                Min=nums[low]
            low=mid+1
        if nums[mid]<=nums[high]:
            if nums[mid]<Min:
                Min=nums[mid]
            high=mid-1
    return Min
nums=list(map(int,input().split()))
print(findMin(nums))




