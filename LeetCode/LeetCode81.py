# 81. Search in Rotated Sorted Array II -- leetcode --gfg


def search(nums,target) :
    n=len(nums)
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if (nums[mid]==target):
            return True
        if(nums[low]==nums[mid]==nums[high]):
            low+=1
            high-=1
        elif(nums[low]<=nums[mid]):
            if(nums[low]<=target<=nums[mid]):
                high=mid-1
            else:
                low=mid+1
        elif(nums[mid]<=nums[high]):
            if(nums[mid]<=target<=nums[high]):
                low=mid+1
            else:
                high=mid-1
    return False
nums=list(map(int,input().split()))
target=int(input())
print(search(nums,target))



# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
 