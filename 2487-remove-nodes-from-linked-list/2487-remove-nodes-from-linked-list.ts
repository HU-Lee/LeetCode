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

function removeNodes(head: ListNode | null): ListNode | null {
    const stack = []
    let node = head
    while (node !== null) {
        while (stack.length > 0 && stack[stack.length-1] < node.val) {
            stack.pop()
        }
        stack.push(node.val)
        node = node.next
    }
    let ans = new ListNode(stack[0], null)
    let curr = ans
    for (let i=1; i<stack.length; i++) {
        curr.next = new ListNode(stack[i], null)
        curr = curr.next
    }
    return ans
};