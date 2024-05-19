import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        head = tail = ListNode(0)

        for i in lists:
            if i: 
                heapq.heappush(h, i)

        while h:
            node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            if node.next: 
                heapq.heappush(h, node.next)

        return head.next
