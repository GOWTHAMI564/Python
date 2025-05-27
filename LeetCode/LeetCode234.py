'''234. Palindrome Linked List'''
'''
Input: head = [1,2,2,1]
Output: true
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(head) :
        arr=[]
        temp=head
        while(temp):
            arr.append(temp.val)
            temp=temp.next
        return arr==arr[::-1]