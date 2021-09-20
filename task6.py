# 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.
str = input('Enter a string: ')
arr = [ch for ch in str if ch.isupper()]
print(arr)

# 3. Write a program to construct a dictionary from the two lists containing the names of students
# and their corresponding subjects.
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
dictionary = dict(zip(students, subjects))
print(dictionary)

# 4. Write a program in Python using generators to reverse the string.
def reverse_string(str):
    length = len(str)
    for i in range(length - 1, -1, -1):
        yield str[i]
reverse_list = list(reverse_string("Consultadd Training"))
print(''.join(reverse_list))

# 5. Write an example on decorators.
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def print_hello():
    return 'hello there'

decorate = uppercase_decorator(print_hello)
decorate()