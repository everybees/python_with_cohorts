data={"example_two": 
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
	},

]
}


# def get_the_name_value():
# 	value_of_name=data["example_two"]
# 	for i in value_of_name:
# 		print(i["name"])
# get_the_name_value()


def get_the_blueberry():
	collect_value=data["example_two"]["batters"]["batter"]
	for i in collect_value:
		val=i["batter"]
		for j in val:
			if j["id"]=="1003":
				print(j["type"])
get_the_blueberry()
