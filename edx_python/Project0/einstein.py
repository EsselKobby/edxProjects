mass = int(input("Please enter the required mass: "))

c = 300000000


def square(c):
    c *= c
    return c


E = mass * square(c)

print(f"m:{mass}")
print(f"E: {E}")
