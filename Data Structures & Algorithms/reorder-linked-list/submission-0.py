# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        #找到中點
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #將後半反轉
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        #合併
        first = head
        second = prev
        while second: #因為second較短
            temp1,temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2