# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicate = set()
        def is_valid(node):
            if (node and node.next and node.val is not None and node.val == node.next.val) or node.val in duplicate:
                duplicate.add(node.val)
                return False
            return True
        current = head
        # prev points to correct value
        dummy = ListNode(float('-inf'))
        prev = dummy
        while current:
            if prev.val != current.val:
                # valid condition
                if is_valid(current):
                    #print("current", current)
                    prev.next = current
                    prev = current
                    current = current.next
                else:
                    # print("prev", prev)
                    prev.next = current.next
                    current = current.next
            else:
                current = current.next


        return dummy.next
        