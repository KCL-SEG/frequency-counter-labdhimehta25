"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

#check file

def frequencies(items):
    frequencies = {}
    for i in items:
        value = items[i]
        #if item is not a string, convert it into one
        if type(i) == int:
            i = str(i)

        if i in frequencies:#increment if already dictionary
            value = value + 1
        else:#if not in dictionary then create it with the starting value of 1
            frequencies[str(i)]=1



    return frequencies
