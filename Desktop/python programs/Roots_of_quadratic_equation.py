# Taking input
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))


discriminant = b * b - 4 * a * c

# Checking the type of roots
if discriminant > 0:
    Type_of_root = "Real and distinct"
    root_1 = (-b + discriminant** 0.5) / (2 * a)
    root_2 = (-b - discriminant** 0.5 ) / (2 * a)
    print("The type of roots are: {}".format(Type_of_root))
    print("Root 1: {}".format(root_1))
    print("Root 2: {}".format(root_2))

elif discriminant == 0:
    Type_of_root = "Real and equal"
    root = -b / (2 * a)
    print("The type of roots are: {}".format(Type_of_root))
    print("Root: {}".format(root))

else:
    Type_of_root = "Complex"
    real_root = -b / (2 * a)
    imaginary_root = ((-discriminant) ) / (2 * a)
    print("The type of roots are : {}".format(Type_of_root))
    print("Root 1: {} + {}i".format(real_root, imaginary_root))
    print("Root 2: {} - {}i".format(real_root, imaginary_root))
