package minimumDepthBinaryTree111

import "testing"

func InitTree(arr []int) *TreeNode {
	length := len(arr)
	if length < 0 {
		return nil
	}
	var nodeArr = make([]*TreeNode, length)
	root := new(TreeNode)
	root.Val = arr[0]
	nodeArr[0] = root
	for i := 1; i < length; i++ {
		node := new(TreeNode)
		val := arr[i]
		if val > 0 {
			nodeArr[i] = node
			node.Val = val

			if i%2 == 0 {
				nodeArr[(i-1)/2].Right = node
			} else {
				nodeArr[(i-1)/2].Left = node
			}
		}

	}
	return root
}

func InitTree2() *TreeNode {
	root := new(TreeNode)
	root.Val = 2
	root.Left = nil

	temp := root
	for _, val := range []int{3, 4, 5, 6} {
		cur := new(TreeNode)
		cur.Val = val
		temp.Right = cur
		temp = cur
	}
	return root
}

type Question struct {
	Input  *TreeNode
	Output int
}

var qs []Question = []Question{
	{Input: InitTree([]int{3, 9, 20, -1, -1, 15, 7}), Output: 2},
	{Input: InitTree2(), Output: 5},
}

func TestMinDepth(t *testing.T) {
	for _, q := range qs {
		depth := MinDepth(q.Input)
		if depth == q.Output {
			t.Logf("input:%v output:%d match depth:%d", q.Input, q.Output, depth)
		} else {
			t.Errorf("[error]input:%v output:%d not match depth:%d", q.Input, q.Output, depth)
		}
	}
}
