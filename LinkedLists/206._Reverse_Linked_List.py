class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

