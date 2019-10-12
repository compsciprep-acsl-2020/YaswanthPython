Shape=input("enter shape")
if(Shape=="triangle"):
    l1=int(input("enter side"))
    l2=int(input("enter side"))
    l3=int(input("enter side"))
    print("perimeter of triangle is:",l1+l2+l3)
elif(Shape=="square"):
    l=int(input("enter side"))
    w=int(input("enter side"))
    print=("perimeter of a square is:", l*2+w*2)
elif(Shape=="rectangle"):
    l=int(input("enter side"))
    w=int(input("enter side"))
    print=("perimeter of a rectangle is:", l*2+w*2)
elif(Shape=="trapezoid"):
    s1 = int(input("enter side"))
    s2 = int(input("enter side"))
    s3 = int(input("enter side"))
    s4 = int(input("enter side"))
    print=("perimeter of a trapezoid is:", s1+s2+s3+s4)
elif(Shape=="parallelogram"):
    l = int(input("enter side"))
    w = int(input("enter side"))
    print = ("perimeter of a parallelogram is:", l * 2 + w * 2)
elif(Shape=="circle"):
    r = int(input("enter side"))
    print = ("perimeter of a circle is:", (2)*(3.14)*r)
elif(Shape=="perimeter of a rhombus"):
    s = int(input("enter side"))
    print = ("perimeter of a rhombus is:", (4)*s)