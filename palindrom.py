def is_palindrom(word):
    drow = word[::-1]
    return word == drow


print(is_palindrom("hahah"))
