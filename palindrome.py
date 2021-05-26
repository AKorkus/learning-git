def is_palindrome(word):
    drow = word[::-1]
    return word.lower() == drow.lower()


# print(is_palindrome("Hahah"))
# print(is_palindrome("string"))
# print(is_palindrome("k"))
# print(is_palindrome("oo"))


x = input("Give word:")
print(is_palindrome(x))
