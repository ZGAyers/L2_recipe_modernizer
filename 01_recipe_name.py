# Component 1 - Get recipe name from user and check that it is valid


# Not Blank function goes here
def not_blank(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
           continue
        else:
            return response

# Main routine goes here
recipe_name = not_blank("What is the name of the recipe? ")

print("You are cooking {}".format(recipe_name))
