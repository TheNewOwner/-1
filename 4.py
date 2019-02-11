def check( x, y , o):
    if o=="+":
        num=x+y
        return num
    elif o=="-":
        num=x-y
        return num
    elif o=="*":
        num=x*y
        return num
def zero( x = 11):
    if x==11:
        return 0
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(0,n,op)
def one( x = 11):
    if x==11:
        return 1
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(1,n,op)
def two( x = 11):
    if x==11:
        return 2
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(2,n,op)
def three( x = 11):
    if x==11:
        return 3
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(3,n,op)
def four( x = 11):
    if x==11:
        return 4
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(4,n,op)
def five( x = 11):
    if x==11:
        return 5
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(5,n,op)
def six( x = 11):
    if x==11:
        return 6
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(6,n,op)
def seven( x = 11):
    if x==11:
        return 7
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(7,n,op)
def eight( x = 11):
    if x==11:
        return 8
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(8,n,op)
def nine( x = 11):
    if x==11:
        return 9
    if type(x)==tuple:
        n=x[0]
        op=x[1]
    print check(9,n,op)
def plus(num):
    return (num,"+")
def minus(num):
    return (num,"-")
def times(num):
    return (num,"*")

seven(times(five()))
four(plus(nine()))
eight(minus(three()))
