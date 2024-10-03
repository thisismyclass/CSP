Length = int(input("what is the length of yard in ft: "))
Width = int(input("what is the width of yard in ft: "))
Cost = float(input("what is the cost per square feet?: "))

area = int(Length * Width)
total_cost = float(Cost * area)
perimeter = int(Length + Length + Width + Width)

print("the total area of your yard is", str(area) ,)
print("the perimmeter of your yard is", str(perimeter) ,)
print("the total cost of your turf will be", str(total_cost) ,)

