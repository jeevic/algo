class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        cur = self.root
        for s in word:
            fn = cur.children.get(s, None)
            if fn is None:
                fn = Node(s)
            else:
                fn.incr_count()
            cur.children[s] = fn
            cur = fn

        return

    def countWordsEqualTo(self, word: str) -> int:
        cur = self.root
        for s in word:
            fn = cur.children.get(s, None)
            if fn is None:
                return 0
            else:
                cur = fn
        return cur.count

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root
        for s in prefix:
            fn = cur.children.get(s, None)
            if fn is None:
                return 0
            else:
                cur = fn
        return cur.count

    def erase(self, word: str) -> None:
        cur = self.root
        for s in word:
            fn = cur.children.get(s, None)
            if fn is None:
                self.print(word)
                return None
            else:
                count = fn.decr_count()
                cur.children[s] = fn
                if count == 0:
                    del cur.children[s]
            cur = fn
        return None

    def print(self, word):
        cur = self.root
        for s in word:
            fn = cur.children.get(s, None)
            if fn is None:
                return
            else:
                cur = fn


class Node:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.children = {}

    def incr_count(self):
        self.count += 1
        return self.count

    def decr_count(self):
        self.count -= 1
        return self.count
