# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        pair = self.storage[idx]

        # if there's a linked list insert at the end
        if pair == None:
            self.storage[idx] = LinkedPair(key, value)
        else:
            while pair.next != None:
                pair = pair.next
            pair.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        pair = self.storage[idx]

        if self.retrieve(key) == None:
            print("WARNING: key not found")
        
        # need to find the pair to be removed
        # and remove it, potentially from a singly linked list

        prev = None
        curr = pair

        while curr != None:
            if curr.key == key:
                if prev != None: #
                    prev.next = curr.next
                    break
                else:
                    self.storage[idx] = curr.next
                    break
            
            prev = curr
            curr = curr.next
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)
        pair = self.storage[idx]

        if pair == None:
            return None

        # go to index, search through linked list for key
        if pair.key == key:
            return pair.value
        while pair.next != None:
            if pair.next.key == key:
                return pair.next.value
        return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # increase capacity
        self.capacity *= 2

        # copy storage to a temp list, overwrite it
        temp = self.storage
        self.storage = [None] * self.capacity

        # rehash key/value pairs
        for i in temp:
            while i != None:
                self.insert(i.key, i.value)
                i = i.next



if __name__ == "__main__":
    ht = HashTable(2)
    
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
