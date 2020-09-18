i = 0
numbers = []
"""
while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)
    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ", numbers)

for num in numbers:
    print(num)
"""

def while_loop (loop_count, loop_step):
    for i in range (0, loop_count):
        print("At the top i is %d" % i)
        numbers.append(i)
        i = i + loop_step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ", numbers)

    for num in numbers:
        print(num)
    numbers.clear()
