class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _ = l1.val + l2.val
        digit, ten = _ % 10, _ // 10

        answer = ListNode(digit)

        if any((ten, l1.next, l2.next)):
            l1_next = l1.next if l1.next else ListNode(0)
            l2_next = l2.next if l2.next else ListNode(0)
            l1_next.val += ten

            answer.next = self.addTwoNumbers(l1_next, l2_next)
        return answer

# O(n) временная
