def is_palindrome(word):
    word1 = ""
    for i in word:
        if i.isalnum():
            word1 += i
    drow = word1[::-1]
    return word1.lower() == drow.lower()


# print(is_palindrome("Hahah"))
# print(is_palindrome("string"))
# print(is_palindrome("k"))
# print(is_palindrome("oo"))


x = input("Give word:")
print(is_palindrome(x))
