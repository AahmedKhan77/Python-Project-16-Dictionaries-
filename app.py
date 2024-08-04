customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["gender"] = "Male"
customer["name"] = 'Jack Smith'
print(customer["name"])
print(customer["gender"])
print(customer.get('birthday','Jan 1 1980'))
