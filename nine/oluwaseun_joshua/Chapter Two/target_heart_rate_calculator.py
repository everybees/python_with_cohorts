
age=input("enter your age:  ")

Age=int(age)

beats_per_minute=220

maximum_heart_rate=beats_per_minute - Age

print("The maximum heart rate is: ",maximum_heart_rate)

target_heart_rate=(maximum_heart_rate / beats_per_minute) * 100
target_heart_rate=int(target_heart_rate)

print("your heart rate is: ",target_heart_rate)

if(target_heart_rate > 80 and target_heart_rate > 90):
    print("Ah! your heart rate is too high,your heart rate is 90 and above, you need to see a doctor")

elif(target_heart_rate > 50 and target_heart_rate <= 80):
    print("your heart rate is good, it is within the range of 50 to 80")

else:
    print("your heart rate is too low, it is within the range of 49 to 10, you need to act fast")

