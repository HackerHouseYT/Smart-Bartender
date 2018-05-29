# drinks.py
drink_list = [
	{
		"name": "Blue & Red - 50ml",
		"ingredients": {
			"blue": 50,
			"red": 50
		}
	}, {
		"name": "Green & Yellow - 50ml",
		"ingredients": {
			"green": 50,
			"yellow": 50
		}
	}, {
		"name": "All - 50ml",
		"ingredients": {
			"green": 50,
			"yellow": 50,
			"blue": 50,
			"red": 50,
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
	{"name": "Blue", "value": "blue"}
]
