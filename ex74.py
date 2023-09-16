# Write a Python program to hash a word.

def hash_word(w):
    return f"The hash is: {hash(w)}."

if __name__ == "__main__":
    word = input("Enter a word: ")
    print(hash_word(word))