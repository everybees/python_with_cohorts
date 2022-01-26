print('FOOD ARRAY')
#
print()
#
x =['Bananas','Oranges','Mangoes']
y = ['Bread','Eggs','Tomatoes']
z = ['Rice','Beans','Yams']

food = [x,y,z]
# for row in range(3):
#     for col in range(3):
#         print(food[row][col],end='\t')
#     print()
#
# #
# print()
# #
# for row in range(3):
#     for col in range(3):
#         print(food[col][row])
# #
# print()
# #
# for col in range(3):
#     for row in range(3):
#         print(food[col][row],'\t[{}][{}]'.format(col,row))
# #
# print()
#
# row = 2
# while row >= 0:
#     col = 2
#     while col >= 0:
#         print(food[col][row])
#         col-=1
#     row -= 1
# #
# print()
# #
# sn =1
# print('S/N\t\tfood item\tPosition')
# for col in range(3):
#     for row in range(3):
#         print('{}.\t\t{}\t\t{}'.format(sn,food[col][row],[col,row]))
#         sn +=1
# #
# print()
# #
# count =0
# print('S/N\t\tfood item\tPosition')
# for col in range(2,-1,-1):
#     for row in range(2,-1,-1):
#         count += 1
#         print(count,end='\t\t')
#         print(food[row][col],end='\t\t')
#         print(row,col,end='\n')
#
# #
# print()
# #
# count =0
# print('S/N\t\tfood item\tPosition')
# for row in range(2,-1,-1):
#     for col in range(2,-1,-1):
#         count += 1
#         print(count,end='\t\t')
#         print(food[row][col],end='\t\t')
#         print(row,col,end='\n')
