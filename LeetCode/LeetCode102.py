# 102. Binary Tree Level Order Traversal
'''Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder( root) :
        if root==None:
            return []
        q=[root]
        ans=[]
        while(q):
            level=[]
            for i in range(len(q)):
                node=q.pop(0)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)
        return ans