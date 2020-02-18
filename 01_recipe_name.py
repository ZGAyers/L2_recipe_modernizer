# Component 1 - Get recipe name from user and check that it is valid


# Not Blank function goes here
def not_blank(question):
    error = "Your recipe name has numbers in it."

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        for letter in response:
            if letter.isdigit() == True:
                has_errors = "yes"
                continue

        if response == "":
            continue

        elif has_errors != "":
            print(error)
            continue

        else:
            return response

# Main routine goes here
recipe_name = not_blank("What is the name of the recipe? ")

print("You're cooking {}".format(recipe_name))
