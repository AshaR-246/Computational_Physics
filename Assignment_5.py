"""Make a code to integrate the given function in the given interval [a, b] using trapezoidal method."""
def f(x):
    return 2*x + 3*x**2

a = 1; b = 2; n = 10   ## Getting 10.000 after 32 iterations
h = (b - a) / n

I = (h/2) * (f(a) + f(b))

for i in range(1, n):
    a += h
    I += h * f(a)

print(f"integral of 2*x+3*x**2 over an interval [1,{a:.4f}] is {I:.3f}")


# step size = 10^-4, I=10.000000005
# step size = 10^-3, I=10.000000500
# step size = 10^-2, I=10.000050000
"""Learn how the result of the integration changes with respect to the step size h. How would you choose optimal step size? """
""" Error decreases with smaller step size. Choosing step size depends on how accurate we want our result to be. i.e. Step size to be chosen depends on accuracy of result required (upto a certain decimal points) 
""" 
""" Second Part: What are the limitation of this method? Give an example of better method if you are aware.   
"""
