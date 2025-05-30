'''3. Longest Substring Without Repeating Characters'''
'''
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxLen=0
        for i in range(0,n):
            checker=[0]*256
            for j in range(i,n):
                if(checker[ord(s[j])]==1):
                    break
                checker[ord(s[j])]=1
                maxLen=max(maxLen,j-i+1)
        return maxLen        


''' TC : O(N2) SC : O(N) '''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right=0
        left=0
        n=len(s)
        d={}
        maxLen=0
        while(right<n):
            if(s[right] in d):
                if(d[s[right]]>=left):
                    left=d[s[right]]+1
            d[s[right]]=right
            maxLen=max(maxLen,right-left+1)
            right+=1
        return maxLen
