class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.storage = [None for x in range(self.capacity)]
        # self.storage = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        """
        return len(storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """FNV-1 Hash, 64-bit"""
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashing = FNV_offset_basis
        for byte in key.encode():
            hashing = hashing * FNV_prime
            hashing = hashing ^ byte
        return hashing


    def djb2(self, key):
        """DJB2 hash, 32-bit"""
        hashing = 5381

        key_bytes = key.encode()

        for byte in key_bytes:
            hashing = ((hashing << 5) + hashing) + byte

        return hashing




    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        """
        hashed_key = self.hash_index(key)
        node = self.storage[hashed_key]
        # self.storage[hashed_key] = HashTableEntry(key, value)
        if node is None:
            self.storage[hashed_key] = HashTableEntry(key, value)
            return self.storage[hashed_key]
        while node is not None:
            if node.key == key:
                self.storage[hashed_key] = HashTableEntry(key, value)
            elif node.next == None:
                node.next = HashTableEntry(key, value)
                break
            node = node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        """
        hashed_key = self.hash_index(key)
        node = self.storage[hashed_key]
        if node is None:
            print("There's nothing there!")
        elif node.key == key and node.next == None:
            self.storage[hashed_key] = None
            node = None

        while node is not None and node.next is not None:
            print("hello " + node.value)
            if node.next.key == key:
                node.next = node.next.next
            node = node.next


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        """

        hashed_key = self.hash_index(key)
        node = self.storage[hashed_key]
        # return node.value

        while node is not None:
            if node.key == key:
                # print(node.value)
                return node.value
            node = node.next
        
        return node

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)
    # print(ht.fnv1("hello"))
    # print(ht.djb2("hello"))
    # print(ht.hash_index("hello"))
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # print("")
