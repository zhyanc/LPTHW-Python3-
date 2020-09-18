ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there's not 10 things in that list, let's fix that.")
#print(ten_things)

stuff = ten_things.split(' ')
#print(stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) < 10:
    next_one = more_stuff.pop()
    print("Adding '%s' ..." % next_one)
    stuff.append(next_one)
    print("There is %d length now!" % len(stuff))

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
