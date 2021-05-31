for i in range(5):
    print("hello world")
def calc(a, e, b):
    if e=='+':
       print(a+b)
    elif e=='-':
       print(a-b)
    elif e=='/':
       print(a/b)
    elif e=='*':
       print(a*b)
    return;
s=input("enter operator +-*/")
c, d=input("enter two  numbers")
out=calc(c, s, d)
print (out)