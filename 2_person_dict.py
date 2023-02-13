person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)  # prints the newly created dictionary


# name of second child
print(person["children"][1])  # to just get betty
print(
    type(person["children"])
)  # tells us what type of string it is (like maybe a list)
print(person["children"][1])

# the name of the cat
print(type(person["pets"]))  # verifies that it is a dict
print(person)

# use a fr loop
for i in person["children"]:
    print(i)

# type of pet: dog name of pet: Fido'
for i, j in person["pets"].items():
    print(f"Type of pet:{i} name of pet: {j}")
