for i in range(5):
    print("hello world")
def calc(a, o, b):
    if o=='+':
    print(a+b)
    elif o=='-':
    print(a-b)
    elif o=='/':
    print(a/b)
    else o=='*':
    print(a*b)
    return;
s=input("enter operator +-*/")
c, d=input("enter two  numbers")
out=calc(c, s, d)
Print (out)