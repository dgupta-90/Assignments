import sys

# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum = num1 + num2
    print(sum)
except:
    print("Error Found !!")

# 2. Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure to
# use read only mode.
try:
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except:
    print("Error opening file. Please enter the name of the file again.")

# 3. Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
try:
    num = input('Enter a number: ')
    if len(num) <= 4 and num.isdigit():
        pass
    else:
        raise Exception
except:
    print('The length is too short/long !!! Please provide only four digits')

# 4. Create a login page backend to ask users to enter the username and password. Make sure to ask
# for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.
username = input("User name: ")
password1 = input("Password: ")
password2 = input("Re-enter your password: ")
count = 0
while count < 3:
    count += 1
    if password1 == password2:
        print("Account created successfully!")
        break
    else:
        print("Incorrect Password.")
        password2 = input("Re-enter your password: ")
    print("Access Denied")

# 5. Read doc.txt file using Python File handling concept and return only the even length string
# from the file. Consider the content of doc.txt as given below:
# Hello I am a file
# Where you need to return the data string
# Which is of even length
# Make sure you return the content in The same link as it is present.
file = open('doc.txt', 'r')
for line in file:
    for word in line.split(" "):
        if len(word) % 2 == 0:
            print(word)
file.close()