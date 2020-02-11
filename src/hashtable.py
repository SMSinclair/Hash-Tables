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
        curr = self.storage[idx]
        prev = None
        new = LinkedPair(key, value)

        # if bucket is empty, put the pair into it
        if curr == None:
            self.storage[idx] = new
        
        else:
            while curr != None:
                #overwrite if key is  in LL
                if curr.key == key:
                    # if not head
                    if prev != None:
                        prev.next = new
                        new.next = curr.next
                        break
                    
                    # if it is the head
                    else:
                        self.storage[idx] = new
                        new.next = curr.next
                        break
                
                # add to end of LL if key not present
                elif curr.next == None:
                    curr.next = new
                    break

                # traverse another step
                prev = curr
                curr = curr.next


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
                if prev != None: 
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
        curr = self.storage[idx]

        # return None if bucket empty
        if curr == None:
            return None

        # if first element matches key, return value
        if curr.key == key:
            return curr.value
        # otherwise traverse the LL and return value with matching key
        while curr.next != None:
            if curr.next.key == key:
                return curr.next.value 
            curr = curr.next    


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
            # traverse the LL and insert into new hash table
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
