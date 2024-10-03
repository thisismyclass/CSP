cut1 = int(input("how far into the pipe do yoy want to make your first cut in ft?: "))
cut2 = int(input("how far into the pipe do yoy want to make your second cut in ft?: "))

side1 = int(0 + cut1)
side2 = int(cut2 - cut1)
side3 = int(10 - cut2)
s = (side1 + side2 + side3)/2

area = s*(s-side1)*(s-side2)*(s-side3)**0.5





print("the first side will be", side1 ,"ft")
print("the second side will be", side2 ,"ft")
print("the third side will be", side3 ,"ft")
print("the area of this triangle is", area,"ft squared")







