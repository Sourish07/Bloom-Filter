from bloom_filter import BloomFilter

# Read in english words
with open("english.txt", encoding="utf-8") as f:
    english_words = f.read().split()

desired_fp_rate = 0.00001
# Create a bloom filter and insert the english words
bloom_filter = BloomFilter(len(english_words), desired_fp_rate)
for word in english_words:
    bloom_filter.insert(word)

# Read in the filtered french words (no word in this list will be in the english list)
with open("filtered_french.txt", encoding="utf-8") as f:
    french_words = f.read().split()

false_positives = []
for word in french_words:
    if bloom_filter.lookup(word) == "Maybe":
        false_positives.append(word)

# Analyzing the performance of our bloom filter
num_of_false_positives = len(false_positives)
n = len(english_words)
m = bloom_filter.size
k = bloom_filter.num_of_hash_functions
actual_fp = num_of_false_positives / len(french_words)
theoretical_fp = (1 - (1 - (1 / m)) ** (n * k)) ** k

print(f"Size of bit array in kilobytes: {m / 8 / 1024}")
print(f"Number of hash functions: {k}")
print(f"Number of false positives: {num_of_false_positives}")
# Slightly different from desired_fp_rate because we rounded up when calculating m and k
print(f"Theoretical false positive rate: {theoretical_fp}")
print(f"Proportion of false positives: {actual_fp}")