# Python Decorators Tutorial
# -------------------------
# Decorators are a powerful way to modify or enhance functions without directly changing their source code.
# They follow the principle of open-closed: open for extension, closed for modification.

# Basic Function Decorator
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} completed")
        return result
    return wrapper

# Example usage of a basic decorator
@log_function_call
def greet(name):
    return f"Hello, {name}!"

# Decorator with Parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Example usage of decorator with parameters
@repeat(times=3)
def say_hello(name):
    print(f"Hello, {name}!")

# Class Decorator
class Timer:
    def __init__(self, func):
        self.func = func
        self.total_time = 0

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        self.total_time += time.time() - start
        return result

# Example usage of class decorator
@Timer
def slow_function():
    import time
    time.sleep(1)
    return "Function completed"

# Decorator to preserve function metadata
from functools import wraps

def preserve_metadata(func):
    @wraps(func)  # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        """This is the wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def add(a, b):
    """This function adds two numbers"""
    return a + b

# Example of method decorator (for class methods)
def validate_arguments(func):
    def wrapper(self, *args, **kwargs):
        if len(args) == 0:
            raise ValueError("At least one argument is required")
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @validate_arguments
    def sum_numbers(self, *args):
        return sum(args)

def main():
    # Testing basic decorator
    print("\nTesting basic decorator:")
    result = greet("Alice")
    print(f"Result: {result}")

    # Testing decorator with parameters
    print("\nTesting decorator with parameters:")
    say_hello("Bob")

    # Testing class decorator
    print("\nTesting class decorator:")
    slow_function()
    print(f"Total time taken: {slow_function.total_time:.2f} seconds")

    # Testing metadata preservation
    print("\nTesting metadata preservation:")
    print(f"Function name: {add.__name__}")
    print(f"Function docstring: {add.__doc__}")

    # Testing method decorator
    print("\nTesting method decorator:")
    calc = Calculator()
    try:
        print(f"Sum: {calc.sum_numbers(1, 2, 3, 4)}")
        print(f"Sum with no args (should raise error):", calc.sum_numbers())
    except ValueError as e:
        print(f"Caught expected error: {e}")

if __name__ == "__main__":
    main()
