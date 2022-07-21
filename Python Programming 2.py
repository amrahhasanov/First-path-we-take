#Python 2
"""Task 1.
Write a program that displays any subtitle 10 times. """
import re



print(" Hello World " * 10)
"""Task 2.
Write a program that displays numbers from 0 to 1000 with step 50 using one loop for """
for i in range(0, 1000, 50):
    print(i)
"""Task 3.
Write a program that takes a number from the user and checks if it is greater than 5. 
The program should display an appropriate message.
"""
try:
    x = float(input("Please enter a number:"))
    if x > 5:
        print(x, "is greater than 5")
    else :
        print(x , "is not greater than 5")
except ValueError:
    print("Please enter only numerical values")
"""Task 4.
Write a program displaying the name of the day of the week depending on the number entered by the user 
(1 - Monday ,..., 7 - Sunday, another - "there is no such day").
"""
try:
    dict_1 = {1 : "Monday", 2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday", 6:"Saturday", 7:"Sunday"}
    input_1 = int(input("enter a number from 1 to 7:"))
    if 0 < input_1 < 8 :
        print(dict_1[input_1])
    else:
        print("there is no such day")
except ValueError:
    print("You can enter only discrete numerical values!")

"""Task 5.
Write a program that takes the number n from the user and displays the value of the sum 1 + 2 + 3 +
… + n.
"""
n = int(input("n:"))
sum_1 = sum(range(1, n+1))
print(sum_1)

"""Task 6.
Write a program that takes numbers from you. If the number 4 is given, the program is to terminate its operation.
"""
def numberchecker():
    number = float(input("please enter a number, except 4:"))
    if number == 4:
        pass
        #quit()
        #or
        #raise SystemExit
    else :
        print("good")

numberchecker()

"""Task 7.
Write a program that takes numbers from the user until 0 is given. After reading 0, 
display the sum of the numbers given by the user.
"""

list_2 = []
while True:
    number_input = float(input("type 0 to find the sum of all your inputs:"))
    if number_input == 0:
        break
    list_2.append(number_input)
print(sum(list_2))


"""Task 8.
Write a program that will download the subtitle and the sign from the user
and check if the sign is in the subtitle. If yes, display the occurrence indexes,
if no, the corresponding message.
"""

try :
    subtitle = str(input("subtitle:"))
    sign = str(input("sign:"))
    j = subtitle.index(sign)
    print(j)
except ValueError:
    print("there is no {} in {} ".format(sign, subtitle))