## Even or Oddd by using function

# def evenOdd(x: int)->str:
#     if (x%2 == 0):
#         return "Even"
#     else:
#         return "Odd"
    
# print(evenOdd(10))
# print(evenOdd(27))

## Default arguments

# def default(x, y = 27):
#     print("x: ", x)
#     print("y: ", y)

# default(10)

## Keyword arguments

# def student(fname, lname):
#     print(fname, lname)

# student(fname = "Mayur", lname = "Jadhav")
# student(fname = "Suraj", lname = "Lohar")

## Positional arguments

# def nameAge(name, age):
#     print("Hi! My name is ", name)
#     print("And my age is ", age)
#     print("\n", end="")

# nameAge("Mayur", 21)
# nameAge("Suraj", 22)

## Arbitatory keyword fun

# def fun(*argv):
#     for arg in argv:
#         print(arg)

# fun("Mayur", "is", "Very", "prideful", "Person", "Don't", "hurt him", "Okay!")

# 
## Arbitatory keyword fun
# def fun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s: %s" % (key, value))

# fun(name='Mayur', age=21, my_class='FY BTech')

## Docstring fun
# def evenOdd(x):
#     if (x%2 == 0):
#         return "Even"
#     else:
#         return "Odd"
    
# print(evenOdd.__doc__)

## Nested function

# def nested():
#     s = "Hi! there"

#     def f2():
#         print(s)
#     f2()
# nested()

## Annonymous fun with lambda

# def cube(x):
#     return x*x*x

# cube_x = lambda x: x*x*x

# print(cube(7))
# print(cube_x(7))

## Pass by Reference and Pass by Value

# def lst(x):
#     x[0] = 27

# list = [2, 34, 56 , 67, 67]

# lst(list)
# print(list)

# def lst(x):
#     x = [23, 45, 56, 567, 67]

# list = [12, 34,56, 67, 67, 55j]
# lst(list)
# print(list)

## Swapping

# def swap(x, y):
#     temp = x
#     x = y
#     y = temp
    
# x = 10
# y = 27

# swap(x, y)
# print(x)
# print(y)

# 
# def swap(x, y):
#     return y, x

# a = 2
# b = 3

# print(swap(a, b))

# 
# def swap(values):
#     values[0], values[1] = values[1], values[0]

# list = [2, 4]
# swap(list)

# print(list[0])
# print(list[1])

## Recursion

# def factorial(n):
#     if (n == 0):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(7))
# print(type(type(int)))

# name = str(input("Enter your name: "))
# print("Hello, " + name + "!")
# print(f"Hello, {name}!")
# print("Hello, {}!".format(name))
# print("Hello, %s!" % name)
# print("Hello, {0}!".format(name))
# print("Hello", name)

## Self as default argument

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def show(self):
#         print(f"Brand: {self.brand}\nModel: {self.model}")

# car1 = Car("BMW", "X5")
# print(car1.show())

## Object Initialization & Method Invocation

# class gfg:
#     def __init__(self, topic):
#         self._topic = topic  # Store parameter value in instance variable

#     def topic(self):
#         print("Topic:", self._topic)  # Access the renamed variable

# # Creating an instance of gfg
# ins = gfg("Python")

# # Calling the topic method
# ins.topic()

## Circle Class for Area Calculation

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
    
# circle = Circle(5)
# print("Area of Circle: ", circle.area())

## First class function
# 1. Assigning Functions to Variables

# def greet(name):
#     print("Hello, " + name + "!")
    
# m = greet
# m("Mayur")

# 2. Passing Functions as Arguments

# def msg(name):
#     return "Hello, " + name + "!"

# def fun1(fun2, name):
#     return fun2(name)

# print(fun1(msg, "Mayur"))

# 3. Returning Functions from Functions

# def fun1(msg):
#     def fun2():
#         return f"Hello, {msg}!"
#     return fun2

# func = fun1("Mayur")
# print(func())

# 4. Using Functions in Data Structures

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y

# d = { "add": add, 
#      "subtract": subtract 
#      }

# print(d["add"](10, 5))
# print(d["subtract"](10, 5))

### Lambda function

# s1 = "Mayur Jadhav"
# s2 = lambda s1 : s1.upper()
# print(s2(s1))

## 1. Using with Condition Checking

# s = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
# print(s(10))
# print(s(-5))
# print(s(0))

## 2. Using with List Comprehension

# list1 = [lambda num=x: num * 10 for x in range(1, 5)]
# for i in list1:
#     print(i())
    
## 3. Using for Returning Multiple Results

# x = lambda a, b: (a + b, a - b, a * b, a / b if b != 0 else "Undefined")
# print(x(10, 5))

## 4. Using with filter()

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x: x%2 == 0, n))
## even = filter(lambda x: x%2 == 0, n)
# print(even)
## print(list(even))

## 5. Using with map()

# a = [1, 2, 3, 4]
# b = map(lambda x: x * 2, a)
# print(list(b))

## 6. Using with reduce()

# from functools import reduce
# a = [1, 2, 3, 4]
# b = reduce(lambda x, y: x * y, a)
# print(b)

### Python map() function

# s = ['1', '2', '3', '4', '5']
# s = list(map(float, s))
# print(s)

## 1. Converting map object to a list

# def double(x):
#     return x * 2

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(double, numbers))
# print(doubled_numbers)

## 2. Using with Lambda Functions

# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(lambda x: x * 2, numbers))
# print(doubled_numbers)

## 3. Mapping Multiple Iterables

# def add(x, y):
#     return x + y

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# added_numbers = list(map(add, numbers1, numbers2))
## added_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
# print(added_numbers)

## 4. Using with Different Data Types

# string = ['apple', 'banana', 'cherry']
# Uppercase = list(map(str.upper, string))
# print(f"The string is -> {Uppercase}")

## 5. Extracting first character from strings

# words = ["Apple", "Banana", "Mango"]
# first_letter = map(lambda s:s[0], words)
# print(list(first_letter))

## 6. Removing whitespaces from strings

# words = ["  Apple", "Banana  ", "  Mango  "]
# stripped_words = map(str.strip, words)
# print(list(stripped_words))

## 7. Calculate fahrenheit from celsius

# celsius = [0, 20, 34, 56, 78]
# fahrenheit = list(map(lambda c: c * (9/5) + 32, celsius))

# fl = fahrenheit.float()
# print(fl)

### 

import time

nums = [2, 3, 5]
target = 8

start = time.time()

class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
              return [num_map[complement], i]
        num_map[num] = i
        
        return []

end = time.time()

print(Solution().twoSum(nums, target))
print("Execution Time: ", end - start)

