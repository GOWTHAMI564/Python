'''
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10'''

class Solution:
    def singleNonDuplicate(nums) :
        n=len(nums)
        if(n==1):
            return nums[0]
        elif(nums[0]!=nums[1]):
            return nums[0]
        elif(nums[n-1]!=nums[n-2]):
            return nums[n-1]
        low=1
        high=n-2
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            #Ur on the left  half so single element is on right 
            elif((mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1])):
                low=mid+1
            #Ur on the right half so single element is on left
            elif((mid%2==0 and nums[mid]==nums[mid-1]) or (mid%2==1 and nums[mid]==nums[mid+1])):
                high=mid-1
nums = [1, 2, 2, 3, 3]
result = Solution.singleNonDuplicate(nums)
print(result)   




