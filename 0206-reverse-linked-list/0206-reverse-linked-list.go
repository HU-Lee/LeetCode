/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    q := head
    var arr []int
    for q != nil {
        arr = append(arr, q.Val)
        q = q.Next
    }
    q = head
    i := len(arr) - 1
    for q != nil {
        q.Val = arr[i]
        i--
        q = q.Next
    }
    return head
}