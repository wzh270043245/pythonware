import random
c=300
d=5

for j in range(c):
    for i in range (d):
        a = random.randint (1, 9)
        b = random.randint (1, 9)
        print("%d X %d =      " % (a,b),end="")
    print("\n")