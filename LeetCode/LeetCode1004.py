
'''1004. Max Consecutive Ones III'''
'''
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''


class Solution:
    def longestOnes(self, nums, k):
        n=len(nums)
        maxLen=0
        left=0
        right=0
        count_zero=0
        while(right<n):
            if(nums[right]==0):
                count_zero+=1
            if(count_zero>k):
                while(count_zero>k):
                    if(nums[left]==0):
                        count_zero-=1
                    left+=1
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
sol=Solution()
print(sol.longestOnes(nums,k))