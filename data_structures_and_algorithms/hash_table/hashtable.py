from data_structures_and_algorithms.hash_table.linked_list import Node ,Linked_list
class Hashtable():
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None]*size

    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        hash_num = (sum * 39) % self.size
        return hash_num

    def add(self, key, value):
        index = self._hash(key)
        if not self._buckets[index]:
            self._buckets[index] = Linked_list()
        self._buckets[index].append([key, value])
        return [key, value]

    def get(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]

        if not bucket:
            return None
        else:
            current = bucket.head

            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contains(self, key):
        index = self._hash(key)
        bucket = self._buckets[index]
        if not bucket:
            return False
        else:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next

if __name__ == "__main__":
    hashmap = Hashtable()
    print(hashmap.add("hi", "there"))
    print(hashmap.add("how you", "doing"))
    print(hashmap.add("whats up", "doing okay"))
    print(hashmap.get('suhaib'))
    print(hashmap.contains('whats your name'))
    print(hashmap.contains('asac '))
   
