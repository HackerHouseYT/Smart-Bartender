# drinks.py
drink_list = [
	{
		"name": "Mojito",
		"ingredients": {
			"yellow": 500
		}
	},{
		"name": "Gin/EmergenC",
		"ingredients": {
			"orange": 200,
			"indigo": 25
		}
	}, {
		"name": "Martini",
		"ingredients": {
			"green": 50,
			"yellow": 50
		}
	}, {
		"name": "Rush Beta",
		"ingredients": {
			"green": 50,
			"yellow": 50,
			"blue": 50,
			"red": 50,
			"orange": 50,
			"indigo": 50,
			"violet": 50,
			"pink": 50
		}
	},
	#test edge - no fluid at all
	{
		"name": "All - 0ml",
		"ingredients": {
			"green": 0,
			"yellow": 0,
			"blue": 0,
			"red": 0,
		}
	},
	
]

drink_options = [
	{"name": "Green", "value": "green"},
	{"name": "Yellow", "value": "yellow"},
	{"name": "Red", "value": "red"},
	{"name": "Blue", "value": "blue"},
	{"name": "Orange", "value": "orange"},
	{"name": "Indigo", "value": "indigo"},
	{"name": "Orange Juice", "value": "orange juice"},
	{"name": "Cranberry Juice", "value": "cranberry juice"}
]
