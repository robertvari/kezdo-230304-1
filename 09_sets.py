shop_a = {"csilla", "tamás", "kriszta", "csaba", "andi"}
shop_b = {"csaba", "andi", "norbi", "adrien", "vivien"}

# union
#print(shop_a | shop_b)

# difference
#print(shop_a - shop_b)
#print(shop_b - shop_a)

# intersection
print( shop_a & shop_b )

# symmetrical difference
print(shop_a ^ shop_b)

# add item to a set
shop_b.add("John")
print(shop_b)

# add multiple items to a set
shop_a.update(["Tom", "Chris", "Márta"])
print(shop_a)

# remove item from a set
shop_b.remove("John")
print(shop_b)