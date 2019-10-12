#create a program to sort even and odd numbers
# 1. Prompt user for a number
# 2. Evalute if number is even or odd
# 3. Return even or odd

#number = int(input("please enter a number"))
def isEvenOdd(number):
    if(number%2 == 0):
                print("This is an even number")
    else:
                 print("this is an even number")

for i in range(10):
      Number = int(input("please enter number"))

      print(isEvenOdd(Number))