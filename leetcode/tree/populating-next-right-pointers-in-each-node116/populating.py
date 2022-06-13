class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root
        l = []
        l.append(root)

        while len(l) > 0:
            size = len(l)
            i = 0
            while i < size:
                node = l[i]
                next = None
                if i + 1 < size:
                    next = l[i + 1]
                node.next = next
                if node.left != None:
                    l.append(node.left)
                if node.right != None:
                    l.append(node.right)
                i += 1
            i = 0
            while i < size:
                l.pop(0)
                i += 1
        return root


class Solution2:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if node1 is None or node2 is None:
            return
        node1.next = node2
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)

