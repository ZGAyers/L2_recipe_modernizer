# Program Assembly - Full program

# modules to be used...
import csv
import re

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

def get_sf():
    serving_size = num_check("What is the recipe serving size? ")
    dodgy_sf = "yes"
    while dodgy_sf == "yes":

        desired_size = num_check("How many servings are needed? ")

        scale_factor = desired_size / serving_size

        if scale_factor < 0.25:
            dodgy_sf = input("Warning: This scale factor is very small and you "
                             "might struggle to accurately weigh the ingredients. \n"
                             "Do you want to fix this and make more servings? ").lower

        elif scale_factor > 4:
            dodgy_sf = input("Warning: This scale factor is quite large - you might "
                             "have issues with mixing bowl volumes and oven space \n"
                             "Do you want to fix this a make a smaller batch? ").lower

        else:
            dodgy_sf = "no"

    return scale_factor


def get_all_ingredients():
    all_ingredients = []

    stop = ""
    print("Please enter ingredients one line at a time. Press 'xxx' when you are done.")
    while stop != "xxx":

        # Ask user for ingredient (via not blank function)
        get_recipe_line = not_blank("Recipe Line: ",
                                   "This can't be blank",
                                   "yes")

        # If exit code is typed and there are more than 2 ingredients
        if get_recipe_line.lower() == "xxx" and len(all_ingredients) > 1:
            break

        elif get_recipe_line.lower() == "xxx" and len(all_ingredients) < 2:
            print("You need at least two more ingredients in the list. "
                  "Please add more ingredients.")

        # If exit code is not entered, add ingredients to list
        else:
            all_ingredients.append(get_recipe_line)

    return all_ingredients

# -- Main Routine --

# set up Dictionaries


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
scale_factor = get_sf()
print(scale_factor)

# Get amounts, units and ingredients from user
full_recipe = get_all_ingredients()


# Split each line of the recipe into amount, unit and ingredient...
mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

for recipe_line in full_recipe:
    recipe_line = recipe_line.strip()

    if re.match(mixed_regex, recipe_line):

        # Get mixed number by matching regex
        pre_mixed_num = re.match(mixed_regex, recipe_line)
        mixed_num = pre_mixed_num.group()

        # Replace space with a + sign...
        amount = mixed_num.replace(" ", "+")
        # Change the string into a decimal
        amount = eval(amount)

        # Get unit and ingredient
        compile_regrex = re.compile(mixed_regex)
        unit_ingredient = re.split(compile_regrex, recipe_line)
        unit_ingredient = (unit_ingredient[1]).strip()  # remove extra white space

    else:
        get_amount = recipe_line.split(" ", 1)

        try:
            amount = eval(get_amount[0])  # convert amount to float of possible
            amount = amount * scale_factor

        except NameError:
            amount = get_amount[0]
            modernised_recipe.append(recipe_line)
            continue

        unit_ingredient = get_amount[1]

    # Get unit and ingredient
    get_unit = unit_ingredient.split(" ", 1)  # splits text at first space

    unit = get_unit[0]
    # convert to ml
    num_spaces = recipe_line.count(" ")
    ingredient = get_unit[1]
    # convert to g

    modernised_recipe.append("{} {} {}".format(amount, unit, ingredient))


# Put updated ingredient in list


# Output ingredient list
for item in modernised_recipe:
    print(item)
