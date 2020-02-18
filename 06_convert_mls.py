# Component 6 - convert and check units


# - Functions -
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

# - main routine -
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

keep_going = ""
while keep_going == "":
    # ask user for amount
    amount = eval(input("How much? "))
    amount = float(amount)

    # ask user for Unit
    unit = unit_checker()

    # if unit is in dictionary, convert to mL
    if unit in unit_central:
        mult_by = unit_central.get(unit)
        amount = amount * mult_by
        print("Amount in mL {}".format(amount))

    # if no unit give / unit is unknown, leave as is
    else:
        print("{} is unchanged".format(amount))

    keep_going = input("<enter> or q: ")
