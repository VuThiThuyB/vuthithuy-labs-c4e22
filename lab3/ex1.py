# x = int(input("Nhập x = "))
# y = int(input("Nhập y = "))
# s = x+y
# output = "{0} + {1} = {2}".format(x,y,s) #format
# print(output)

#import calc    dùng r = calc.eval(x,y,op)
#from calc import *   ~  from calc import eval,add
from calc import eval   # dùng r = eval(x,y,op)

x = int(input("Nhập x = "))
y = int(input("Nhập y = "))
list=["+","-","*","/"]
op =input("Nhập phép toán(+,-,*,/):")

r = eval(x,y,op)

#r = calc.eval(x,y,op)

# if op == list[0]:
#     r = x+y
# elif op == list[1]:
#     r = x-y
# elif op == list[2]:
#     r = x*y
# elif op == list[3]:
#     if y==0:
#         print("Invalid operators")
#     else:
#         r = x/y
# else:
#     print("Invalid operators")

print(x,op,y,"=",r)


