"""
PYTHON SYNTAX BASICS - Undergraduate Assignment
Edit ONLY the sections marked "Your code" and "Your answers"
"""

# EXERCISE 1: PRINT 
# I) Introduce yourself by printing you name and roll using print statment in python

# I) Your Code
print("Ashalata Rath ") 
print("24220PHY045") 

""" Question 1: What kind of errors you will get: (a) if you make mistake in the spelling of print statement 
 and (b) if you forget one of the quotation mark? """

# Your answers
# (a) NameError
# (b) SyntaxError: unterminated string 

# Question 2: (a) How do you comment a line in python?
# (b) How do you comment block of multiple lines without commenting each line? 

# Your answers:
# (a) using "#" 
# (b) using three single or double quotes at the start and end of the multi-line code. 


# EXERCISE 2: VARIABLES & TYPES 
# Assign: student_name (str), roll_no (int), cgpa (float)

# Your code
student_name="Ashalata" 
roll_no=45
cgpa = 9.00
# Question 3: (a) What do you understand about the three kind of data type: str, int, and float?

# Your answer (use block comment in your answer)
''' str: String can store characters as well as numbers. 
int stores integer data and float stores decimal numbers. '''
""" Question 3 (b) What would be output of the following code?
 (learn here how the variables are being updated)"""
x = 2.0
y = 5.0
y = 0.0
x = 10.0

print(x, y)
# Your answer 
#10.0 0.0
# EXERCISE 3: Mathematical Operators
""" Give an example of each mathematical operation: + (addition), 
  - (subtraction), * (multiplication), / (division), ** (power)"""

# Your code
print(5+2)
print(5-2)
print(5*2)
print(5/4)
print(5**2)
# Question 4: What would be output of the following code? 
print(2 > 5)
print(1 == 1)
print(2 < 4)

# Your answer
'''FALSE
   TRUE
   TRUE '''

# EXERCISE 4: IF-ELSE 
# Print "Pass" if gpa >= 6.0 else "Fail" (use gpa above)

# Your code
gpa=float(input("Enter GPA: ")) 
if gpa >= 6.0:
  print("Pass") 
else:
  print("Fail") 
# Question 5: What would be the output of following code?
if True:
  print("True")

if False:
  print("False")

# Your answer
#True
# EXERCISE 5: LISTS
""" Create a list colors = ["you name", "roll no"]
 and numbers = [9.8, 6.7, 8.5]
 use these lists to print your cgpa with your roll no and name if your cgpa is 6.7"""

# Your code 
colors = ["Ashalata Rath", "24220PHY045"]
numbers = [9.8, 6.7, 8.5]
for x in numbers:
  if x==6.7:
    print("Name: ", colors[0], "Roll no. :", colors[1],"CGPA:", x) 

# EXERCISE 6: FOR LOOP
# Print numbers 1 to 5 using for i in range(1,6)

# YOUR CODE 
for i in range(1,6):
  print(i) 

# Question 6: What kind of error you would get if you forget put : in the for loop?
# Your answer
#SyntaxError: expected ':' 

# EXERCISE 7: WHILE LOOP
# Print "Your name" 3 times using while

# Your code
i=0
while i<3:
  print("Asha")
  i+=1
# Why do we need while loop in python? 
# Your answer
# While loop runs a block of code till a condition is false. 
# it is used when number of times the loop has to run is not known. 
# EXERCISE 8: Functions
""" Define a function which adds two numbers. Call this function and print "sum of numbers=", ans where ans is 
 the summation you get from the function"""

# Your code
def add(x, y) 
 return x+y
print("sum of numbers=", add(10,20)) 
# EXERCISE 9: Testing loop
# Make a python code which print summation of odd and even numbers in the given range (0-100) using the for loop
s_o=0
s_e=0
for i in range(1,101):
  if i%2==0:
    s_e+=i
  else:
    s_o+=i
print("summation of odd: ", s_o) 
print("summation of even: ", s_i) 
# EXERCISE 10: Series summation 
""" Write a code to calculate the sum of n odd numbers starting from 1. You would need to use 
 for loop for calculating the summation"""
# Learn here how the variable is being updated in the for loop.
n=int(input("Enter a number: ")) 
sum_o=0
for i in range(1,2n+1):
  if i%2!=0:
    sum_o+=i
print(f"Sum of {n} odd numbers is {sum_o}") 



