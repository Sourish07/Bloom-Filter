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

        # self.hash_functions = [lambda x: farmhash.hash64withseed(x, seed) for seed in range(self.num_of_hash_functions)]
        self.hash_functions = [lambda x: mmh3.hash(x, seed) for seed in range(self.num_of_hash_functions)]

    def insert(self, string):
        for hash_function in self.hash_functions:
            index = hash_function(string) % self.size
            self.bit_array[index] = 1

    def lookup(self, string):
        for hash_function in self.hash_functions:
            index = hash_function(string) % self.size
            if self.bit_array[index] == 0:
                return "Nope"
        return "Maybe"