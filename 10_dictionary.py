phonebook = {
    "06 20 111 2233": {"name": "Csaba", "address": "Budapest"},
    "06 30 111 2233": {"name": "Kriszta", "address": "Pécs"},
    "06 30 222 3344": {"name": "Tamás", "address": "Debrecen"}
}

print(  phonebook["06 20 111 2233"]  )
print(  phonebook["06 20 111 2233"]["name"]  )
print(  phonebook["06 20 111 2233"]["address"]  )

shop_members = {
    1: {"name": "Csaba", "address": "Budapest", "phone": "06 20 111 3322"},
    2: {"name": "Kriszta", "address": "Pécs", "phone": "06 20 888 3322"}
}