class RandomizedSet:

    def __init__(self):
        self.nums_arr = []
        self.nums_map = {}


    def insert(self, val: int) -> bool:
        if val in self.nums_map:
            return False
        self.nums_arr.append(val)
        self.nums_map[val] = len(self.nums_arr) - 1
        return True


    def remove(self, val: int) -> bool:
        if val not in self.nums_map:
            return False
        # 删除移动到列表结尾
        idx = self.nums_map[val]
        last_idx = len(self.nums_arr) - 1
        last_val = self.nums_arr[last_idx]
        if idx != last_idx:
            self.nums_arr[idx], self.nums_arr[last_idx] = self.nums_arr[last_idx], self.nums_arr[idx]
        self.nums_map[last_val] = idx
        self.nums_arr.pop()
        del self.nums_map[val]
        return True


    def getRandom(self) -> int:
        idx = random.randint(0, len(self.nums_arr) - 1)
        return self.nums_arr[idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()