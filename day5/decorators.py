def my_decorators(func):
    def wrapper():
        print("Before run the function")
        func()
        print("after run the function")

    return wrapper


@my_decorators
def hello():
    print("Hello world")


hello()
