from random import randint, choice
import calc
# x = randint(0,10)
# y = randint(0,10)
error = randint(-1,1)
# #r = x + y + error
# op=choice(["+","-","*","/"])

# def eval(x,y,op):
#     if op == "+":
#         return x+y
#     elif op == "-":
#         return x-y
#     elif op == "*":
#         return x*y
#     elif op == "/":
#         return x/y

# t = eval(x,y,op)

# t = calc.eval(x,y,op)
# r = t + error

quiz = calc.random()
# x = quiz[0]
# y = quiz[1]
# op = quiz[2]
# r = quiz[3]
x,y,op,r = quiz

output = "{0} {3} {1} = {2}".format(x,y,r,op)
#output = calc.random()

print(output)

user_answer = input("(Y/N) ? ").upper()

if error == 0:
    if user_answer == "Y":
        print("Yay")
    else:
        print("Nay")
else:
    if user_answer == "Y":
        print("Nay")
    else:
        print("Yay")

# if user_answer == "Y":
#     if (error == 0):
#         print("Yay")
#     else:
#         print("You're wrong")
# elif user_answer == "N":
#     if (error == 0):
#         print("You're wrong")
#     else:
#         print("Yoy")
# else:
#     print("Invalid operators")


