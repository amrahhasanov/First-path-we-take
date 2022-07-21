#Python 3
"""Task 1.
Write a program that opens the Data1.txt file and displays its contents. """

f = open("Data1.txt")
print(f.read())
f.close()

"""Task 2.
Write a program that opens the data1.txt file and reads it line by line. """

f = open("Data1.txt")
# print(f.readlines()) or
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())


"""Task 3.
Write a program that reads the data2.txt text file of the specified format: 1; 2; 3; 4; 5
and writing the numbers in the list ([1,2,3,4,5]). 
"""

f = open("data2.txt","rt")
print(f.read())
list_1 = []
with open('data2.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        list_1.append(inner_list)
print(list_1)
f.close()



"""Task 4.
Write a program that saves any sequence of characters in the Result4.txt file. """
f = open("Result4.txt", "a")
ag = {" a"," b", " c" , " d", " e"}
f.writelines(ag)
f.close()

f = open("Result4.txt", "r")
print(f.read())

"""Task 5.
Write a program that saves any list (texts, numbers) in the Result5.txt file, 
so that each element is on a separate line.
"""
f = open("Result5.txt", "a")
ag = {" a\n"," b\n", " c\n" , " d\n", " e\n"}
f.writelines(ag)
f.close()

f = open("Result5.txt", "r")
print(f.read())

"""Task 6.
Write a program to read the data3.txt text file in the specified format: 
5; 2
3; 5
2; 10
and rewrite these numbers to the Result6.txt file, add the power of two numbers 
5; 2; 25
3; 5; 243
2; 10; 1024
"""
f = open("Result6.txt","rt")
print(f.read())
f.close()
f = open("Result6.txt","w")
ad = (5 ** 2 , 3 ** 5 , 2 ** 10 )
f.write(str(ad))
f.close()

"""Task 7.
Write the search program in the file Data1.txt text number of:
spaces,
a set sequence of characters,

the characters go to the next line.
"""
#couldn't understand the question
