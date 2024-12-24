# Variables and Basic Python Syntax ...............................
a=12                        # Basic variable declaration(No Data type required)
b=23
print('These are Basic Maths Operations performed on variable')  # Basic Print Function
print('New line')    # Here by default a new line is introduced at the end of <the data to be printed>.
print('Hello World',end=" ")
# This is a method by which a specific parameter(end) is passed to the print function definition and the by default new line
# character occurring at the end of <data to be printed> is replaced by space(character you want).


# Variables.......................................................................
# Note:-
# 1. Variable declaration doesn't require a data type but still each variable is allocated a data type.
# 2. This data type can be checked using type function.
# 3. A variable can store any type of data.
# 4. There are 3 types of numbers integers, float and complex
# 5. Multiple variable assignment:-
# a,b,c=10,20,30    .......As python allows tuples thus multiple assignment technique can be used.
integerno=10
floatno=1.4
complexno=23+4j
# Operators........................................................
print(a+b)                      # Normal Addition
print(a-b)                      # Normal Subtraction
print(a*b)                      # Normal Multiplication
print(a/b)                      # Division with float answer
print(a//b)                     # Division with integer answer
print(a**b)                     # Exponent operator
print(a%b)                      # Remainder Operator
print(a*b/+a/b/b*b**b*b//a-b)   # This is done by BODMAS Rule


# User Input........................................
a=input()
print(a,type(a))
# This input function is used for console input. It returns console input as string. Thus type a would be string.
b=int(input())
print(b,type(b))
# To convert a string into a number we can do it using int function. Similarly there is a float function.
c=float(input())
d=complex(c,b)
print(d,type(d))
