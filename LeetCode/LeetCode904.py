'''904. Fruit Into Baskets'''
'''
Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
'''

class Solution:
    def totalFruit(self, fruits) :
        n=len(fruits)
        maxLen=0
        left=0
        right=0
        d={}
        while(right<n):
            if(fruits[right] in d):
                d[fruits[right]]+=1
            else:
                d[fruits[right]]=1
            if(len(d)>2):
                while(len(d)>2):
                    d[fruits[left]]-=1
                    if(d[fruits[left]]==0):
                        del d[fruits[left]]
                    left+=1
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen
fruits = [0,1,2,2]
sol=Solution()
print(sol.totalFruit(fruits))