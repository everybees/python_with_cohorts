from re import X


f=None
for i in range(6):
    with open("app.log","w")as f:
        if i > 2:
            break
print(f.closed)


# def fun1():
#     x= 50
#     return x
# fun1()
# print(x)

# x= "abbaaf"
# x= "a"
# while i in x [:-1]:
#     print(i)

a=[1,2,3,4]
b=[sum(a[0:x+1])for x in range (0, len(a))]
print(b)