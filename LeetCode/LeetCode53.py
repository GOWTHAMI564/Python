'''53. Maximum Subarray''' # we cant apply sliding window since there is no k
'''
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.'''

class Solution:
    def maxSubArray(self, nums) :
        n=len(nums)
        maxSum=float("-inf")
        currSum=0
        for i in nums:
            currSum+=i
            maxSum=max(maxSum,currSum)
            if(currSum<0):
                currSum=0
        return maxSum
nums = [5,4,-1,7,8]
sol=Solution()
print(sol.maxSubArray(nums))
