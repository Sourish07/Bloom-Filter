import json

# used to format the txt files

with open("english.txt", encoding="utf-8") as f:
    english_words = set(f.read().split())
    

with open("french.txt", encoding="utf-8") as f:
    french_words = f.read().split()
    for french_word in french_words:
        if french_word in english_words:
            print(french_word)

    filtered_french_words = [w for w in french_words if w not in english_words]

    with open("filtered_french.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(filtered_french_words))


# with open("words_alpha.txt") as f:
#     valid_words = set(f.read().split())

# print(f"read in {len(valid_words)} words")

# with open("harry_potter_1.txt") as f:
#     hp_words = f.read().split()
#     hp_words = [word.lower() for word in hp_words]
#     # remove non-alphabetic characters
#     hp_words = ["".join(char for char in word if char.isalpha()) for word in hp_words]
#     hp_words = set(hp_words)

# print(f"read in {len(hp_words)} words from Harry Potter")

# not_present_words = hp_words - valid_words

# print(f"{len(not_present_words)} words from Harry Potter are not in the dictionary")
# [print(word) for word in sorted(not_present_words)]
