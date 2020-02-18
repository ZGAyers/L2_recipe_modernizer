# Component 7 - convert measurement to grams

# import food dictionary spreadsheet
import csv

# open file
groceries = open('01_ingredients_ml_to_g.csv')
# Read data into a list
csv_groceries = csv.reader(groceries)
# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key, next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]

print(food_dictionary)

# loop code for testing purposes
keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    # Get the ingredient and change it to match dictionary
    ingredient = input("Ingredient: ").lower()

    # if unit is in dictionary, convert to mL
    if ingredient in food_dictionary:
        mult_by = food_dictionary.get(ingredient)
        amount = amount * float(mult_by) / 250
        print("Amount in g {}".format(amount))

    # if no ingredient give / ingredient is unknown, leave as is
    else:
        print("{} is unchanged".format(amount))

    # option to end loop and exit program
    keep_going = input("<enter> or q: ")
