phonebook = {
    "06 20 111 2233": {"name": "Csaba", "address": "Budapest"},
    "06 30 111 2233": {"name": "Kriszta", "address": "Pécs"},
    "06 30 222 3344": {"name": "Tamás", "address": "Debrecen"}
}

# update existing item
phonebook["06 20 111 2233"] = "Peti"

# add new item to a dictionary
phonebook["06 70 111 2233"] = "Kriszta"

# remove an item
del phonebook["06 20 111 2233"]