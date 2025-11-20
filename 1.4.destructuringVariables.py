x = 5,11
x,y = 5,11

t = 5,11

x,y = t

print(x,y)

people = [("Gojo", 29, "Jujutsu Sorcerer"), ("Tony", 50, ("Genius", "Billionaire", "Playboy", "Philantropist")), ("Itachi", 19, "Memeber of Akatsuki")] 

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Proffesion: {profession}")

for name, _ , profession in people:
    pass

head, *tail = [1,2,3,4,5] 
*head, tail = [1,2,3,4,5]
print(head)
print(tail)