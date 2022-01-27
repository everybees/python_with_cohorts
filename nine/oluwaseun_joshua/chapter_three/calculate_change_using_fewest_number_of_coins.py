
purchase_price =input("enter an amount")
purchase_price=int(purchase_price)

for i in range(1):

    if(purchase_price /4==0 and purchase_price >200):  
        print("your change is in quarter")
    
    elif(purchase_price /2==0 and purchase_price <=140 ):
        print("your change is in dime")
    
    elif(purchase_price /2!=0):
        print("your change is in pennies")
