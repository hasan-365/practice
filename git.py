def greet_user():
    name = input ("what is your name?")
    age = input ("how old are you?")
    location = input ("where are you from?")
    job_role = input ("what is your job role?")
    print (f"Hello, {name} an {job_role} from {location}! You are {age} years old! Welcome to the Git practice")

if __name__ == "__main__":
    greet_user()