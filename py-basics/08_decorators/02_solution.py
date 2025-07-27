
def debug(func):
    def wrapper(*args):
        print(args)
        args_value = ', '.join(str(arg) for arg in args)
        print(args_value)
        return func(args)
    return wrapper


@debug
def greet(name, greeting = "hello"):
    print(f"{greeting}, {name} Chilwal")

greet("Yogesh", "hay")