"""Task 1.
Write a program that displays text"""
print("Hello World :)")
"""Task 2.
Write a program that takes the user's name and displays the text
"""
given_name = str(input("Please enter your name:"))
print("Hello", given_name)
"""Task 3*.
Use the format method to display the subtitle from task """
subtitle_g = ("This is {}")
print(subtitle_g.format("Task3"))
"""2. Task 4.
Create a variable   zmienna= "	This is tekst	 " (with	 spaces!) and interpret the results of the following commands:
"""
#a) len(zmienna),
zmienna= "	This is tekst12345	 "
print(len(zmienna))
#b) zienna.upper(),
print(zmienna.upper())
#c) zmienna.lower(),
print(zmienna.lower())
#d) zmienna = zmienna.strip(),
print(zmienna.strip())
#e) zmienna.split("ciąg_znaków"),
print(zmienna.split())
#f) zmienna.startswith("ciąg_znaków"),
print(zmienna.startswith("i"))
#g) zmienna.endswith("ciąg_znaków"),
print(zmienna.endswith(""))
#h) zmienna.count("ciąg_znaków"),
print(zmienna.count("t"))
#i)  zmienna.index("ciąg_znaków"),
print(zmienna.index("e"))
#j) zmienna[n],
print(zmienna[10])
#k) zmienna[n:m],
print(zmienna[9:14])
#l) "ciąg_znaków" in zmienna,
print("12345" in zmienna)
print("asdfgh" in zmienna)
#m) zmienna.replace("ciag_znaków1", "ciąg_znaków2"),
print(zmienna.replace("12345", "54321"))
#n) zmienna + 2,
"""print(zmienna + 2)"""
#o)  zmienna + str(2),
print(zmienna + str(2))
#p) zmienna * 2.
print(zmienna * 2)
"""Task 5.
Write a program to initialize the list of texts and (variable lista):
display its second element,
check the operation of the commands:
"character string".join(lista),
list.append("character string"),
list.remove("character string"). """
lista = ["apple", "orange", "banana"]
print(lista[1])
print(" & ".join(lista))
lista.append("strawberry")
print(lista)
lista.remove("banana")
print(lista)
"""Task 6.
Create the variables:
napis = "abcd" 
liczba1 = 2 
liczba2 = 2.3 
check the result of the type(variable) function,
check the result of the type(str(variable)) function."""

napis = "abcd"
liczba1 = 2
liczba2 = 2.3
print(type(napis))
print(type(liczba1))
print(type(liczba2))
print(str(type(napis)))
print(str(type(liczba1)))
print(str(type(liczba2)))
