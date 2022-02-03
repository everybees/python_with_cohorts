import json


with open('nine/adeola_deji/chapter_four/user_data.json') as json_file:
    data = json.load(json_file)
    print(data)
    # prints all the individual data
    # for i in data:
    #     print(i, end="")
    #     print()
    #     print()
    #     print("....")

    # looping and printing key and value i.e tuple unpacking
    # for i in data:
    #     for key in i:
    #         print(key, "-->", i[key])
    #     print()
    #     print()

    # using the .items() fxn
    # for i in data:
    #     for item in i.items():
    #         print(item)
    #     print()

    # Printing keys and values using the .keys() and .values() fxn
    # for i in data:
    #     print(i.keys())
    #     print()
    #     print(i.values())
    #     print()
    #     print()

    # checking for desired values
    # for i in data:
    #     if str(i["id"]).__contains__("1"):
    #         print(i["id"], "==>", i["login"])
    #         print()

    






    
        

    