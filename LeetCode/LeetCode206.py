# 206. Reverse Linked List

'''Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList( head) :
        temp=head
        arr=[]
        while(temp):
            arr.append(temp.val)
            temp=temp.next
        arr=arr[::-1]
        i=0
        temp=head
        while(temp):
            temp.val=arr[i]
            i+=1
            temp=temp.next
        return head