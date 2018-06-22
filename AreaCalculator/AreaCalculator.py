"""
The program does the following:

Prompts the user to select a shape.
Calculates the area of that shape.
Prints the area of that shape to the user.

Author: Erik Djamgarian

"""
print "The program is starting now.. "

print "Hi, I am Sara. I will guide you through this little program by asking you for various inputs. Ok? Lets go!"

option = raw_input("Im gonna need a type of a shape in order to calculate the area. Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius**2
  print "The area is %f" %area
elif option == "T":
  base = float(raw_input("Please enter a base for your triangle: "))
  height = float(raw_input("Please enter a height for your triangle: "))
  area = 0.5 * base * height
  print "Area of triangle is %f" %area
else:
  print "Sorry invalid shape, did you make sure you entered a capital letter?"

print "Thanks for participating!"
