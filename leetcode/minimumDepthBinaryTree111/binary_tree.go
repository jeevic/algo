package minimumDepthBinaryTree111

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func MinDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queens := make(QueenTrees, 0, 1)

	queens.Enqueue(root)
	var step int = 1

	for !queens.Empty() {
		size := queens.Len()
		for i := 0; i < size; i++ {
			cur := queens.Dequeue()
			if cur.Left == nil && cur.Right == nil {
				return step
			}
			if cur.Left != nil {
				queens.Enqueue(cur.Left)
			}
			if cur.Right != nil {
				queens.Enqueue(cur.Right)
			}
		}
		step++
	}
	return step
}

type QueenTrees []*TreeNode

func (q *QueenTrees) Enqueue(node *TreeNode) {
	*q = append(*q, node)
}

func (q *QueenTrees) Dequeue() *TreeNode {
	if q.Len() > 0 {
		node := (*q)[0]
		*q = (*q)[1:]
		return node
	}
	return nil
}

func (q *QueenTrees) Len() int {
	return len(*q)
}

func (q *QueenTrees) Empty() bool {
	return q.Len() == 0
}
