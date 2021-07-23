# Part A:
# A palindrome is a word that is spelt the same forward and backwards. Your task is to write a function that
# takes, as input, a single word and returns True if it is a palindrome and False otherwise.
def palindrome_check(word):
        if word == word[::-1]:
            result = word + " is a palindrome"
        else:
            result = word + " is not a palindrome"
        print(result)

# Part B:
# Using your function from Part A, write a program which reads words from a file. For each word, print
# "<word> is a palindrome" if the word is a palindrome, or "<word> is not a palindrome" if not. You
# can test you program on the file palindromic.txt
file = open(r"C:\Users\ACER\Dropbox\My PC (LAPTOP-ED4KFDF2)\Downloads\palindromic.txt")
for word in file:
    word = word.strip()
    palindrome_check(word)
file.close()