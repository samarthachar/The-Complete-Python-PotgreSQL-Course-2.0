friends = {"Tony", "Satoru", "Peter"}
local = {"Tony", "Peter"}

abroad = friends.difference(local)
print(abroad)

friends = local.union(abroad)
print(friends)


MCU = {"Tony", "Peter", "Satoru"}
JJK = {"Satoru", "Yuji", "Tony"}

both = MCU.intersection(JJK)
print(both)