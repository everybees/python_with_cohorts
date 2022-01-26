grossaries= {'soup':9000, 'stew':4000}

print('I sent you to get ' + str(grossaries.get('soup')) +' worth of soup ingredients' + 'and ' + str(grossaries.get('stew')) + ' worth of stew. Thank you. ')


grossaries.setdefault('t-fare', '9000a')
print(grossaries)





print()
print()
print()


message= 'I want to eat bread'
dictionary={}

for letters in message:
    dictionary.setdefault(letters, 'okay')


print(dictionary)






























# message ='it is so great having you speak with us today'
# count ={}
#
# for character in message:
#     count.setdefault(character, 0)
#     count[character]=count[character]+1
#
# print(count)
#































































# grossaries.setdefault('fastFoods', '6000')
#
# print(grossaries)



































































#
# spam={'food':200, 'water':500}
# print('Please get me ' + str(spam.get('food', 0)) +' quantity of food')














































# picnicItem={'apples':5, 'cups':4 }
#
# print('I am giving ' +str(picnicItem.get('cups', 0))+'cups')