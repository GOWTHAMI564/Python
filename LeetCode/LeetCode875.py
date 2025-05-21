'''Koko Eating Bananas -- LeetCode , GFG '''
'''
Examples:
Input: arr[] = [3, 6, 7, 11] , k = 8
Output: 4
Explanation: Koko eats at least 4 bananas per hour to finish all piles within 8 hours, as she can consume each pile in 1 + 2 + 2 + 3 = 8 hours.
Input: arr[] = [30, 11, 23, 4, 20], k = 5
Output: 30
Explanation: With 30 bananas per hour, Koko completes each pile in 1 hour, totaling 5 hours, which matches k = 5.
Input: arr[] = [5, 10, 15, 20], k = 7
Output: 10
Explanation: At 10 bananas per hour, Koko finishes in 7 hours, just within the k = 7 limit.
'''

#binary search 
from math import*
class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        low=1
        high=max(arr)
        while(low<=high):
            div=(low+high)//2
            Sum=0
            for num in arr:
                Sum+=ceil(num/div)
            if(Sum<=k):
                high=div-1
            else:
                low=div+1
        return low
sol=Solution()
arr=[1,2,5,9]
k=6
res=sol.smallestDivisor(arr,k)
print(res)