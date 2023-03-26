
class LFUCache:
    """
    @see  https://mp.weixin.qq.com/s/oXv03m1J8TwtHwMJEZ1ApQ
    """
    kv_map = {}
    kc_map = {}
    freq_keys_map = {}
    min_freq = 0
    size = 0

    def __init__(self, capacity: int):
        self.kv_map = {}
        self.kc_map = {}
        self.freq_keys_map = {}
        self.min_freq = 0
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if self.kv_map.get(key, None) is None:
            return -1
        self.incr_freq(key)
        return self.kv_map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return -1
        if self.kv_map.get(key, None) is not None:
            self.kv_map[key] = value
            self.incr_freq(key)
            return

        if self.size >= self.capacity:
            self.remove_least_freq_key()

        self.kv_map[key] = value
        self.kc_map[key] = 1
        self.min_freq = 1
        freq_keys = self.freq_keys_map.get(self.min_freq, [])
        freq_keys.append(key)
        self.freq_keys_map[self.min_freq] = freq_keys
        self.size += 1
        self.min_freq = 1
        return

    def remove_least_freq_key(self):
        lfreq = self.min_freq
        keys = self.freq_keys_map[lfreq]
        # 删除最左侧
        key = keys.pop(0)
        self.freq_keys_map[lfreq] = keys

        if len(keys) == 0:
            del self.freq_keys_map[lfreq]

        del self.kc_map[key]
        del self.kv_map[key]
        self.size -= 1
        return

    def incr_freq(self, key):
        freq = self.kc_map[key]
        self.kc_map[key] += 1
        freq_keys = self.freq_keys_map[freq]

        freq_keys.remove(key)
        self.freq_keys_map[freq] = freq_keys

        if len(freq_keys) == 0:
            del self.freq_keys_map[freq]
            if self.min_freq == freq:
                self.min_freq = freq + 1

        new_freq_keys = self.freq_keys_map.get(freq + 1, [])
        new_freq_keys.append(key)
        self.freq_keys_map[freq + 1] = new_freq_keys
        return

    # Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
