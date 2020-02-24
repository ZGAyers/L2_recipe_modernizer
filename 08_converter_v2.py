# Component 08 v2- combine component 7 and component 8
# import food dictionary spreadsheet
import csv

# --- Functions ---
def general_converter(how_much, lookup, dictionary, conversion_factor):
    # if unit is in dictionary, convert to mL
    if lookup in dictionary:
        mult_by = dictionary.get(lookup)
        how_much = how_much * float(mult_by) * conversion_factor
        converted = "yes"
    else:
        converted = "no"

    return [how_much, converted]


def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t", "teaspoons"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp", "tablespoons"]
    cup = ["cup", "c", "cups"]
    ounce = ["oz", "ounces", "fl oz", "ounce"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    mls = ["ml", "milliliter", "millilitre", "milliliters", "millilitres"]
    litre = ["litre", "liter", "l", "litres", "liters"]
    pound = ["pound", "lb", "#", "pounds"]
    grams = ["g", "gram", "grams"]

    if unit_tocheck == "":
        return unit_tocheck
    elif unit_tocheck.lower() in grams:
        return "g"
    elif unit_tocheck == "T" or unit_tocheck.lower() in tablespoon:
        return "tbs"
    elif unit_tocheck.lower() in teaspoon:
        return "tsp"
    elif unit_tocheck.lower() in cup:
        return "cup"
    elif unit_tocheck.lower() in ounce:
        return "ounce"
    elif unit_tocheck.lower() in pint:
        return "pint"
    elif unit_tocheck.lower() in quart:
        return "quart"
    elif unit_tocheck.lower() in mls:
        return "mls"
    elif unit_tocheck.lower() in litre:
        return "litre"
    elif unit_tocheck.lower() in pound:
        return "pound"


# --- Main Routine ---

# dictionaries go here
unit_central = {
    "tsp": 5,
    "tbs": 15,
    "cup": 237,
    "ounce": 28.35,
    "pint": 473,
    "quart": 946,
    "pound": 454,
    "litre": 1000,
    "ml": 1
}
# Generate food dictionary
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

# --- Get Items ---
keep_going = ""
while keep_going == "":
    amount = eval(input("How much? "))
    amount = float(amount)

    # Get unit and change it to match dictionary
    unit = unit_checker()
    ingredient = input("Ingredient: ")

    # Convert to mls if possible
    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    # if unit is in dictionary, convert to mL
    if amount[1] == "yes":
        amount_2 = general_converter(amount[0], ingredient, food_dictionary, 250)

        # if the ingredient is in the list convert it
        if amount_2[1] == "yes":
            print(amount_2)

    # if no ingredient give / ingredient is unknown, leave as is
    else:
        print("{} is unchanged".format(amount))

    # option to end loop and exit program
    keep_going = input("<enter> or q: ")
