from random import randint,choice
def add(x,y): #function scope
    r = x+y
    return r

# a = int(input("a = "))
# b = int(input("b = "))
# t = add(a,b)
# print(t)
# #print(add(a,b))

def eval(x,y,op):
    if op == "+":
        r = x+y
    elif op == "-":
        r = x-y
    elif op == "*":
        r = x*y
    elif op == "/":
        r = x/y
    return r
def random():
    x = randint(0,10)
    y = randint(0,10)
    error = randint(-1,1)
    op=choice(["+","-","*","/"])
    r = eval(x,y,op) + error
    #r = t + error
    # s = "{0} {3} {1} = {2}".format(x,y,r,op)
    return [x,y,op,r]
# result= eval(9,10,"-")
# print(result)


