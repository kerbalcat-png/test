def divide(a, b):
    try:
        return a/b
    except TypeError: 
        raise TypeError
    
def multiply(a, b):
    try: 
        return a*b
    except TypeError: 
        raise TypeError


# import tests