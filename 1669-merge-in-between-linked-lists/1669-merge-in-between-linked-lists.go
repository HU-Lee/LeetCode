/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeInBetween(list1 *ListNode, a int, b int, list2 *ListNode) *ListNode {
    a_node := list1
    b_node := list1
    for i:=1; i<=b; i++ {
        if i < a {
            a_node = a_node.Next
        }
        b_node = b_node.Next
    }
    b_node = b_node.Next

    end_list2 := list2
    for end_list2.Next != nil {
        end_list2 = end_list2.Next
    }

    end_list2.Next = b_node
    a_node.Next = list2

    return list1
}