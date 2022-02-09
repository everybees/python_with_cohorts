from multiprocessing.sharedctypes import Value


zombie = [
    {
        "f_name": "John",
        "l_name": "Doe",
        "siblings": ["Chi", "Emma"],
        "friends": [
            {
                "f_name": "Pet",
                "l_name": "Doe",
            },
            {
                "f_name": "Ife",
                "l_name": "Doe",
            }
        ]
    },
    {
        "f_name": "Dee",
        "l_name": "Doe",
        "siblings": ["Chi", "Emma"],
        "friends": [
            {
                "f_name": "Jane",
                "l_name": "Doe",
            },
            {
                "f_name": "Met",
                "l_name": "Doe",
            }
        ]
    }
]

for i in zombie:
    for key, value in i.items():
        print(key, "-->", value)

# for i in zombie.items():
#    if(zombie["f_name"] == "Dee"):
#        print(zombie["f_name"])
       
name = "iajadskl;lk,jusyuokpos.!kds"
name_j = name.replace(";", "")
print(name_j)