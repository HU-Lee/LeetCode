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

function doubleIt(head: ListNode | null): ListNode | null {
    let node = head;
    const stack: number[] = []
    while (node !== null) {
        stack.push(node.val)
        node = node.next
    }
    let carry = 0
    let lastNode = null
    while (stack.length > 0) {
        const x = stack.pop()
        const val = x*2 + carry;
        carry = val >= 10 ? 1 : 0;
        const newNode = new ListNode(val%10, lastNode);
        lastNode = newNode
    }
    if (carry !== 0) {
        lastNode = new ListNode(carry, lastNode)
    }
    return lastNode
};