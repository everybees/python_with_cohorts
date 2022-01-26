import  pprint

message= 'It will be really great if we can all be disciplined'
ourDictionary={}

for theLetters in message:
    ourDictionary.setdefault(theLetters, 1)
    ourDictionary[theLetters]=ourDictionary[theLetters]+2



print(ourDictionary)


































 #ourDictionary.setdefault(theLetters, 0)
#ourDictionary[theLetters]=ourDictionary[theLetters]+10


#print(ourDictionary)







































# dictionary={}
#
# for elements in message:
#     dictionary.setdefault(elements, 0)
#     dictionary[elements]=dictionary[elements]+3
#
#
# print( dictionary)































































































# dictionary={}
#
# for elements in message:
#     dictionary.setdefault(elements, 0)
#     dictionary[elements]=dictionary[elements]+1
#
#
#
# # pp = pprint.PrettyPrinter(indent=1)
# # pp.pprint(dictionary)
#
# print(dictionary)
#
#




















# dictionary(message)
# pprint(message)























