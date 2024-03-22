/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    var arr []int
    q := head
    for q != nil {
        arr = append(arr, q.Val)
        q = q.Next
    }
    i,j := 0, len(arr)-1
    for i < j {
        if arr[i] != arr[j] {
            return false
        }
        i++
        j--
    }
    return true
}