### Challenge: How many drinks do you need to buy to throw a great party? 
# you will have a list of your friends, and their favorite drink. 
# you will also know how many drinks of a certain type are drunk per hour


#list of your friends and their favorite drink
favorite_drinks = {'Adam':'Gin and Tonic','Angela':'Mate Vodka','Sven':'Whiskey','Alexandra':'Whiskey',
                    'Michael':'White Wine','Ariana':'Gin and Tonic','Thomas':'Beer','Eduardo':'White Wine',
                    'Leanne':'Red Wine', 'Karla':'Whiskey', 'Taylor': 'Mate Vodka','Jonathan':'Water'}


#types of drinks people drink, with lists of examples
cocktails = ['Gin and Tonic', 'Mate Vodka', 'Rum and Coke']

wines = ['Red Wine', 'White Wine']

liquors = ['Whiskey', 'Gin', 'Vokda']

nonalcoholic = ['Tea', 'Water', 'Orange juice']

beers = ["Beer"]



# number of drinks per hour people drink, depeneding on the type. 
number_of_drinks_per_hour_per_type = {'cocktails':1, 'beers':3,'wines':2,'liquors':2,'nonalcoholic':3}
def party_calculator():
	cocktails_count = 0
	wine_count = 0
	liquoer_count = 0
	nonalcoholic_count = 0
	beercount = 0

	for key, value in favorite_drinks.items():
		if value in cocktails:
			cocktails_count += 1 * number_of_drinks_per_hour_per_type["cocktails"] * 6
		elif value in wines:
			wine_count += 1 * number_of_drinks_per_hour_per_type["wines"] * 6
		elif value in liquors:
			liquoer_count += 1 * number_of_drinks_per_hour_per_type["liquors"] * 6
		elif value in nonalcoholic:
			nonalcoholic_count += 1 * number_of_drinks_per_hour_per_type["nonalcoholic"] * 6
		elif value in beers:
			beercount += 1 * number_of_drinks_per_hour_per_type["beers"] * 6
		else:
			print(value)

	print(cocktails_count, "Cocktails")
	print(wine_count, "Wines")
	print(liquoer_count, "Liquers")
	print(nonalcoholic_count, "Softdrinks")
	print(beercount, "Beers")


party_calculator()



