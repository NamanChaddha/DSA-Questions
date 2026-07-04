class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        pres = head.next
        head = pres
        last = None
        while True:
            temp = pres.next     
            temp2 = temp.next if temp else None
            pres.next = prev
            if last:
                last.next = pres     
            if temp is None:
                prev.next = None
                break
            if temp2 is None:
                prev.next = temp
                break
            prev.next = temp2       
            last = prev
            prev = temp
            pres = temp2
        return head
