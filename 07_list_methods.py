my_friends = ["Robert", "Csilla", "Tamás"]

print(my_friends)

# add an item to the end of the list
my_friends.append("András")
print(my_friends)

# remove an item from the list
my_friends.remove("Robert")
print(my_friends)

# update item in a list
name_index = my_friends.index("András")
my_friends[name_index] = "Kiss Tamás"
print(my_friends)

# remove with index
name_index = my_friends.index("Kiss Tamás")
del my_friends[name_index]
print(my_friends)

# add two lists together
my_enemy_list = ["Sauron", "Darth Vader", "Voldemort"]
print(my_friends + my_enemy_list)