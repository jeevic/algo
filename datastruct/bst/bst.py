
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        初始化二叉树节点

        参数:
            val (int): 节点的值，默认为0
            left (TreeNode): 左子节点，默认为None
            right (TreeNode): 右子节点，默认为None

        返回值:
            无
        """
        self.val = val
        self.left = left
        self.right = right


class Bst:
    root = None

    def __init__(self):
        pass

    def resetTree(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return self.root

        self.insertNode(self.root, val)
        return self.root

    def insertNode(self, node, val):
        if node is None:
            return TreeNode(val)
        if node.val > val:
            node.left = self.insertNode(node.left, val)

        if node.val < val:
            node.right = self.insertNode(node.right, val)

        return node

    def search(self, val):
        return self.searchBst(self.root, val)

    def searchBst(self, node, val):
        if node is None:
            return None
        if node.val == val:
            return node
        if node.val > val:
            return self.searchBst(node.left, val)
        if node.val < val:
            return self.searchBst(node.right, val)

    def delete(self, val):
        self.root = self.deleteNode(self.root, val)
        return self.root

    def deleteNode(self, node, val):
        if node is None:
            return None
        if node.val == val:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # 找一个节点顶上来 找右侧最小节点 或 左侧最大节点
            # 同时将节点删除
            minNode = self.getMinRight(node)
            node.right = self.deleteNode(node.right, minNode.val)

            minNode.left = node.left
            minNode.right = node.right
            node = minNode
        elif node.val > val:
            node.left = self.deleteNode(node.left, val)
        elif node.val < val:
            node.right = self.deleteNode(node.right, val)

        return node

    def getMinRight(self, node):
        while node.left is not None:
            node = node.left
        return node

    res = []

    def print(self):
        self.res = []
        self.printNode(self.root)
        return self.res

    def printNode(self, node):
        if node is None:
            return
        self.printNode(node.left)
        self.res.append(node.val)
        self.printNode(node.right)


if __name__ == '__main__':
    bst = Bst()
    bst.insert(2)
    bst.insert(1)
    bst.insert(4)
    bst.insert(3)

    print(bst.print())

    node = bst.search(3)
    print(node.val)
    print(bst.print())

    bst.delete(3)
    print(bst.print())

    bst.delete(4)
    print(bst.print())

    bst.delete(2)
    print(bst.print())

    bst.delete(1)
    print(bst.print())
