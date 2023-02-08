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
print(len(earthquakes["features"]))
print()


# 2) iterate through the dictionary
for earthquake in earthquakes["features"]:
    if earthquake["properties"]["mag"] > 6:
        eq_dict = {}
        eq_dict["Location"] = earthquake["properties"]["place"]
        eq_dict["Magnitude"] = earthquake["properties"]["mag"]
        eq_dict["Longitude"] = earthquake["geometry"]["coordinates"][0]
        eq_dict["Latitude"] = earthquake["geometry"]["coordinates"][1]

        print(eq_dict)

# 3) using the eq_dict dictionary, print out the information as shown below (first three shown):

"""
for earthquake in earthquakes["features"]:
    if earthquake["properties"]["mag"] > 6:
        eq_dict = {}
        eq_dict["Location"] = earthquake["properties"]["place"]
        eq_dict["Magnitude"] = earthquake["properties"]["mag"]
        eq_dict["Longitude"] = earthquake["geometry"]["coordinates"][0]
        eq_dict["Latitude"] = earthquake["geometry"]["coordinates"][1]
        print()
        print("Location:", eq_dict["Location"])
        print("Magnitude:", eq_dict["Magnitude"])
        print("Longitude:", eq_dict["Longitude"])
        print("Latitude:", eq_dict["Latitude"])
"""
print()
for eq in eq_dict:
    print("Location:", eq_dict["Location"])
    print("Magnitude:", eq_dict["Magnitude"])
    print("Longitude:", eq_dict["Longitude"])
    print("Latitude:", eq_dict["Latitude"])
    print()
