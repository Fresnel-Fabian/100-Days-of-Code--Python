import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before function
        function()
        print("function excecuted with 2 second delay")
        # Do something after function
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

say_hello()

def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)
decorated_function()