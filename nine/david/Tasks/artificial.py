# create a value that holds 2 lists, those two lists should have dictionaries of several keys and values of different types



family = [
    {
        "Principal" : "Mr Dele",
        "Occupation" : ["Principal", "Real Estate", "Pure Water Factory"],
        "Age" : 58,
        "Gender": "Male",
        "Height": 5.7,
        "Complextion": "Dark",
        "Marital Status": "Married",
        "Children": 2,
        "Vehicles" : ["Toyota Venza", "Benz"]
    },
    {
        "Principals_wife" : "Mrs Angela",
        "Occupation": ["Vice Principal", "Trader", "Project manager", "House wife"],
        "Children": 2,
        "Age": "50",
        "Height": 5.7,
        "Complextion": "Fair",
        "Hobbies" : ["Singing", "Baking", "Cycing", "Gymnasium", "Beach"],
        "BestFriends" : ["Mrs Benson", "Mrs Olivia"],
        "vehicle" : ["Camry", "Honda Rx350"]
    }
]

def find():
    for lists in family:
        # lists = ["principal"]
        print(lists["Principal"])
find()
 
