def named(**kwargs):
    print(kwargs)

named(name="Gojo", age=29)

def named(name, age):
    print(name, age)

details = {"name": "Gojo", "age": 29}

named(**details)

def print_nicely(**kwargs):
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Gojo", age=29, job="The Honoured One")

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1,3,5, name="Gojo", age=29)

def myfunction(**kwargs):
    print(kwargs)

# myfunction(**"Bob")
# myfunction(**None)
