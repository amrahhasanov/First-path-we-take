"""Task 1.
Create a dictionary and use it to store personal data (name, surname, age, pesel, telephone number).
Tip: only age is to be a number, other values are to be texts. Then give the form of commands:"""

dict1 = {"name": "Amrah",
         "surname": "Hasanov",
         "age": 22,
         "pesel": "1234567890",
         "telephone number": "122 211 121"}
#to determine the size of the dictionary,
print(len(dict1))
import sys
print(sys.getsizeof(dict1),"bytes")

#display all dictionary keys, each in a separate line,
for key, value in dict1.items():
    print(key)

#display all dictionary values, each in a separate line,
for key, value in dict1.items():
    print(dict1[key])

#all elements of the dictionary, each in a separate line with a key format: value,
for key, value in dict1.items():
    print(key, ":", dict1[key])

#to check if a key exists in the dictionary,
if str(input("s:")) in dict1:
    print("yes")
else:
    print("no")

#references to the value with the 'Last name' key ,
"""Could not understand the question"""
print(dict1["surname"])

"""or"""

try:
    print(dict1["Last name"])
except KeyError:
    print("did you mean surname? ")

"""or"""
"""dict1["Last name"] = dict1["surname"]
del dict1["surname"]
print(dict1.keys())
for key, value in dict1.items():
    print(key, ":", dict1[key])"""


#changes of values with the 'Phone number' key ,
dict1["telephone number"] = 999111999
print(dict1["telephone number"])

#insert a new dictionary element with the key 'Year of study' , the value is to be a number,

dict1["Year of study"] = 2022
print(dict1)

#remove the 'Year of Studies' key element.

dict1.pop("Year of study")
print(dict1)

"""Task 2.
What is the result of the methods: pop, popitem and clear for the dictionary from task 1. """

dict1.pop("pesel")
print(dict1)
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)

"""Task 3.
Create a dictionary in which the keys are uppercase letters of the Latin alphabet 
and all values will be equal to 100. 
Note: the dictionary should not be created using a loop or a letter-forming expression!"""
a = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N",
     "O", "P", "Q", "R", "S", "T", "V","X", "Y", "Z")
b = 100
dict2 = dict.fromkeys(a,b)
print(dict2)

"""Task 4.
Write the function counts_alphanumeric characters (text), 
which will return a dictionary in which the keys are the alphanumeric characters 
(' a' - ' z' , ' A' - ' Z' , ' 0' - ' 9' ) in the text and the values are the number of their occurrences.
The letters should not be case sensitive. 
If the argument is not a text, the function is to display an error message and return a None value."""

list1 = []
def counts_alphanumeric():
    for i in range(10):
        a = (input("Enter an alphanumeric character: ").lower())
        if a.isalnum() and len(a) == 1:
            list1.append(a)

        else:
            print("You can only one character at a time and it has to be an alphanumeric character...")
            return None


counts_alphanumeric()
dict1 = {i:list1.count(i) for i in list1}
print(dict1)

"""Task 5.
Write a program loading data from Test.txt file into the dictionary. 
Note: the keys in the file may be repeated, so the associated values should be lists.
"""
d = { line.split()[0] : line.split()[1] for line in open("Test.txt") }
print(d)
#?

"""Task 6.
Complete the program from task 5 so that the contents of the dictionary are saved in the Test1.txt file, 
with the keys and values sorted. Tip: use the sorted function."""
#?