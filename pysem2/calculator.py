# print("select operation:")
# print("1,Addition")
# print("2,Subtraction")
# print("3,Multiplication")
# print("4,Division")

# choice=input("enter choice(1/2/3/4):")

# num1=int(input("enter first number:"))
# num2=int(input("enter second number:"))

# if choice=='1':
#     print(num1,"+",num2,"=",num1+num2)  

# elif choice=='2':
#     print(num1,"-",num2,"=",num1-num2)

# elif choice=='3':
#     print(num1,"*",num2,"=",num1*num2)

# elif choice=='4':
#     print(num1,"/",num2,"=",num1/num2)

# else:
#     print("invalid input")     
# m=int(input("enter a number:"))
# if m==1:
#     print("january")
# elif m==2:
#     print("february")
# elif m==3:
#     print("march")
# elif m==4:
#     print("april")
# elif m==5:
#     print("may")
# elif m==6:
#     print("june")
# elif m==7:

import turtle
wn = turtle.Screen()
wn.bgcolor("white")


pen = turtle.Turtle()
pen.color("blue")
pen.speed(3)


def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)




      