name = "sourish"

# hash #1
import mmh3
# print(mmh3.hash(name, 42))


# hash #2
import cityhash
# print(cityhash.CityHash64(name))

# hash #3
import farmhash
# print(farmhash.hash32(name))
# print(farmhash.hash64(name))
# print(farmhash.hash128(name))
# print(farmhash.fingerprint128(name))

HASH_FUNCTIONS2 = [
    lambda x: mmh3.hash(x, 9),
    lambda x: mmh3.hash(x, 7),
    lambda x: mmh3.hash(x, 2001),
    lambda x: farmhash.hash32withseed(x, 7),
    farmhash.hash32,
    farmhash.hash64,
    lambda x: int("".join(str(x) for x in farmhash.hash128(x))),
]

for h in HASH_FUNCTIONS2:
    print(h(name))

first_7_primes = [2, 3, 5, 7, 11, 13, 17]

HASH_FUNCTIONS3 = [
    lambda x: mmh3.hash(x, 2),
    lambda x: mmh3.hash(x, 3),
    lambda x: mmh3.hash(x, 5),
    lambda x: mmh3.hash(x, 7),
    lambda x: mmh3.hash(x, 11),
    lambda x: mmh3.hash(x, 13),
    lambda x: mmh3.hash(x, 17),
]

HASH_FUNCTIONS = [lambda x: farmhash.hash64withseed(x, p) for p in range(7)]
