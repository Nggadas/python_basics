# TREE-HOUSE SOLUTION

# make a list to hold onto our items
shopping_list = []

# print out instructions on how to use the app
print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break

    # add new items to our list
    shopping_list.append(new_item)
# print out the list
print("Here's your list:")

for item in shopping_list:
    print(item)


# MY ATTEMPT

# shopping_list = []
# add_item = True
#
# while add_item:
#
#     user_input = input("Add item to shopping list or type 'Done' to quit: ")
#
#     if user_input.upper() == "DONE":
#         print("**********Shopping List**********")
#         print(shopping_list)
#         add_item = False
#         break
#     else:
#         shopping_list += user_input