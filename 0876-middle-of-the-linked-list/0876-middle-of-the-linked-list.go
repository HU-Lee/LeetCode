/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    middle := head
    fw := head

    for {
        if fw.Next == nil {
            break
        } else if fw.Next.Next == nil {
            middle = middle.Next
            break
        }
        middle = middle.Next
        fw = fw.Next.Next
    }
    return middle
}