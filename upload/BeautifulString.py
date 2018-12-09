"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;
For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;
For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.
"""
def isBeautifulString(inputString):
    abc = [0]*26
    for c in inputString:
        abc[ord(c) - 97] += 1  

    # turn letters into numbers
    for i in range(len(abc)-1):
        if abc[i+1]>abc[i]:
            return False
    return True
