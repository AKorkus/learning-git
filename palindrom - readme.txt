Short documentation:

Palindrome is a word, that written backwards reads the same.
Checked by the function is_palindrome(word).

How the function works?
It takes a string as an argument. --"WORD"
Creates a variable by reversing string. --"DROW"
Changes all capital letters to lower letters with lower method.
Returns if "WORD" is the same as "DROW".

For example:

is_palindrome(Hahah)
WORD = Hahah
DROW = hahaH
hahah = hahah?
True

is_palindrome(string)
WORD = string
DROW = gnirts
string = gnirts?
False

Of course all single characters (like "a") are palindromes.
Function treats digits as characters and numbers as strings, so 101 is a palindrome.
Empty string is a palindrome.