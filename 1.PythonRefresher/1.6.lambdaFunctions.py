def add(x, y):
    return x + y

add = lambda x, y: x+ y

print(add(5,7))

print((lambda x,y: x + y)(10, 7))

def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

# Same result
doubled = [double(x) for x in sequence]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = map(double, sequence)
doubled = list(map(lambda x: x*2, sequence))

print(doubled)