# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        if head is None:
            return None
        while head is not None:
            arr.append(head.val)
            head=head.next
        arr.sort()
        a=ListNode(arr[0])
        temp=a
        for i in range(1,len(arr)):
            a.next=ListNode(arr[i])
            a=a.next
        return temp