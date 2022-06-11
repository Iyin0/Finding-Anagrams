# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here

    if len(word) == len(anagram):       # to check if both inputs have the same number of strings
        for i in anagram:               # to check if the characters in the anagram are exactly in the word
            if i in word:
                check = True
            else:
                check = False
                break
        for j in word:                  # to check if the characters in the word are exactly in the anagram
            if j in anagram:
                check = True
            else:
                check = False
                break
    else:
        check = False

    return check


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
print(find_anagram("listen", "silent"))
print(find_anagram("listens", "silent"))
