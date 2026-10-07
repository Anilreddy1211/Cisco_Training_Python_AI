import pprint

# =========================================================
# 1. DICTIONARY OF LISTS
# =========================================================

print("1. DICTIONARY OF LISTS")
print("-" * 30)

products = {}

products['id'] = [101, 102, 103]
products['names'] = ['pA', 'pB', 'pC']
products['cost'] = [1000, 2000, 3000]
products['Qty'] = [10, 20, 30]

pprint.pprint(products)

print("\nFirst Product:")
print("ID:", products['id'][0])
print("Name:", products['names'][0])
print("Cost:", products['cost'][0])
print("Quantity:", products['Qty'][0])

print("\nAll Products:")

for i in range(len(products['id'])):
    print(
        f"ID: {products['id'][i]}, "
        f"Name: {products['names'][i]}, "
        f"Cost: {products['cost'][i]}, "
        f"Quantity: {products['Qty'][i]}"
    )


# =========================================================
# 2. LIST OF DICTIONARIES
# =========================================================

print("\n\n2. LIST OF DICTIONARIES")
print("-" * 30)

products = []

products.append({
    'id': 101,
    'name': 'pA',
    'cost': 1000,
    'Qty': 10
})

products.append({
    'id': 102,
    'name': 'pB',
    'cost': 2000,
    'Qty': 20
})

products.append({
    'id': 103,
    'name': 'pC',
    'cost': 3000,
    'Qty': 30
})

pprint.pprint(products)

print("\nFirst Product:")
print("ID:", products[0]['id'])
print("Name:", products[0]['name'])
print("Cost:", products[0]['cost'])
print("Quantity:", products[0]['Qty'])

print("\nAll Products:")

for product in products:
    print(
        f"ID: {product['id']}, "
        f"Name: {product['name']}, "
        f"Cost: {product['cost']}, "
        f"Quantity: {product['Qty']}"
    )


# =========================================================
# 3. DICTIONARY OF DICTIONARIES
# =========================================================

print("\n\n3. DICTIONARY OF DICTIONARIES")
print("-" * 30)

products = {}

products['id'] = {
    'id1': 101,
    'id2': 102,
    'id3': 103
}

products['names'] = {
    'name1': 'pA',
    'name2': 'pB',
    'name3': 'pC'
}

products['cost'] = {
    'cost1': 1000,
    'cost2': 2000,
    'cost3': 3000
}

products['Qty'] = {
    'Qty1': 10,
    'Qty2': 20,
    'Qty3': 30
}

pprint.pprint(products)

print("\nAccessing Data:")

print("ID:", products['id']['id1'])
print("Name:", products['names']['name1'])
print("Cost:", products['cost']['cost1'])
print("Quantity:", products['Qty']['Qty1'])


# =========================================================
# 4. DICTIONARY KEYED BY PRODUCT ID
# =========================================================

print("\n\n4. DICTIONARY KEYED BY PRODUCT ID")
print("-" * 30)

products = {
    101: {
        'name': 'pA',
        'cost': 1000,
        'Qty': 10
    },

    102: {
        'name': 'pB',
        'cost': 2000,
        'Qty': 20
    },

    103: {
        'name': 'pC',
        'cost': 3000,
        'Qty': 30
    }
}

pprint.pprint(products)

print("\nAccess Product 102:")

print("Name:", products[102]['name'])
print("Cost:", products[102]['cost'])
print("Quantity:", products[102]['Qty'])


# =========================================================
# LOOP THROUGH DICTIONARY
# =========================================================

print("\nAll Products:")

for product_id, details in products.items():

    print(
        f"ID: {product_id}, "
        f"Name: {details['name']}, "
        f"Cost: {details['cost']}, "
        f"Quantity: {details['Qty']}"
    )


# =========================================================
# UPDATE PRODUCT
# =========================================================

print("\nUpdating Product 102...")

products[102]['cost'] = 2500
products[102]['Qty'] = 25

print("\nUpdated Product 102:")
pprint.pprint(products[102])


# =========================================================
# ADD NEW PRODUCT
# =========================================================

print("\nAdding New Product...")

products[104] = {
    'name': 'pD',
    'cost': 4000,
    'Qty': 40
}

print("\nUpdated Products:")
pprint.pprint(products)


# =========================================================
# SEARCH PRODUCT
# =========================================================

print("\nSearching Product...")

product_id = 103

if product_id in products:
    print("Product Found!")
    pprint.pprint(products[product_id])
else:
    print("Product Not Found")


# =========================================================
# DELETE PRODUCT
# =========================================================

print("\nDeleting Product 104...")

if 104 in products:
    products.pop(104)

print("\nFinal Products:")
pprint.pprint(products)
