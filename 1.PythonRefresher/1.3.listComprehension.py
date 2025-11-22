numbers = [1,3,5]
doubled = [num * 2 for num in numbers]
print(doubled)

friends = ["Tony", "Satoru", "Suguru", "Peter"]
start_s = [friend for friend in friends if friend.startswith("S")]
print(start_s)

print(id(friends))
print(id(start_s))
