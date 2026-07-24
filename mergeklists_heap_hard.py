# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap=[]
        if lists==[]:
            return None
        else:
            if len(lists)==1:
                return lists[0]
            for i in range(len(lists)):
                head=lists[i]
                s=head
                while s is not None:
                    heapq.heappush(minheap,s.val)
                    s=s.next
            if minheap==[]:
                return None
            s=ListNode(heapq.heappop(minheap))
            head2=s
            s.next=None
            while minheap:
                ss=heapq.heappop(minheap)
                t=ListNode(ss)
                s.next=t
                s=s.next
            return head2
            
