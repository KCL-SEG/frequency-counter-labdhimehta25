"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

#check file

def frequencies(items):
    frequencies = {}
    for i in items:
        #if item is not a string, convert it into one
        if type(i) == int:
            i = str(i)

        if i in frequencies:#increment if already dictionary
            frequencies[i] = frequencies.get(i) + 1
        else:#if not in dictionary then create it with the starting value of 1
            frequencies[str(i)]=1



    return frequencies
