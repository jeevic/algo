
"""
层次遍历序列化
"""

class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.traverse(root)

    def traverse(self, root):
        if root is None:
            return ""
        queue = []
        queue.append(root)
        size = len(queue)
        ser = ""

        while len(queue) > 0:
            i = size
            while i > 0:
                node = queue.pop(0)
                if node is None:
                    ser += ",#"
                else:
                    ser += ",{}".format(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                i -= 1
        return ser.lstrip(",")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        l = data.split(",")
        print(l)
        queue = []
        root = TreeNode(l[0])
        queue.append(root)
        i = 0
        while i < len(l) - 1:
            size = len(queue)
            j = 0
            while j < size:
                node = queue.pop(0)
                i += 1
                left_val = l[i]
                if left_val != "#":
                    left_node = TreeNode(left_val)
                    node.left = left_node
                    queue.append(left_node)

                i += 1
                right_val = l[i]
                if right_val != "#":
                    right_node = TreeNode(right_val)
                    node.right = right_node
                    queue.append(right_node)
                j += 1

        return root

"""
前序遍历
"""
class Codec2:
    serialize_str = ""
    sep = ","
    null = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.traverse(root)
        return self.serialize_str.lstrip(self.sep)

    def traverse(self, root):
        if root is None:
            self.serialize_str += "{}{}".format(self.sep, self.null)
            return

        self.serialize_str += "{}{}".format(self.sep, root.val)

        self.traverse(root.left)
        self.traverse(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        queue = data.split(self.sep)
        print(queue)
        return self.construct(queue)

    def construct(self, queue):
        if len(queue) == 0:
            return None
        val = queue.pop(0)
        if val == "#":
            return None
        root = TreeNode(val)
        left = self.construct(queue)
        right = self.construct(queue)
        root.left = left
        root.right = right
        return root

"""
后续遍历
"""


class Codec:
    serialize_str = ""
    sep = ","
    null = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.traverse(root)
        return self.serialize_str.lstrip(self.sep)

    def traverse(self, root):
        if root is None:
            self.serialize_str += "{}{}".format(self.sep, self.null)
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.serialize_str += "{}{}".format(self.sep, root.val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None

        queue = data.split(self.sep)
        print(queue)
        return self.construct(queue)

    def construct(self, queue):
        if len(queue) == 0:
            return None
        val = queue.pop()
        if val == "#":
            return None
        root = TreeNode(val)
        right = self.construct(queue)
        left = self.construct(queue)
        root.left = left
        root.right = right
        return root
