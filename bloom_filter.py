import bitarray
from hash_functions import HASH_FUNCTIONS

class BloomFilter():
    def __init__(self, size=3_546_472, num_of_hash_functions=7):
        self.size = size
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)

        self.num_of_hash_functions = min(num_of_hash_functions, len(HASH_FUNCTIONS))

    def insert(self, string):
        for hash_function in HASH_FUNCTIONS[:self.num_of_hash_functions]:
            index = hash_function(string) % self.size
            self.bit_array[index] = 1

    def lookup(self, string):
        for hash_function in HASH_FUNCTIONS[:self.num_of_hash_functions]:
            index = hash_function(string) % self.size
            if self.bit_array[index] == 0:
                return "Nope"
        return "Maybe"