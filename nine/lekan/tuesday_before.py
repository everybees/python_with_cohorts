from xmlrpc.client import boolean

data = {"colors": [
    {
        "color": "red",
        "value": "#f00"
    },
    {
        "color": "green",
        "value": "#0f0"
    },
    {
        "color": "blue",
        "value": "#00f"
    },
    {
        "color": "cyan",
        "value": "#0ff"
    },
    {
        "color": "magenta",
        "value": "#f0f"
    },
    {
        "color": "yellow",
        "value": "#ff0"
    },
    {
        "color": "black",
        "value": "#000"
    }
],

    "example_one": {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "ppu": 0.55,
        "batters":
            {
                "batter":
                    [
                        {"id": "1001", "type": "Regular"},
                        {"id": "1002", "type": "Chocolate"},
                        {"id": "1003", "type": "Blueberry"},
                        {"id": "1004", "type": "Devil's Food"}
                    ]
            },
        "topping":
            [
                {"id": "5001", "type": "None"},
                {"id": "5002", "type": "Glazed"},
                {"id": "5005", "type": "Sugar"},
                {"id": "5007", "type": "Powdered Sugar"},
                {"id": "5006", "type": "Chocolate with Sprinkles"},
                {"id": "5003", "type": "Chocolate"},
                {"id": "5004", "type": "Maple"},
            ]
    },
    "example_two": [
        {
            "id": "0001",
            "type": "donut",
            "name": "Cake",
            "ppu": 0.55,
            "batters":
                {
                    "batter":
                        [
                            {"id": "1001", "type": "Regular"},
                            {"id": "1002", "type": "Chocolate"},
                            {"id": "1003", "type": "Blueberry"},
                            {"id": "1004", "type": "Devil's Food"}
                        ]
                },
            "topping":
                [
                    {"id": "5001", "type": "None"},
                    {"id": "5002", "type": "Glazed"},
                    {"id": "5005", "type": "Sugar"},
                    {"id": "5007", "type": "Powdered Sugar"},
                    {"id": "5006", "type": "Chocolate with Sprinkles"},
                    {"id": "5003", "type": "Chocolate"},
                    {"id": "5004", "type": "Maple"}
                ]
        },
        {
            "id": "0002",
            "type": "donut",
            "name": "Raised",
            "ppu": 0.55,
            "batters":
                {
                    "batter":
                        [
                            {"id": "1001", "type": "Regular"}
                        ]
                },
            "topping":
                [
                    {"id": "5001", "type": "None"},
                    {"id": "5002", "type": "Glazed"},
                    {"id": "5005", "type": "Sugar"},
                    {"id": "5003", "type": "Chocolate"},
                    {"id": "5004", "type": "Maple"}
                ]
        },
        {
            "id": "0003",
            "type": "donut",
            "name": "Old Fashioned",
            "ppu": 0.55,
            "batters":
                {
                    "batter":
                        [
                            {"id": "1001", "type": "Regular"},
                            {"id": "1002", "type": "Chocolate"}
                        ]
                },
            "topping":
                [
                    {"id": "5001", "type": "None"},
                    {"id": "5002", "type": "Glazed"},
                    {"id": "5003", "type": "Chocolate"},
                    {"id": "5004", "type": "Maple"}
                ]
        }
    ],

    "example_three": {
        "id": "0001",
        "type": "donut",
        "name": "Cake",
        "image":
            {
                "url": "images/0001.jpg",
                "width": 200,
                "height": 200
            },
        "thumbnail":
            {
                "url": "images/thumbnails/0001.jpg",
                "width": 32,
                "height": 32
            }
    },

    "example_four": {
        "items":
            {
                "item":
                    [
                        {
                            "id": "0001",
                            "type": "donut",
                            "name": "Cake",
                            "ppu": 0.55,
                            "batters":
                                {
                                    "batter":
                                        [
                                            {"id": "1001", "type": "Regular"},
                                            {"id": "1002", "type": "Chocolate"},
                                            {"id": "1003", "type": "Blueberry"},
                                            {"id": "1004", "type": "Devil's Food"}
                                        ]
                                },
                            "topping":
                                [
                                    {"id": "5001", "type": "None"},
                                    {"id": "5002", "type": "Glazed"},
                                    {"id": "5005", "type": "Sugar"},
                                    {"id": "5007", "type": "Powdered Sugar"},
                                    {"id": "5006", "type": "Chocolate with Sprinkles"},
                                    {"id": "5003", "type": "Chocolate"},
                                    {"id": "5004", "type": "Maple"}
                                ]
                        }

                    ]
            }
    }
}


def get_f():
    print("The colours with #f are :")
    for i in range(len(data["colors"])):
        if data["colors"][i]["value"].__contains__("#f"):
            print(data['colors'][i]['color'])


def check_for_maple():
    for i in range(len(data["topping"])):
        if data["example_one"]["topping"][i]["type"].__contains__("Maple"):
            print("The Id of the maple is", data["example_one"]["topping"][i]["id"])


def check_for_batters_in_old_fashioned_donuts():
    for i in range(len(data["example_two"])):
        if data["example_two"][i]["name"].__contains__("Old Fashioned"):
            for x in range(2):
                print(data["example_two"][i]["batters"]["batter"][x]["type"])


def check_for_all_toppings():
    print("Type \t\t\t\t\t", "\t\t\t ID")
    for i in range(len(data["example_four"])):
        if data["example_four"]["items"]["item"][i]["topping"]:
            for k in range(len(data["example_four"]["items"]["item"][i]["topping"])):
                print(data["example_four"]["items"]["item"][i]["topping"][k]["type"], "\t                         \t", data["example_four"]["items"]["item"][i]["topping"][k]["id"])


def check_for_all_thumbnail():
    for i in range(len(data["example_three"])):
        if data["example_three"]["thumbnail"]:
            print(data["example_three"]["thumbnail"])



#
# get_f()
# print()
# check_for_maple()
# print()
# check_for_batters_in_old_fashioned_donuts()
# print()
# check_for_all_toppings()
# print()
check_for_all_thumbnail()

a_str = 'hello'
a_str[1] = 'r'
print(a_str)



