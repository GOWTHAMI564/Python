''' 1423. Maximum Points You Can Obtain from Cards '''
'''
Example 1:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 '''
class Solution:
    def maxScore(self,cardPoints,k) :
        n=len(cardPoints)
        left=0
        right=k-1
        leftSum=sum(cardPoints[left:right+1])
        rightSum=0
        maxSum=leftSum
        rightIndex=n-1
        for i in range(k-1,-1,-1):
            leftSum-=cardPoints[i]
            rightSum+=cardPoints[rightIndex]
            maxSum=max(maxSum,leftSum+rightSum)
            rightIndex-=1
        return maxSum
sol=Solution()
cardPoints=list(map(int,input().split()))
k=int(input())
print(sol.maxScore(cardPoints,k))