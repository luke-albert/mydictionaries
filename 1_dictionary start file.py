import random

phonebook = {}
phonebook = {"Chris": "555−1111", "Katie": "555−2222", "Joanne": "555−3333"}

mydictionary = dict(m=8, n=9)  # creates a dictonary

print(mydictionary)

print(f"Number of key value pairs: {len(phonebook)}")  # len prints the number of keys

"""

print()
print("*****  start section 1 - print dictionary ********")
print()





print()
print('*****  end section 1 ********')
print()





print()
print("*****  start section 2 - search dictionary ********")
print()


name = "chris" #case sensitive

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} does not exist in the phonebook")


print()
print("*****  end section 2 ********")
print()





print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

phonebook["Chris"] = "555-4444"

phonebook["Joe"] = "555-0123"

print(phonebook) #will print the updated version


print()
print("*****  end section 3 ********")
print()





print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

print(phonebook)
del phonebook["Chris"] #deletes everything about Chris (key and value)
print(phonebook)


print()
print("*****  end section 4 ********")
print()




print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()

for key in phonebook:
    print(
        f"The key is: {key} and the value {phonebook[key]}"
    )  # will iterate through each key

for value in phonebook.values():
    print(value)  # just the values for each key

for k, v in phonebook.items():
    print(f"The key is: {k} and the value is {v}")  # iterates through each key

for ph_tuple in phonebook.items():  # make it a tuple (3 separate tuples for each key)
    print(ph_tuple)


print()
print("*****  end section 5 ********")
print()





print()
print("*****  start section 6 - using get and clear ********")
print()

name = "Chris"

phone = phonebook.get(name, "key not found") # will print "key not found" if it doesnt find it (it is very case sensitive)

print(phone)  


phonebook.clear()

print(phonebook)

print()
print("*****  end section 6 ********")
print()



print()
print("*****  start section 7 - using pop method ********")
print()


remove = phonebook.pop("Chris", "not found") #removes key and value

print(remove) #what is getting removed
print(phonebook) #the new updated phonebook

print()
print("*****  end section 7 ********")
print()



print()
print("*****  start section 8 - using popitem ********")
print()


a = phonebook.popitem()  # pops out the last item

print(a)

print(phonebook)


print()
print("*****  end section 8 ********")
print()



print()
print("*****  start section 9 - using random and converting to list ********")
print()

list_of_keys = list(
    phonebook
)  # making a list of the dictionary just makes a list of the keys
random_key = random.choice(list_of_keys)  # give you a name(key) randomly at a time
print(random_key)
print(phonebook[random_key])  # gives you random name along with their phone number

print(
    phonebook[random.choice(list(phonebook))]
)  # same thing as above but in just one line; this is more efficient


print()
print("*****  end section 9 ********")
print()

"""
