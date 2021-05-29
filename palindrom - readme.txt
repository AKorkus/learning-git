Short documentation:

Palindrome is a word, that written backwards reads the same.
Checked by the function is_palindrome(word).

To use program, you need to install IDLE (python compiler) and run palindrome.py with it.

How the function works?
It takes a string as an argument. --"WORD"
Removes characters that are not alphanumerical: abc, 123! --> abc123
Creates a variable by reversing string. --"DROW"
Changes all capital letters to lower letters with lower method.
Returns if "WORD" is the same as "DROW".

For example:
>>> is_palindrome(Kobyła ma mały bok!)
True
>>> is_palindrome(Kobyła nie ma dużego boku!)
False


Of course all single characters (like "a") are palindromes.
Function treats digits as characters and numbers as strings, so 101 is a palindrome.
Empty string is a palindrome.