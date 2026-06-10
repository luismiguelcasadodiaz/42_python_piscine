def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished.")
        return result
    return wrapper


@log_call
def greet(name):
    print(f"Hi, {name}!")


if __name__ == "__main__":
    greet("Alice")
    # Output:
    # Calling greet...
    # Hi, Alice!
    # greet finished.
