def decorator(func):
    def wrapper(*args, **kwargs):
        additional_word = "additional_word"
        return_val = func(*args, **kwargs) + ", " + additional_word
        return return_val
    return wrapper

@decorator
def hello(a="Hello MAZAFACKA"):
    return a

result = hello()
print(result)
