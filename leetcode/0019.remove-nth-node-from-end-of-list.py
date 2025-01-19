# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while(temp):
            count += 1
            temp = temp.next
        lNode = count - n
        if(lNode == 0):
            return head.next
        current = head
        tCount = 0
        dummy = ListNode()
        tail = dummy
        while(current and current.next):
            if tCount == lNode - 1:
                current.next = current.next.next
                tail.next = current
                break;
            tail.next = ListNode(current.val)
            tail = tail.next
            tCount += 1
            current = current.next
        return dummy.next
        
