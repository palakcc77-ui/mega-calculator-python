# Import math in your code
import math

#Define the functions
def square():
    a=float(input("Enter side: "))
    print(f"The area of square is {a*a}. ")
    print(f"The volume of square is {4*a}. ")
    
def rectangle():
    l=float(input("Enter length: "))
    b=float(input("Enter breadth: "))
    print(f"The area of rectangle is {l*b}. ")
    print(f"The perimeter of rectangle is {2*(l+b)}. ")

def triangle():
    b=float(input("Enter base: "))
    h=float(input("Enter height: "))
    print(f"The area of triangle is {(b*h)/2}. ")

def circle():
    r=float(input("Enter radius: "))
    print(f"The area of circle is {math.pi*r*r}. ")
    print(f"The circumfrence of circle is {2*math.pi*r}. ")

def cube():
    a=float(input("Enter Side: "))
    print(f"The area of cube is {6*a*a}. ")
    print(f"The volume of cube is {a**3}. ")

def sphere():
    r=float(input("Enter radius: "))
    print(f"The volume of sphere is {(4/3)*math.pi*r**3}. ")
    print(f"The area of sphere is {4*math.pi*r**2}. ")\
    
def cylinder():
    r=float(input("Enter radius: "))
    h=float(input("Enter height: "))
    print(f"The volume of cylinder is {math.pi*r**2*h}. ")
    print(f"The area of cylinder is {2*math.pi*r*(h+r)}. ")

def cone():
    r=float(input("Enter radius: "))
    h=float(input("Enter height: "))
    l=float(input("Enter slate height: "))
    print(f"The volume of cone is {(1/3)*math.pi*r**2*h}. ")
    print(f"The area of cone is {math.pi*r*(l+r)}. ")

while True:
    print("mega shape calculator ( function based)".upper().center(120))
    print(""
          "1. Square.\n" \
          "2. Rectangle.\n" \
          "3. Triangle.\n" \
          "4. Circle.\n" \
          "5. Cube.\n" \
          "6. Sphere.\n" \
          "7. Cylinder.\n" \
          "8. Cone.\n" \
          "9. Exist.\n" \
          "")
    choice=int(input("Enter any operation: "))
    if choice == 1:
       square()
    elif choice == 2:
       rectangle()
    elif choice == 3:
       triangle()
    elif  choice ==4:
         circle()
    
    elif choice == 5:
             cube()
    elif choice == 6:
             sphere()
    elif choice == 7:
             cylinder()
    elif choice == 8:
             cone()
    elif choice == 9:
             print("Program Ended.")
             breakpoint
    else:
       print("Invalid choice.")



