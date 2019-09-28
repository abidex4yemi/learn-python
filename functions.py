# Basic function declaration
def foo():
    print("World World!!!")


def meaning_of_life():
    return 42


print(meaning_of_life())

# returns a nontype
# called_foo = foo()

# returns 42
called_meaning = meaning_of_life()


def add_numbers(x, y):
    return x + y


print(add_numbers(3, 2))


def greeting(name):
    greeting = "Hello"
    return f"{greeting} {name}"


print(greeting("Yemi"))
