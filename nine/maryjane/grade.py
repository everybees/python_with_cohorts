
passes=1
fail=1
count =0


while count <=10:
    score= input("enter score (1=pass, 2=fail):")
    score=int (score)
    if(score==1):passes+=1
    if(score==2):fail+=1
    count+=1
print("passes:", passes)
print("failed:", fail)