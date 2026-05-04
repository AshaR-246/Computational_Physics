"""
Firsr Part: In this assignment students will learn to find the root of the given function using the Newton-Raphson method. They will first derive the formula in their notebook and get it checked by the 
instructor. At this time they may clear any doubt they have about the method. They will write the code to find the roots of a given function. 

Second Part: It would be the best code if it works for complex roots also, and gives at least two-roots (if there) in a single compilation. 
"""
import cmath

def f(x):
    return x**4 - x**3 + x**2 - x - 1

def df(x):
    return 4*x**3 - 3*x**2 + 2*x - 1

x_o = 2

for i in range(1,11):
    if df(x_o) == 0:
        print("Method failed")
        break

    x1 = x_o - (f(x_o)/df(x_o))

    if abs(x1 - x_o) < 1e-6:
        break

    x_o = x1
    print(f"x{i}={x1:.6f}")

print("Newton Raphson Method for Complex root")

# Complex root
def g(z):
    return z**3+z**2+z+1

def dg(z):
    return 3*z**2+2*z+1

z_o = complex(1,1)

for i in range(1,11):
    if dg(z_o) == 0:
        print("Method failed")
        break

    z1 = z_o - (g(z_o)/dg(z_o))

    if abs(z1 - z_o) < 1e-4:
        break

    z_o = z1
    print(f"z{i}={z1:.4f}")
