import math

def calculate_circumference_circle(radius):
    return 2 * math.pi * radius

def calculate_area_circle(radius):
    return math.pi * radius**2

def calculate_perimeter_rectangle(length, width):
    return 2 * (length + width)

def calculate_area_rectangle(length, width):
    return length * width

def calculate_perimeter_triangle(side1, side2, side3):
    return side1 + side2 + side3

def calculate_area_triangle(base, height):
    return 0.5 * base * height

def calculate_surface_area_cube(side):
    return 6 * side**2

def calculate_volume_cube(side):
    return side**3

def calculate_perimeter_quadrilateral(side1, side2, side3, side4):
    return side1 + side2 + side3 + side4

def calculate_area_quadrilateral(side1, side2, side3, side4):
    s = (side1 + side2 + side3 + side4) / 2
    area = math.sqrt((s-side1) * (s-side2) * (s-side3) * (s-side4))
    return area

def calculate_surface_area_cone(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * (radius + slant_height)

def calculate_volume_cone(radius, height):
    return (1/3) * math.pi * radius**2 * height

def calculate_surface_area_pyramid(base, height):
    slant_height = math.sqrt(base**2 + height**2)
    return base * slant_height + base**2

def calculate_volume_pyramid(base, height):
    return (1/3) * base**2 * height

# Function to calculate perimeter of a square
def calculate_perimeter_square(side):
    return 4 * side

# Function to calculate area (content) of a square
def calculate_area_square(side):
    return side**2

# Display the available options
print("Welcome to the Shape Calculator!")
print("Choose an option:")
print("1. Circle")
print("2. Triangle")
print("3. Rectangle ")
print("4. Sqaure")
print("5. Cubic")
print("6. Cone")
print("7. Pyramid")

# Get user input for option
option = int(input("Enter your choice (1/2/3/4/5/6/7): "))

if option == 1:
    radius = float(input("Enter the radius of the circle: "))
    circumference = calculate_circumference_circle(radius)
    area = calculate_area_circle(radius)
    print("The circumference of the circle is:", circumference)
    print("The area of the circle is:", area)
elif option == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    perimeter = calculate_perimeter_triangle(base, base, base)
    area = calculate_area_triangle(base, height)
    print("The perimeter of the triangle is:", perimeter)
    print("The area of the triangle is:", area)

elif option == 3:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    perimeter = calculate_perimeter_rectangle(length, width)
    area = calculate_area_rectangle(length, width)
    print("The perimeter of the rectangle is:", perimeter)
    print("The area of the rectangle is:", area)
elif option == 4:
    length = float(input("Enter the length of the square: "))
    width = float(input("Enter the width of the square: "))
    perimeter = calculate_perimeter_rectangle(length, width)
    area = calculate_area_rectangle(length, width)
    print("The perimeter of the square is:", perimeter)
    print("The area of the square is:", area)