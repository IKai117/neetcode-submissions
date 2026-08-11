# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        num = 1
        while right.next != None:
            right = right.next
            num += 1
        m = num - n 

        # if num == 1:
        #     dummy.next = None
        #     return dummy.next
        for i in range(m):

            left = left.next   

        left.next = left.next.next

        return dummy.next       