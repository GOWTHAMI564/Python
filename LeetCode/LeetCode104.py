
# 104. Maximum Depth of Binary Tree
'''Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth( root) :
        def findheight(root):
            if(root==None):
                return 0
            lh=findheight(root.left)
            rh=findheight(root.right)
            return 1+max(lh,rh)
        return findheight(root)