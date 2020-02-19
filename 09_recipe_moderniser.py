# Program Assembly - Full program

# modules to be used...
import csv

# --- Functions ---


# Not Blank function goes here
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue

        elif has_errors != "":
            print(error)
            continue

        else:
            return response


# Number Checking Function goes here
def num_check(question):

    error = "Please enter a number that is more than zero"

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def general_converter(how_much, lookup, dictionary, conversion_factor):
    # if unit is in dictionary, convert to mL
    if lookup in dictionary:
        mult_by = dictionary.get(unit)
        how_much = how_much * mult_by * conversion_factor

    return how_much


def unit_checker():

    unit_tocheck = input("Unit? ")

    # Abbreviation lists
    teaspoon = ["tsp", "teaspoon", "t"]
    tablespoon = ["tbs", "tablespoon", "T", "tbsp"]
    cup = ["cup", "c", "cups"]
    ounce = ["oz", "ounces", "fl oz", "ounce"]
    pint = ["p", "pt", "fl pt", "pint", "pints"]
    quart = ["q", "qt", "fl qt", "quart", "quarts"]
    mls = ["ml", "milliliter", "millilitre", "milliliters", "millilitres"]
    litre = ["litre", "liter", "l", "litres", "liters"]
    pound = ["pound", "lb", "#", "pounds"]
    grams = ["g", "gram", "grams"]

    if unit_tocheck == "":
        print("you chose {}".format(unit_tocheck))
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


# -- Main Routine --

# set up Dictionaries
# open food dictionary
groceries = open('01_ingredients_ml_to_g.csv')
# Read data into a list
csv_groceries = csv.reader(groceries)
# Create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key, next is definition)

for row in csv_groceries:
    food_dictionary[row[0]] = row[1]
# set up list to hold 'modernised' ingredients
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

# Ask user for recipe name and check its not blank
recipe_name = not_blank("What is the recipe name? ",
                   "The recipe can't be blank and can't contain numbers, ",
                   "no")

# Ask user where the recipe is originally from (numbers ok)
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank, ",
                   "yes")
# Get serving sizes and scale factor
serving_size = num_check("What is the recipe serving size? ")
dodgy_sf = "yes"
while dodgy_sf == "yes":

    desired_size = num_check("How many servings do you need? ")

    scale_factor = desired_size / serving_size

    if scale_factor < 0.25:
        print(scale_factor)
        dodgy_sf = input("Warning: This scale factor is very small and you "
                         "might struggle to accurately weigh the ingredients. \n"
                         "Do you want to fix this and make more servings? ").lower

    elif scale_factor > 4:
        print(scale_factor)
        dodgy_sf = input("Warning: This scale factor is quite large - you might "
                         "have issues with mixing bowl volumes and oven space \n"
                         "Do you want to fix this a make a smaller batch? ").lower

    else:
        dodgy_sf = "no"

# Loop for each ingredient
keep_going = ""
while keep_going == "":
    # Get ingredient name
    ingredient = not_blank("Please enter a ingredient name: ",
                           "This can't be blank",
                           "yes")
    if ingredient.lower() == "xxx":
        break
    # Get ingredient amount
    amount = num_check("What is the amount of this ingredient? ")

    # Get unit
    unit = unit_checker()

    # Convert unit to ml
    amount = general_converter(amount, unit, unit_central, 1)
    print(amount)

    # Convert from ml to g
    if ingredient in food_dictionary:
        mult_by = food_dictionary.get(ingredient)
        amount = amount * float(mult_by) / 250
        print("Amount in g {}".format(amount))

    # if no ingredient give / ingredient is unknown, leave as is
    else:
        print("{} is unchanged".format(amount))

    # Put updates ingredient in list
        print("Amount in mL {}".format(amount))
        print("Amount in g {}".format(amount))


# Output ingredient list
