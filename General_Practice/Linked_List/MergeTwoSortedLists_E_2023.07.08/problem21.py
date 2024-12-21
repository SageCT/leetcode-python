from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ans = ListNode()
        head = ans
        while list1 and list2:
            if list2.val < list1.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next

        if list1:
            head.next = list1

        elif list2:
            head.next = list2

        return ans.next
