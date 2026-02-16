/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    let head = new ListNode()
    let temp = head
    let current = list1
    let current2 = list2
    while(current && current2) {
        if(current.val <= current2.val) {
            temp.next = new ListNode(current.val)
            current = current.next
        }
        else {
            temp.next = new ListNode(current2.val)
            current2 = current2.next
        }
        temp = temp.next
    }
    if(current) {
        temp.next = current
    }
    if(current2) {
        temp.next = current2
    }
    return head.next
};