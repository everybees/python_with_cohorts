prompt=input("what is your problem? Type \"enter\" if you wish to continue the conversation")
if prompt=="enter":
    prompt2=input("have you had this problem before? Y/N")
    if prompt2=="Y":print("well, you have it again")
    elif prompt2=="N":print("well, you have it now")

elif prompt!="enter":print("bye, goodluck!")
