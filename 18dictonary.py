#Dictonary

customer = {
    "name":"Choudhary",
    "age":30,
    "is_verified":True
}

print customer.get("name")

#key error if looking for key which don't exists and it is case sencitive
print customer["name"]

#if key don't have value then we can supply a default value
print customer.get("birthdate", "Jan 1 1997")

customer["name"] = "CS Choudhary"

customer["birthdate"] = "20 May 92"


print customer

print "----------------------------------Assignment----------------------------------------"

numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}

input_number = raw_input("Phone : ")
output = ""
for degit in input_number:
    output += numbers.get(int(degit), "!")+ " "

print output








