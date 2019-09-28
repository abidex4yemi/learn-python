# Basic function declaration
def foo():
    print("World World!!!")


def meaning_of_life():
    return 42


# print(meaning_of_life())

# returns a nontype
# called_foo = foo()

# returns 42
called_meaning = meaning_of_life()


def add_numbers(x, y):
    return x + y


# print(add_numbers(3, 2))


def greeting(name):
    greeting = "Hello"
    return f"{greeting} {name}"


# print(greeting("Yemi"))

# function arguments


def say_greeting(greeting, name):
    return f"{greeting} {name}"

# Calling say_greeting with incomplete parameter will throw typeError
# say_greeting("Hello")


# function with default argument
# Note: default argument must come last when declaring the function
#
# This code below will give SyntaxError: non-default argument follows default argument
# def say_greeting_with_default_arg(name, greeting="Hello!"):
#     return f"{greeting} {name}"

def say_greeting_with_default_arg(name, greeting="Hello!"):
    return f"{greeting}, {name}"


# print(say_greeting_with_default_arg("Yemi", "Hey"))


def create_query(language="Javascript", num_stars=50, sort="desc"):
    return f"language: {language}, number of stars: {num_stars}, sort: {sort}"
