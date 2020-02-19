# Component 09 - ingredient splitter
import re

# ingredient has mixed fraction followed by unit and ingredient
recipe_line = "1 1/2 ml flour" # change to input statement in due course

mixed_regex = "\d{1,3}\s\d{1,3}\/\d{1,3}"

if re.match(mixed_regex, recipe_line):
    print("true")
    # Get mixed number by matching regex
    pre_mixed_num = re.match(mixed_regex, recipe_line)
    mixed_num = pre_mixed_num.group()

    # Replace space with a + sign...
    amount = mixed_num.replace(" ", "+")
    # Change the string into a decimal
    amount = eval(amount)
    print(amount)

    # Get unit and ingredient
    compile_regrex = re.compile(mixed_regex)
    print(compile_regrex)
    unit_ingredient = re.split(compile_regrex, recipe_line)
    unit_ingredient = (unit_ingredient[1]).strip() # remove extra white space
    print(unit_ingredient)

get_unit = unit_ingredient.split(" ", 1) # splits text at first space
print(get_unit)

unit = get_unit[0]
ingredient = get_unit[1]