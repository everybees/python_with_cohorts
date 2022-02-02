first_name = 'Johnnie'
last_name = 'Doe'
age = 47
state_of_origin = 'Lagos'
for i in range (0,len(first_name),2):
    print (first_name[i].upper(),age // 10,sep="",end="")
    
print ("\n")   
    
for i in range (0,len(state_of_origin),2):
    print (state_of_origin[i].upper(),last_name.upper(),sep="",end="")
    
print ("\n")
    

full_name = first_name + last_name
full_name = full_name.upper()
for i in range (len(full_name)):
    if i == len(full_name) - 1:
        print (full_name[i])
    else:
        print (full_name[i], end= "-")
    

   