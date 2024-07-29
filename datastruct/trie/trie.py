"""
 Trie前缀树实现
 @see https://mp.weixin.qq.com/s/hGrTUmM1zusPZZ0nA9aaNw
"""


class TrieNode:
    """
     TreeNode节点
    """
    # 如果value有值, 代表是单词的结尾
    value = None
    # 存储 子节点value
    children = {}


class TrieMap:
    size = 0
    root = None

    def __init__(self):
        self.size = 0
        self.root = TrieNode()

    # 从节点 node 开始搜索 key，如果存在返回对应节点，否则返回 null
    def _get_node(self, node, key):
        p = node
        for char in key:
            if p is None:
                return None
            p = node.children.get(char, None)
        return p

    # 添加 key
    def put(self, key, value):
        if not self.contains_key(key):
            self.size += 1

        self.root = self._put_traverse(self.root, key, value, 0)
        return True

    def _put_traverse(self, node, k, v, idx):
        if node is None:
            # 子节点不存在
            node = TrieNode()
        if idx == len(k):
            node.value = v
            return node
        c = k[idx]
        node.children[c] = self._put_traverse(node, )

    # 删除key
    def remove(self, key):
        if self.contains_key(key) is None:
            return
        self._remove_traverse(self.root, key, 0)
        self.size -= 1

    def _remove_traverse(self, node, key, idx):
        if node is None:
            return None
        if idx == len(key):
            # 找到对应node 删除 value
            node.value = None
        else:
            c = key[idx]
            child = self._remove_traverse(node.children.get(c), key, idx + 1)
            if child is None:
                del node.children[c]
            else:
                node.children[c] = child
        if len(node.children) == 0 and node.value is None:
            return None
        return node

    # 获取 key 对应的值
    # 搜索 key 对应的值，不存在则返回 null
    def get(self, key):
        last = self._get_node(self.root, key)
        if last is None or last.value is None:
            return None
        return last.value

    # 判断 key 是否存在 true/false
    def contains_key(self, key):
        return True if self.get(key) is not None else False

    # 在Map的所有键中搜索query的最短前缀
    # shortestPrefixOf("themxyz") -> "the"
    def shortest_prefix_of(self, query):
        p = self.root
        for idx, char in enumerate(query):
            if p is None:
                return ""
            if p.value is not None:
                return query[0:idx]
            p = p.children.get(char, None)

        if p is not None and p.value is not None:
            return query

        return ""

    # 在 Map 的所有键中搜索 query 的最长前缀
    # longestPrefixOf("themxyz") -> "them"
    def longest_prefix_of(self, query):
        long_idx = 0
        p = self.root
        for idx, char in enumerate(query):
            if p is None:
                break
            if p.value is not None:
                long_idx = idx
            p = p.children.get(char, None)

        if p is not None and p.value is not None:
            return query
        return query[0:long_idx]

    # 搜索所有前缀为prefix 的键
    # keysWithPrefix("th") -> ["that", "the", "them"]
    def keys_with_prefix(self, prefix):
        res = []
        # 前缀的最后一个节点
        x = self._get_node(self.root, prefix)
        if x is None:
            return res
        self._prefix_traverse(x, prefix, res)

    def _prefix_traverse(self, node, path, res):
        """"""
        if node is None:
            return
        if node.value is not None:
            res.append(path)

        for char, nxt in node.children.items():
            path = path + char
            self._prefix_traverse(nxt, path, res)
            path = path[0:len(path) - len(char)]
        return res

    # 判断是和否存在前缀为 prefix 的键
    # hasKeyWithPrefix("tha") -> true
    # hasKeyWithPrefix("apple") -> false
    def has_key_prefix(self, prefix):
        return True if self._get_node(self.root, prefix) is not None else False

    # 通配符 . 匹配任意字符，搜索所有匹配的键
    # keysWithPattern("t.a.") -> ["team", "that"]
    def keys_with_pattern(self, pattern):
        res = []
        self._keys_with_pattern_traverse(self.root, "", pattern, 0, res)
        return res

    # 遍历函数，尝试在「以 node 为根的 Trie 树中」匹配 pattern[i..]
    def _keys_with_pattern_traverse(self, root, path, pattern, idx, res):
        if root is None:
            return
        if idx == len(pattern):
            # 匹配完成
            if root.value is not None:
                res.append(path)

        char = pattern[idx]
        if char == ".":
            for c, nxt in root.children.items():
                path = path + c
                self._keys_with_pattern_traverse(nxt, path, pattern, idx + 1, res)
                path = path[:-1]
        else:
            path = path + char
            self._keys_with_pattern_traverse(root.children[char], path + char, pattern, idx + 1, res)
            path = path[:-1]

    # 通配符 . 匹配任意字符，判断是否存在匹配的键
    # hasKeyWithPattern(".ip") -> true
    # hasKeyWithPattern(".i") -> false
    def has_key_with_pattern(self, prefix):
        return self._has_key_with_pattern_traverse(self.root, prefix, 0)

    # 函数定义：从 node 节点开始匹配 pattern[i..]，返回是否成功匹配
    def _has_key_with_pattern_traverse(self, root, pattern, idx):
        if root is None:
            return False
        if idx == len(pattern):
            return root.value is not None
        char = pattern[idx]
        if char != ".":
            return self._has_key_with_pattern_traverse(self.root.children[char], pattern, idx + 1)

        for c, nxt in self.root.children.items():
            if self._has_key_with_pattern_traverse(nxt, pattern, idx + 1):
                return True

        return False

    # 返回 Map 中键值对的数量
    def size(self):
        return self.size


if __name__ == '__main__':
    trie = TrieMap()
    trie.put("app", 5)
    trie.put("team", 3)
    trie.put("that", 6)
    trie.put("them", 1)
    trie.put("zip", 2)
