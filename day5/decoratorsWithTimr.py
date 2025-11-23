import time


def decorators(func):
    def wrapper(*arg, **kwarg):
        start = time.time()
        result = func(*arg, **kwarg)
        end = time.time()
        print(f"time taken {end - start}")
        return result

    return wrapper


@decorators
def compute():
    for _ in range(100000):
        pass


compute()
