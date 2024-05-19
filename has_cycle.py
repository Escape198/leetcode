class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = head.next

print("Связанный список содержит цикл:", has_cycle(head))  # True

head_no_cycle = ListNode(1)
head_no_cycle.next = ListNode(2)
head_no_cycle.next.next = ListNode(3)

print("Связанный список содержит цикл:", has_cycle(head_no_cycle))  # False
