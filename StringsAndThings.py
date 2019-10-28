# Strings are data that falls within " " marks.

# Concatenation: Put two or more strings together.

firstName = "Fred"
lastName = "Flintstone"

fullName = firstName + " " + lastName

print(fullName)

# Repetition
# Repetition operator: *

print("Hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream")
    print("Merrily, "*4)
    print("Life is but a dream")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
#   slicing operator:  :
#   slicing lets us make substrings

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)+1):
    print(name[0:i])

# Searching inside of strings

print("biv" in name)
print("v" not in name)

if "y" in name:
    print("The letter y is in name")
else:
    print("The letter y in not in name")

 # String Methods to investigate:
    # Method        Use Example         Explanation
    # center        aStr.center(w)      It returns a string padded with the fillchar (a padding character) and it doesn't change the original string.
    str = "this is string example...cool!"
    print("str.center(40, 'a') : ", str.center(40, 'a'))
    # ljust         aStr.ljust(w)       The function left aligns the string according to the width and fills the leftover space of line with blank space.
    str = "this is string example...cool!";
    print(str.ljust(50, '0'))
    # rjust         aStr.rjust(w)       This string method gives back a new string of a certain length after substituting a given character in left side of the first string.
    str = "this is string example...cool!";
    print(str.rjust(50, '0'))
    # upper         aStr.upper()        It changes all the lowercase letters to uppercase letters.
    str = "this is string example...cool!";
    print("str.capitalize() : ", str.upper())
    # lower         aStr.lower()        It changes all the uppercase letters to lowercase letters.
    aList = [123, 'xyz', 'zara', 'abc'];
    print("Index for xyz : ", aList.index('xyz'))
    print("Index for zara : ", aList.index('zara'))
    # index         aStr.index(item)    It looks for original elements from the beginning of the list and brings the lowest index back to there.
    str1 = "this is string example....wow!!!";
    str2 = "is";
    # rindex        aStr.rindex(item)   It brings back the highest index of the substring inside of the string.
    print(str1.rindex(str2))
    print(str1.index(str2))
    # find          aStr.find(item)     The string method returns an integer value.
    str1 = "this is string example....wow!!!";
    str2 = "exam";
    # rfind         aStr.rfind(item)    It brings back the highest index of the substring.
    print(str1.find(str2))
    print(str1.find(str2, 10))
    print(str1.find(str2, 40))
    # replace       aStr.replace(old, new)      It brings back the copy of an old string and replaces it with a new substring.
    str = ("I just wanted to say hi")
    print(str.replace("hi", "bye"))

# Be sure to include multiple examples of all of them in use

# Character Functions

print(ord('5'))

print(chr(97+13))

print(str(12548))

# testing functions from mapper.py

from Mapper import *

print(letterToIndex('P'))
print(indexToLetter(10))