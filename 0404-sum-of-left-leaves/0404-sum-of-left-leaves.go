/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	} else if root.Left != nil && root.Left.Left == nil && root.Left.Right == nil {
        return root.Left.Val + sumOfLeftLeaves(root.Right)
    } else {
        return sumOfLeftLeaves(root.Left) + sumOfLeftLeaves(root.Right)
    }
}