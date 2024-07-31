# problem link: https://www.codechef.com/problems/CABLE

inp = input()
a, b, c, x = inp.split()

cuboid = int(a) * int(b) * int(c)
cube = int(x) ** 3

if cuboid > cube: print("Cuboid")
elif cube > cuboid: print("Cube")
else: print("Equal")