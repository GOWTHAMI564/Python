# 33. Search in Rotated Sorted Array--leetcode
def search(nums,target) :
    n=len(nums)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        # check if left half is sorted    
        elif(nums[low]<=nums[mid]):
            if (nums[low]<=target<=nums[mid]):
                    high=mid-1
            else:
                low=mid+1
        # check if right half is sorted
        elif(nums[mid]<=nums[high]):
            if (nums[mid]<=target<=nums[high]):
                low=mid+1
            else:
                high=mid-1  
    return -1
nums=list(map(int,input().split()))
target=int(input())
print(search(nums,target))



'''
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''