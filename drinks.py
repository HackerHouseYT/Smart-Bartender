# drinks.py
drink_list = [
	{
		"name": "Blue & Red \n- 50ml",
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
			"water": 50,
			"milk": 50,
			"orange juice": 50,
			"cranberry juice": 50
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
	{"name": "Water", "value": "water"},
	{"name": "Milk", "value": "milk"},
	{"name": "Orange Juice", "value": "orange juice"},
	{"name": "Cranberry Juice", "value": "cranberry juice"}
]
