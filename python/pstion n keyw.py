1. define a function that takes two numbers and return their sum.
eg;add(3,4) should return 7
positional arguments
def hello(a,b):
    
    return a+b
print((hello(3,4)))
keyword arguments
def hello (a,b):
    
    return a+b
print(hello(a=3,b=4))        

2.write a function that takes a neme as input and prints a greeting.
eg:greet("Alice") should print "Hello,Alice"  
positional arguments 
def greet(name):
     
    print((f"hello,{name}!"))
greet("Alice")
keyword arguments    
def greet(name):
    
    print(f"hello,{name}!")
greet(name="Alice")
3.creat a function that returns the square of a number.
eg:square(5) should return 25
positional
n=5
def square(n):
    return n * n
result = square(5)
print(result)
keywords
def square(n):
    return n * n
result = square(n=5)
4.write a function that checks if a number is even or odd.
eg:check_even_odd(7)should print "odd"
positional
def check_even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
 check_even_odd(7)
 keyword
def check_even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd") 
check_even_ odd(n=7) 
         
5.create a function that takes a list of numbers and return the 
largest of 3 numbers number 
positional      
def num(a,b,c):
    print(max(a,b,c))
 num(30,40,50) 
def num(a,b,c):
    if a>b and a>c:
        print("a is greater than b and c")  
    elif b>a and b>c:
        print("b is greaterthan a and c")
    else:
        print("c is greater than a and b")    
 num(30,40,50)  
keyword     
def num(a,b,c):
    if a>b and a>c:
        print("a is greater than b and c") 
    elif b>a and b>c:
        print("b is greater than a and c")       
    else:
        print("c is greater than a and b")    
num(a=30,c=50,b=40)        