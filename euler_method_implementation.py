"""First Part: Make a Python code to solve the given first order differential equation dy/dx=f(x,y) using the Euler Method""" 
def f(x,y):
    return (2*x - y)/(x + 2)

x0 = 0
y0 = 4
h = 0.05
n = 20

for i in range(1, n+1):
    y0 += h * f(x0, y0)
    x0 += h
    print(f"y{i} = {y0:.5f}")

""" Second Part: What are the limitation of this method, and how would you improve the method? 
"""
""" It is sensitive to step size(h), for larger step size the value deviates largely from actual value. 
This equation becomes unstable for higher order ODE. 
Euler’s method uses only the slope at the beginning of the interval. While slope changes continuously. Error accumulates over iterations. 

The method can be improved by reducing the step size or by using more accurate numerical methods such as the Improved Euler’s method or Runge–Kutta methods, which use multiple slope evaluations to obtain better approximations. """