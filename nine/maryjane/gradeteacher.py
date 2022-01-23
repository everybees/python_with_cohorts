grade= [67, 56, 7, 56, 45, 30, 9]
count=0
passed=0
failed=0
teacher= "Jones"
for score in grade:
    if score>=56:passed+=1

    if score<56:failed+=1

print(passed, failed)
if(passed>failed):print("welldone Mr/Mrs", teacher)
else:print("work more on your students")
