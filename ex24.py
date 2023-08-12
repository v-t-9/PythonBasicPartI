# Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(letter):
    le = letter.lower()
    if le in "aeiou":
        return f"The letter {letter} is a vowel"
    return f"The letter {letter} is not a vowel"

if __name__ == "__main__":
    letter1 = "a"
    letter2 = "B"
    letter3 = "E"
    letter4 = "z"
    print(is_vowel(letter1))
    print(is_vowel(letter2))
    print(is_vowel(letter3))
    print(is_vowel(letter4))
