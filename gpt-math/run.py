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

# Function to calculate perimeter of a cube
def calculate_perimeter_cube(side):
    return 12 * side

# Function to calculate area of a cube
def calculate_area_cube(side):
    return 6 * side**2

# Function to calculate volume of a cube
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

def calculate_surface_area_pyramid(base, width, height):
    # Calculate the surface area of a pyramid
    slant_height = math.sqrt(((base/2) ** 2) + height ** 2)
    surface_area = base * width + base * slant_height + width * slant_height
    return surface_area

def calculate_circumference_circumference(base, width):
    # Calculate the circumference of a pyramid
    circumference = math.sqrt((base ** 2) + (width ** 2)) + base + width
    return circumference

def calculate_volume_pyramid(base, height):
    return (1/3) * base**2 * height

# Function to calculate perimeter of a square
def calculate_perimeter_square(side):
    return 4 * side

# Function to calculate area (content) of a square
def calculate_area_square(side):
    return side**2

def solve_quadratic_equation(a, b, c):
    """Solve a quadratic equation of the form ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real solutions
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2


# Display the available options
print("Welcome to the Shape Calculator!")
print("Choose an option:")
print("1. Circle")
print("2. Triangle")
print("3. Rectangle ")
print("4. Sqaure")
print("5. Cube")
print("6. Cone")
print("7. Pyramid")
print("8. Quadratic")

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
    length = float(input("Enter the length of one side of the square: "))
    perimeter = calculate_perimeter_square(length)
    area = calculate_area_square(length)
    print("The perimeter of the square is:", perimeter)
    print("The area of the square is:", area)
elif option == 5:
    side = float(input("Enter the side length of the cube: "))
    # Calculate perimeter, area, and volume of the cube
    perimeter = calculate_perimeter_cube(side)
    area = calculate_area_cube(side)
    volume = calculate_volume_cube(side)
    print("The perimeter of the cube is:", perimeter)
    print("The area of the cube is:", area)
    print("The volume of the cube is:", volume)
elif option == 6:
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    # Calculate surface area and volume of the cone
    surface_area = calculate_surface_area_cone(radius, height)
    volume = calculate_volume_cone(radius, height)
    print("The surface area of the cone is:", surface_area)
    print("The volume of the cone is:", volume)
elif option == 7:
    base = float(input("Enter the base length of the pyramid: "))
    height = float(input("Enter the height of the pyramid: "))
    width = float(input("Enter the width of the pyramid: "))
    # Calculate surface area and volume of the pyramid
    surface_area = calculate_surface_area_pyramid(base, width, height)
    circumference = calculate_circumference_circumference(base, height)
    volume = calculate_volume_pyramid(base, height)
    print("The surface area of the pyramid is:", surface_area)
    print("The volume of the pyramid is:", volume)
    print("The circumference of the pyramid is:", circumference)
elif option == 8:
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    c = float(input("Enter the value of c: "))
    solution = solve_quadratic_equation(a, b, c)
    if solution is not None:
        print("Quadratic Equation Solution(s):", solution)
    else:
        print("Quadratic Equation has no real solutions.")