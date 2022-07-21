"""Task 1.
Write a program in which the text display function will be defined and used.
"""
print("Task 1")
def text_displayer():
    print("text asdfgh")
text_displayer()

"""Task 2.
Modify the function in Job 1 so that the subtitle is given in the argument. 
"""
print("Task 2")
def text_displyer_1(sub):
    print(sub)


s = "text hgfdsa"
text_displyer_1(s)

"""Task 3.
Write a function that calculates and returns the result of a + b, 
where a and b are arguments of the function. 
"""
print("Task 3")
def sum_finder(a, b):
    c = a + b
    return c
a1 = 5
b1 = 10
print(sum_finder(a1,b1))

"""Task 4.
Write a program that takes two numbers from the user 
and displays the result returned by the function from task 3.
"""
print("Task 4")
a2 = float(input("number1:"))
b2 = float(input("number2:"))
print("Sum of number1 and number2 is equal to: ",sum_finder(a2,b2))

"""Task 5.
Load the random package, use the import command. 
Then use the random function of this package to display numbers in the range:
a) [0.0 ; 1.0)
b)    [1; 10)
c)     [5; 15]
In subsections b and c these number have to  be integers. 
"""
print("Task 5")
def rand_func(x,y):
    import random
    list_1 = []
    for i in range(10):
        n = random.uniform(x, y)
        list_1.append(n)

    print(list_1)

x1 = 0.0
y1 = 1.0
rand_func(x1, y1)

def rand_func2(x, y):
    import random
    list_2 = []
    for i in range(10):
        n = random.randint(x, y)
        list_2.append(n)

    print(list_2)

x2 = 1
y2 = 10
rand_func2(x2, y2)
x3 = 5
y3 = 15
rand_func2(x3 , y3)

"""Task 6.
Write a program that draws 6 numbers and saves them in the list. 
"""
print("Task 6")
def draw_1():
    list_82 = []
    for i in range(6):
        list_82.append(input('Enter the a number: '))

    print(list_82)
draw_1()

"""Task 7.
Write a program that draws one integer from the range [0; 100] and retrieves the other from the user. 
The program is to display a message: "the number drawn is less/more/equivalent".
"""
print("Task 7")
import random
def draw_2():
    list_28 = []
    num_1 = int(input("enter a number: "))
    num_2 = random.randint(0, 100)
    if num_1 < num_2:
        print("the number drawn is less")
    elif num_1 > num_2:
        print("the number drawn is more")
    elif num_1 == num_2:
        print("the numbers are equal")
    print("the random number was: ",num_2)
a = int(input("how many times do you want to try? "))
for _ in range(a):
    draw_2()




"""Task 8*.
Write a program imitating a totolotek game.
The player gives 6 numbers from the 49th pot,
then 6 numbers are drawn and the number of hits is displayed."""

'''assuming the player should choose 6 numbers from 1 to 49'''
#1 he will input 6 numbers from 1-49
#2 the numbers will be saved into a list
#3 the random module will choose 6 numbers from 1-49
#4 they will be saved into another list
#5 they will be compared
#6 the matched elements will be saved into another list
#7 the len() of the list will be printed
#8 it will be checked whether the player won or not
print("Task 8")
list_user = []
def draw_1():

    for i in range(6):
        aa = int(input('Enter the a number: '))
        if 1 <= aa <= 49:
            list_user.append(aa)
        else :
            aa = int(input('This one was not on range of 49, Enter another instead:'))
            if 1 <= aa <= 49:
                list_user.append(aa)
            else:
                print("Now you decreased our chance of winning")


    print("Your numbers: ",list_user)
draw_1()

import random
list_computer = []
def draw_2():
    num_2 = random.randint(0, 49)
    list_computer.append(num_2)
for _ in range(6):
    draw_2()
print("Drawn numbers: ", list_computer)



common_list = []
for element in list_user:
    if element in list_computer:
        common_list.append(element)

if len(common_list) == 0:
    print("There is no match")
    print("Unfortunately you did not won anything")

elif len(common_list) >= 3:
    print("Congratulations you won the Jackpot.....")
else:
    print("These are the common elemens: ", common_list)
    print("Number of common elements: ", len(common_list))
    print("Unfortunately you did not won anything")