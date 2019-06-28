first_name = input("What is your first name?  ")
print("Hello,", first_name)

if first_name == "John":
    print(first_name, "is learning Python")
elif first_name == "Jane":
    print(first_name, "is learning with fellow students in the community!")
else:
    print("You should totally learn Python, {}!".format(first_name))


print("have a great day {}!".format(first_name))