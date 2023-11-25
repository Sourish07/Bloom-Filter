import bitarray
import math
import farmhash
import mmh3

class BloomFilter():
    def __init__(self, number_of_elements, false_positive_probability):
        n = number_of_elements
        p = false_positive_probability 

        self.size = math.ceil(-(n * math.log(p)) / (math.log(2) ** 2))
        self.bit_array = bitarray.bitarray(self.size)
        self.bit_array.setall(0)

        self.num_of_hash_functions = math.ceil((self.size / n) * math.log(2))

        # If we don't use a default parameter, then the lambda will capture the value 
        # of s at the time of execution, not at the time of definition

        # MurmurHash3
        self.hash_functions = [lambda x, seed=s: mmh3.hash(x, seed) for s in range(self.num_of_hash_functions)]
        
        # FarmHash
        # self.hash_functions = [lambda x, seed=s: farmhash.hash64withseed(x, seed) for s in range(self.num_of_hash_functions)]

    def insert(self, string):
        for hash_function in self.hash_functions:
            index = hash_function(string) % self.size
            self.bit_array[index] = 1

    def lookup(self, string):
        for hash_function in self.hash_functions:
            index = hash_function(string) % self.size
            if self.bit_array[index] == 0:
                return "No"
        return "Maybe"