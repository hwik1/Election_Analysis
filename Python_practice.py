counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

    counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

for county in counties:
    print(county)

# for county in counties_dict.keys():    
    print(county)

counties_dict = {'Arapahoe':422829, 'Denver':463353, 'Jefferson':432438}

for county, voters in counties_dict.items():
    print("{} county has {} registered voters.".format(county,voters))
    print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters} registered voters.")

