def bakingPython():
    breadWeight = 16
    servingSize = 2.5
    guests = 25

    loavesOfBread = (guests * servingSize) / breadWeight

    yeast = loavesOfBread * 1.5
    salt = loavesOfBread * 1.5
    sugar = loavesOfBread * 1.5
    flour = loavesOfBread * 2.5
    starter = loavesOfBread * 2.0
    water = loavesOfBread * 0.5

    print("For " + guests + " people, you will need ")
    print(loavesOfBread + " loaves of bread:\n")
    print("  " + yeast + " teaspoons instant yeast")
    print("  " + salt + " teaspoons salt")
    print("  " + sugar + " teaspoons sugar")
    print("  " + flour + " cups all-purpose flour")
    print("  " + starter + " cups sourdough starter")
    print("  " + water + " cups lukewarm water")
