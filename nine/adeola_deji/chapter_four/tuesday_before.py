data = {
    "colors": 
        [
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
                        { "id": "1001", "type": "Regular" },
                        { "id": "1002", "type": "Chocolate" },
                        { "id": "1003", "type": "Blueberry" },
                        { "id": "1004", "type": "Devil's Food" }
                    ]
            },
        "topping":
            [
                { "id": "5001", "type": "None" },
                { "id": "5002", "type": "Glazed" },
                { "id": "5005", "type": "Sugar" },
                { "id": "5007", "type": "Powdered Sugar" },
                { "id": "5006", "type": "Chocolate with Sprinkles" },
                { "id": "5003", "type": "Chocolate" },
                { "id": "5004", "type": "Maple" }
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
                                { "id": "1001", "type": "Regular" },
                                { "id": "1002", "type": "Chocolate" },
                                { "id": "1003", "type": "Blueberry" },
                                { "id": "1004", "type": "Devil's Food" }
                            ]
                    },
                "topping":
                    [
                        { "id": "5001", "type": "None" },
                        { "id": "5002", "type": "Glazed" },
                        { "id": "5005", "type": "Sugar" },
                        { "id": "5007", "type": "Powdered Sugar" },
                        { "id": "5006", "type": "Chocolate with Sprinkles" },
                        { "id": "5003", "type": "Chocolate" },
                        { "id": "5004", "type": "Maple" }
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
                                { "id": "1001", "type": "Regular" }
                            ]
                    },
                "topping":
                    [
                        { "id": "5001", "type": "None" },
                        { "id": "5002", "type": "Glazed" },
                        { "id": "5005", "type": "Sugar" },
                        { "id": "5003", "type": "Chocolate" },
                        { "id": "5004", "type": "Maple" }
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
                                { "id": "1001", "type": "Regular" },
                                { "id": "1002", "type": "Chocolate" }
                            ]
                    },
                "topping":
                    [
                        { "id": "5001", "type": "None" },
                        { "id": "5002", "type": "Glazed" },
                        { "id": "5003", "type": "Chocolate" },
                        { "id": "5004", "type": "Maple" }
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
                                            { "id": "1001", "type": "Regular" },
                                            { "id": "1002", "type": "Chocolate" },
                                            { "id": "1003", "type": "Blueberry" },
                                            { "id": "1004", "type": "Devil's Food" }
                                        ]
                                },
                            "topping":
                                [
                                    { "id": "5001", "type": "None" },
                                    { "id": "5002", "type": "Glazed" },
                                    { "id": "5005", "type": "Sugar" },
                                    { "id": "5007", "type": "Powdered Sugar" },
                                    { "id": "5006", "type": "Chocolate with Sprinkles" },
                                    { "id": "5003", "type": "Chocolate" },
                                    { "id": "5004", "type": "Maple" }
                                ]
                        }

                    ]
            }
    }
}


def check_for_color_f():
    color_data = data["colors"]
    print("The functions that have #f are: ")
    for i in color_data:
        if i["value"].__contains__("#f"):
            print(i["color"])
# check_for_color_f()
print()


def check_for_maple():
    example_one_toppings = data["example_one"]["topping"]
    for i in example_one_toppings:
        if i["type"] == "Maple":
            print("id of maple is:", i["id"])
check_for_maple()
print()


def check_for_donut():
    example_two = data["example_two"]
    for i in example_two:
        if i["name"] == "Old Fashioned":
            batters_in_batter =i["batters"]["batter"]
            print("Batter types used in making old fashioned donut are: ")
            for i in batters_in_batter:
                print(i["type"])
# check_for_donut()
print()


def toppings_available():
    example_four =data["example_four"]["items"]["item"][0]["topping"]
    print("All toppings in example four are: ")
    for i in example_four:
        print(i["type"])
# toppings_available()