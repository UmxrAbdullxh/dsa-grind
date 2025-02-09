# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummyTail = dummy
        count = 0
        curr = head
        temp = ListNode()
        tail = temp

        temp2 = ListNode()
        tail2 = temp2 
        
        while curr:
            tail.next = ListNode(curr.val)
            tail = tail.next
            count += 1
            if count % k == 0:
                reversedList = self.reverseList(temp.next)
                dummyTail.next = reversedList
                while dummyTail.next:
                    dummyTail = dummyTail.next
                temp = ListNode()
                tail = temp

                temp2 = ListNode()
                tail2 = temp2
            else:
                tail2.next = ListNode(curr.val)
                tail2 = tail2.next
            curr = curr.next
        if temp2:
            dummyTail.next = temp2.next
        ## print(arr)
        return dummy.next
    
    def reverseList(self, linkedList):
        prev = None
        curr = linkedList
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        
