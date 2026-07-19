# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []
        tail = head
        while tail:
            ifcycle = True
            if tail.val in arr:
                last = arr.index(tail.val)
                count = 0
                for i in range(len(arr) - last-1):
                    count += 1
                    if tail.val != arr[last]:
                        ifcycle = False
                    arr.append(tail.val)
                    tail = tail.next
                    last += 1
                if ifcycle and count == len(arr) - last:
                    return True
            arr.append(tail.val)
            tail = tail.next

        return False

