import time

def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        print("Total time taken in : ", function.__name__, end - start)
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

fast_function()