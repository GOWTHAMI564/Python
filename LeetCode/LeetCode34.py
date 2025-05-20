# 34. Find First and Last Position of Element in Sorted Array --LeetCode


def searchRange(nums,target) :
        def getLowerBound(nums,target):
            n=len(nums)
            low=0
            high=n-1
            ans=-1
            while(low<=high):
                mid=(low+high)//2
                if (nums[mid]>=target):
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans
        def getUpperBound(nums,target):
            n=len(nums)
            low=0
            high=n-1
            ans=n
            while(low<=high):
                mid=(low+high)//2
                if(nums[mid]>target):
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            return ans

        lb=getLowerBound(nums,target)
        if(lb==-1 or nums[lb]!=target):
            return [-1,-1]
        ub=getUpperBound(nums,target)-1
        return [lb,ub]

nums=list(map(int,input().split()))
target=int(input())
print(searchRange(nums,target))
# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]