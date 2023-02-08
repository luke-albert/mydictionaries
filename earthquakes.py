"""
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""


import json

infile = open("eq_data.json", "r")

earthquakes = json.load(infile)

# 1) print out the number of earthquakes
print("Number of earthqakes:", len(earthquakes["features"]))
print()

a = 1
eq_dict = {}


# 2) iterate through the dictionary


for earthquake in earthquakes["features"]:
    if earthquake["properties"]["mag"] > 6:

        eq_dict[a] = [
            earthquake["properties"]["place"],
            earthquake["properties"]["mag"],
            earthquake["geometry"]["coordinates"][0],
            earthquake["geometry"]["coordinates"][1],
        ]

        a += 1

print(eq_dict)


# 3) using the eq_dict dictionary, print out the information as shown below (first three shown):


print()

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

for element in list1:
    print("Location:", eq_dict[element][0])
    print("Magnitude:", eq_dict[element][1])
    print("Longitude:", eq_dict[element][2])
    print("Latitude:", eq_dict[element][3])
    print()
