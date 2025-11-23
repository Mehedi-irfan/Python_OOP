def decorator(func):
    def wrapper(*args, **kwargs):
        print("Staring..")
        func(*args, **kwargs)
        print("Finished")

    return wrapper


@decorator
def great():
    print("hello")


great()
