def greet_user():
    name = input ("what is your name?")
    age = input ("how old are you?")
    location = input ("where are you from?")
    print (f"Hello, {name} from {location}! You are {age} years old! Welcome to the Git practice")

if __name__ == "__main__":
    greet_user()