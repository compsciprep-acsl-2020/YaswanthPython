shape=input("Enter a shape")
if(shape=="triangle"):
    b = int(input("enter base"))
    h = int(input("enter base"))
    print("area of triangle is:",(.5)*b*h)
elif(shape=="square"):
    s = int(input("enter side"))
    print("area of a square is,", s**2)
elif(shape=="rectangle"):
    l = int(input("Enter side"))
    w = int(input("enterside"))
    print("area of rectangle is,", l*w)
elif(shape=="parallelogram"):
    b = int(input("enter side"))
    h = int(input("enter side"))
    print("area of parallelogram is,", b*h)
elif(shape=="circle"):
    r = int(input("enter side"))
    print("area of circle is,", (3.14)*r**2)
elif(shape=="trapezoid"):
    b1 = int(input("enter side"))
    b2 = int(input("enter side"))
    h = int(input("enter side"))
    print("area of trapezoid is, (0.5)*(b1+b2)*h")
elif(shape=="rhombus"):
    p = int(input("enter side"))
    q = int(input("enter side"))
    print("area of rhombus is, p*q/2")
else:
    print("error")