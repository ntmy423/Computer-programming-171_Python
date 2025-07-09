# by My Nguyen
# Nov 19, 2024
# Homework 8: Write a program that reads food recipe from a file
# Program Description: This program processes a food database and recipe file to analyze nutritional information
# and generate a formatted food label. It includes error handling for missing files and ingredients.

import csv

# First function
def loadFoods(filename):
    foodData = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Food (100g)'].strip()
                
                calories = None
                if row['Calories (kCal)']:
                    calories = float(row['Calories (kCal)'])
                
                protein = None
                if row['Protein (g)']:
                    protein = float(row['Protein (g)'])
                
                carbohydrate = None
                if row['Carbohydrates (g)']:
                    carbohydrate = float(row['Carbohydrates (g)'])
                
                fat = None
                if row['Fats (g)']:
                    fat = float(row['Fats (g)'])
                
                foodType = row['Type']
                
                foodData[name] = {
                    "Calories": calories,
                    "Protein": protein,
                    "Carbohydrate": carbohydrate,
                    "Fat": fat,
                    "Type": foodType
                }
        return foodData
    except FileNotFoundError:
        print(f"That file could not be loaded.")
        return None

# Second function
def readRecipe(filename):
    try:
        with open(filename, mode='r') as file:
            lines = file.readlines()
        header = lines[0].strip().split(',')
        recipeDict = {
            "Name": header[0].strip(),
            "Serves": float(header[1].strip())
        }
        for line in lines[1:]:
            parts = line.strip().split(',')
            if len(parts) == 2:
                ingredient = parts[0].strip()
                quantity = float(parts[1].strip())
                recipeDict[ingredient] = quantity
        return recipeDict
    except FileNotFoundError:
        print(f"That file could not be loaded.")
        return None
    except ValueError as e:
        print(f"Error reading recipe file: {e}")
        return None

# Third function
def analyzeIngredients(foodData, recipeDict):
    analysis = {
        "Calories": 0.0,
        "Protein": 0.0,
        "Carbohydrate": 0.0,
        "Fat": 0.0,
        "Total Grams": 0.0,
        "Incomplete": False
    }
    for ingredient, grams in recipeDict.items():
        if ingredient in ("Name", "Serves"):
            pass
        elif ingredient not in foodData:
            print(f"Trouble looking up {ingredient}")
            analysis["Incomplete"] = True
        else:
            details = foodData[ingredient]
            multiplier = grams / 100.0
            analysis["Calories"] += details["Calories"] * multiplier 
            analysis["Protein"] += details["Protein"] * multiplier
            analysis["Carbohydrate"] += details["Carbohydrate"] * multiplier 
            analysis["Fat"] += details["Fat"] * multiplier
            analysis["Total Grams"] += grams

    servings = recipeDict["Serves"]
    for key in ("Calories", "Protein", "Carbohydrate", "Fat", "Total Grams"):
        analysis[key] /= servings
    return analysis

# Fourth function
def generateLabel(recipeDict, analysisDict):
    label = f"\n{recipeDict['Name']} ({analysisDict['Total Grams']:.1f} g)\n"
    # Calories
    label += f"{'Calories':<18}{analysisDict['Calories']:.1f}\n"
    
    # Protein
    label += f"{'Protein':<18}{analysisDict['Protein']:.1f} g\n"
    
    # Carbohydrate
    label += f"{'Carbohydrate':<18}{analysisDict['Carbohydrate']:.1f} g\n"
    
    # Fat
    label += f"{'Fat':<18}{analysisDict['Fat']:.1f} g\n"
    
    # Note if some ingredients are missing
    if analysisDict["Incomplete"]:
        label += "Note: Not all ingredients accounted for"
        
    return label

# Main script
if __name__ == "__main__":
    # Load food database
    foodData = None
    while foodData == None:  # Loop until a valid food database is loaded
        foodFile = input("Enter filename for foods database: ")
        foodData = loadFoods(foodFile)

    # Load recipe file
    recipeDict = None
    while recipeDict == None:  # Loop until a valid recipe file is loaded
        recipeFile = input("Enter recipe filename: ")
        recipeDict = readRecipe(recipeFile)

    # Analyze ingredients and generate label
    analysis = analyzeIngredients(foodData, recipeDict)
    label = generateLabel(recipeDict, analysis)
    print(label)
