# Define a function named 'calculate_area' that takes one parameter 'shape'
def calculate_area(shape):
    # Check if the shape is "rectangle"
    if shape == "rectangle":
        # Prompt the user to enter the length of the rectangle and convert it to an integer
        length = int(input("Enter length of rectangle: "))
        # Prompt the user to enter the breadth of the rectangle and convert it to an integer
        breadth = int(input("Enter breadth of rectangle: "))
        # Calculate and print the area of the rectangle
        print("Area of rectangle is:", length * breadth)
    # Check if the shape is "circle"
    elif shape == "circle":
        # Prompt the user to enter the radius of the circle and convert it to an integer
        radius = int(input("Enter radius of circle: "))
        # Calculate and print the area of the circle using the formula πr^2
        print("Area of circle is:", 3.14159 * radius * radius)
    # If the shape is neither "rectangle" nor "circle"
    else:
        # Print None
        print(None)