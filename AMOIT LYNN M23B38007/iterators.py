# Decorators are a function that etend the behavior of a base function without modifying it

def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("Add sprinkles")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("we added fudge")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} icecream")


get_ice_cream("vanilla")