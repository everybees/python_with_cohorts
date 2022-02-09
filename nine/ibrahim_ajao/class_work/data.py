data_style = {"colors": [
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
                {"id": "5004", "type": "Maple"}
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


def color_printing_key_sign(input):
    result = input["colors"]
    for j in result:
        if j["value"].__contains__("#f"):
            print(j["color"])


def example_one_all_topping_maple(input):
    result = input["example_one"]["topping"]
    for i in result:
        if i["type"] == "Maple":
            print(i["id"])


def old_fashion_donut(input):
    result = input["example_two"][2]["batters"]["batter"]
    for i in range(2):
        print(result[i]["type"])


def example_four_topping(input):
    result = input["example_four"]["items"]["item"][0]["topping"]
    for i in range(len(result)):
        print(result[i]["type"])


color_printing_key_sign(data_style)
print()
example_one_all_topping_maple(data_style)
print()
old_fashion_donut(data_style)
print()
example_four_topping(data_style)
print()