def say_hello(name):
    print(f"Hello, {name}!")

def greet_user():
    name = input("Enter your name: ")
    say_hello(name)

if __name__ == "__main__":
    greet_user()