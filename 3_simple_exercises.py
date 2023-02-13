# 1) print out the value for the key 'history' using the dictionary below


sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}

score = sampleDict["class"]["student"]["marks"][
    "history"
]  # this is how to drill down in a nested dictionary
print(score)  # will print jsut the score which is 80


# 2) Add 2 inches to the son's height. (not hardcoded value because they didnt give a specific value)

dict = {
    "son's name": "Lucas",
    "son's eyes": "green",
    "son's height": 32,
    "son's weight": 25,
}

dict["son's height"] += 2
print(dict)


# 3) Given a Python dictionary, Change Brad’s salary to 8500 (we know this is a hardcoded value)

sampleDict = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 6500},
}

sampleDict["emp3"]["salary"] = 8500
print(sampleDict)


# 4 )Given the dictionary below, add a new key - 'work' with the values shown below:
#       "work": ["Apology", "Phaedo", "Republic", "Symposium"]

dict = {
    "name": "Plato",
    "country": "Ancient Greece",
    "born": -427,
    "teacher": "Socrates",
    "student": "Aristotle",
}


dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict)
