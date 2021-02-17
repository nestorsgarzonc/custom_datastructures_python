class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size=1000000
        self.table=[None]*self.size

    def calculate_hash_value(self, key):
        return key%self.size
    
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hv=self.calculate_hash_value(key)
        self.table[hv]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hv=self.calculate_hash_value(key)
        if self.table[hv]!=None:
            return self.table[hv]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hv=self.calculate_hash_value(key)
        if self.table[hv]!=None:
            self.table[hv]=None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
