
#user1 = int(input("Enter a number: "))
#user2 = int(input("Enter a number: "))
#if user1 == user2:
 #   print("True")
#else:
    #print("False")

#no = 16

#user1 = int(input("Enter a number: "))

#if user1 == no:
   # print("True")
#else:
    #print("False")
user1score = 0
user2score = 0
for i in range(10):
    rock ='rock'
    paper ='paper'
    scissors ='scissors'
    user1 = input("Enter rock,paper,scissors :")
    user2 = input("Enter rock,paper,scissors :")

    if user1 == rock and user2 == paper:
        print('user2 win')
        user2score += 1

    if user1 == paper and user2 == scissors:
       print('user2 win')
       user2score += 1

    if user1 == rock and user2 == scissors:
        print("user1 win")
        user1score += 1

        print('user1score',user1score)
        print('user2score',user2score)