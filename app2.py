phone = input("Phone: ")
digits = {
   "1": "One",
   "2": "Two",
   "3": "Three",
   "4": "Four"
}
output = ""
for ch in phone:
    output += digits.get(ch,"!") + " "
print(output)