# Packing and Unpacking variables 
# args (*) & kwargs (**)

# args (*)
# Unpack
print(1,2,3,4,5,6)

# list
numbers = [1,2,3,4,5,6]
# tuples
numbers = 1,2,3,4,5,6
# numbers packed in list & touples
# unpaking in single element using *numbers
print(*numbers)

# example
print("abc")
print(*"abc")
# same as
print("a","b","c")

# pack hapens inside a function
def add(x,y):
    return x+y

# can add only two numbers
add(10,10)

def add(*numbers):
    # like tuples numbers = (1,2,3,4,5,6,7)
    total = 0
    for number in numbers:
        total = total + number
    return total

print(add(1,2,4))

# pack and unpacking keyword arguments
def about(name,age,likes):
    return f'Meet {name}, a {age} years old {likes} programmer.'
# as usual
about(name ="shovon", age=28, likes="javaScript")                   
print(about(name ="shovon", age=28, likes="javaScript"))

# Packing using keyword args
data = {
    "name": "Shovon",
    "age": 28,
    "likes":"JavaScript & Python"
}

about(**data)
print(about(**data))

# Unpacking using keyword args
data = {
    "name": "Shovon",
    "age": 28,
    "likes":"JavaScript & Python"
}

def foo(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')

print(foo(**data))
print(foo(name="Shovon",age=28,likes="JavaScript & Python"))
