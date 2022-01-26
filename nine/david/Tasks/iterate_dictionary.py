# guy.keys() #to get all the keys in a dictionary
# guy.values() # to get all the values in a dictionary

# for key, values in guy.items():
    # print(key, value) to iterate and get both the keys and values in a dictionary

# guy = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "siblings": ["Bola", "mobile", "Kennedy", "Jameson", "Postman"],
#     "coohort": 1,
#     "friend_list": ""
# }

name = "Nobody expects the spanish inquisition! and you?!"

name = name.lower()
name = name.strip("?", "!")
name = name.strip("!", "")
print(name)