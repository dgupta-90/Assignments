from functools import reduce

# 1. Write a program to reverse a string.
str = input('Enter string: ')
print(str[::-1])

# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.
str = input('Enter string: ')
up = 0
low = 0
for i in str:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1
print(f'Upper case characters: {up}, Lower case characters: {low}')

# 3. Create a function that takes a list and returns a new list with unique elements of the first list.
def remove_duplicates(lst):
    arr = []
    for i in lst:
        if i not in arr:
            arr.append(i)
    return arr

lst = list(input('Enter elements by comma:').split(','))
print(remove_duplicates(lst))

# 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
words = input('Enter sequence of words separated by hyphen: ').split('-')
words.sort()
print('-'.join(words))

# 5. Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.
sentence = input("Enter a sentence: ")
print(sentence.upper())

# 6. Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
def addition(a, b):
    print(int(a) + int(b))

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
addition(num1, num2)

# 7. Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.
def longest_string(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s1) == len(s2):
        print(s1)
        print(s2)
    else:
        print(s2)

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
longest_string(str1, str2)

# 8. Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).
def square_of_numbers():
    x = []
    for i in range(1,21):
        x.append(i**2)
    print(tuple(x))

square_of_numbers()

# 9. Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.
def showNumbers(limit):
    for i in range(0, limit+1):
        if i % 2 == 0:
            print(f'{i}: EVEN ')
        else:
            print(f'{i}: ODD ')

l = input('Enter limit: ')
showNumbers(l)

# 10. Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
print(list(filter(lambda x: x % 2 == 0, range(1, 21))))

# 11. Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
# Hints: Use filter() to filter even elements of the given listUse map() to generate a list of squares of the
# numbers in the filtered list. Use lambda() to define anonymous functions.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, arr)))
print(new_list)

# 12. Write a function to compute 5/0 and use try/except to catch the exceptions
def divide():
    return 5/0

try:
    divide()
except Exception as ex:
    print("Exception occurred: ", ex)

# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
arr = [1, 2, 3, 4, 5, 6, 7]
print(reduce(lambda x, y: str(x) + str(y), arr))

# 14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
values = input("Enter a list of numbers separated by comma: ").split(',')
arr = list(values)
print(list(filter(lambda x: eval(x) % 3 != 0 and eval(x) % 7 == 0, arr)))

# 15. Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.
def multiply(l):
    return l*l

values = eval(input("Enter the list of numbers separated by comma: "))
arr = list(values)
result = map(multiply, arr)
print(list(result))

# 16. What is the output of the following codes:
# (i) 2
# (ii) after f after f?
#      name ‘f’ is not found