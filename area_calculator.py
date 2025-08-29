#Write a menu driven python program which perform the following:
'''
    ->Find area of Circle.
    ->Find area of Triangle.
    ->Find area of Square.
    ->Find area of Rectangle.

    Hint: Use Infinite while loop for menu.
'''

print("Menu: ")
print("1.Area of Circle")
print("2.Area of Triangle")
print("3.Area of Square")
print("4.Area of Rectangle")
print("5.Exit")
print("----------------------")

while True:
    choice = int(input("Enter Value 1 to 5: "))
    print("----------------------")

    if choice == 1:
        print("Area of Circle")
        radius = float(input("Enter Value of Radius: "))
        area_circle = 3.14*radius*radius
        print("Area of Circle is: ", area_circle)

    elif choice == 2:
        print("Area of Triangle")
        base = float(input("Enter Value of Base: "))
        height = float(input("Enter Value of Height: "))
        area_triangle = 0.5*base*height
        print("Area of Triangle is: ", area_triangle)

    elif choice == 3:
        print("Area of Square")
        side = float(input("Enter Value of Side: "))
        area_square = side*side
        print("Area of Square is: ", area_square)

    elif choice == 4:
        print("Area of Rectangle")
        length = float(input("Enter Value of Length: "))
        width = float(input("Enter Value of Width: "))
        area_rect = length*width
        print("Area of Rectangle is: ", area_rect)

    elif choice ==5:
        print("Exit")
        break

    else:
        print("Wrong Value, Try Again...")