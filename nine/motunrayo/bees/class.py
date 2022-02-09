class_a=["Helen","Paul","Joe","Rogen","Motunrayo"]
class_b=["David","Adeola-Esther","Mofobi","John-Doe"]

longest_in_a = max(class_a,key=len)
longest_in_b = max(class_b,key=len)

smallest_in_a = min(class_a,key=len)
smallest_in_b = min(class_b,key=len)

if len(longest_in_a) > len(longest_in_b):
 print("class a has the longest name",longest_in_a)
if len(longest_in_b) > len(longest_in_a):
    print("class i has the longest name",longest_in_b)

if len(smallest_in_a) < len(smallest_in_b):
    print("class a has the smallest name",smallest_in_a)
if len(smallest_in_b) < len(smallest_in_a):
   print("class i has the smallest name",smallest_in_b)
#classes = [class_a,class_b] 
#for i in range(len(classes)):
 #for j in range(len(classes[i])):
           # print(classes[i][j])
