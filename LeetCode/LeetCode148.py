'''148. Sort List'''
'''
Input: head = [4,2,1,3]
Output: [1,2,3,4]
 '''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(head) :
        arr=[]
        temp=head
        while(temp):
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        ind=0
        temp=head
        while(temp):
            temp.val=arr[ind]
            ind+=1
            temp=temp.next
        return head