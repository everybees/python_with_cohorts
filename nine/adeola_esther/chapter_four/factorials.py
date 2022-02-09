factorial=1

user= int(input('Enter the factorial number!: '))

if user>0:
    for i in range(user):
      factorial*=user
      user -=1
    print(factorial)

