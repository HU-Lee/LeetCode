/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    // group by 2 half
    slow := head
    fast := head
    for fast.Next != nil && fast.Next.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
    }

    // reverse
    var target *ListNode = slow.Next
    var prev *ListNode = nil    
    for target != nil {
        temp := target.Next
        target.Next = prev
        prev = target
        target = temp
    }

    // delete the tail
    slow.Next = nil

    left := head
    right := prev

    // merge
    for right != nil {
        tmp_left := left.Next
        tmp_right := right.Next
        left.Next = right
        right.Next = tmp_left
        left = tmp_left
        right = tmp_right
    }
}