# by My Nguyen
# Dec 2, 2024
# Homework 9: Lunar Lander Simulation
# Program description: There were many computer games developed in the 1970s that allowed players to simulate the moon landing. The goal was to pilot the lunar lander to a safe landing. In this homework, we will make a version of this game. We make 2 functions in this homework. One of them gets the amount of fuel from the user. The other functions allows the player to land on a planet.


import sys

def askFuel(currentFuel):
    while True:
        try:
            fuel = int(input("Enter units of fuel to use: \n"))
            if fuel < 0:
                print("Cannot use negative fuel.")
            elif fuel > currentFuel:
                print(f"No enough fuel. Max Fuel: {currentFuel}")
            else:
                return fuel
        except ValueError:
            print("Please Enter Integer Value.")

def playLevel(name, G, fuel):
    altitude = 50  
    velocity = 0  
    T = 0.10  
    seconds = 0
    
    print(f"Landing on the {name}")
    print(f"Gravity is {G:.2f} m/s^2")
    print(f"Initial Altitude: {altitude} meters")
    print(f"Initial Velocity: {velocity:.2f} m/s")
    print(f"Burning a unit of fuel causes {T:.2f} m/s slowdown.")
    print(f"Initial Fuel Level: {fuel} units\n")
    print(f"GO")

    while altitude > 0:
        burn = askFuel(fuel)
        fuel -= burn
        velocity = velocity + G + T * burn
        altitude += velocity
        altitude = max(0, altitude) 
        seconds += 1

        print(f"After {seconds} seconds Altitude is {altitude:.2f} meters, velocity is {velocity:.2f} m/s.")
        print(f"Remaining Fuel: {fuel} units.")

        if altitude == 0:
            if -2 <= velocity <= 2:
                print("Landed Successfully.")
                return True
            else:
                print("Crashed!")
                return False
            return nextLevel 

if __name__ == "__main__":
    planets = [
        ("Moon", -1.622, 150),
        ("Earth", -9.81, 5000),
        ("Pluto", -0.42, 100),
        ("Neptune", -14.07, 2000),
        ("Uranus", -10.67, 1500),
        ("Saturn", -11.08, 1800),
        ("Jupiter", -25.95, 4000),
        ("Mars", -3.77, 500),
        ("Venus", -8.87, 1500),
        ("Mercury", -3.59, 600),
        ("Sun", -274.13, 10000)
    ]

    level = 0
    print("Welcome to Lunar Lander Game.")
    while level < len(planets):
        play = input(f"Do you want to play level {level + 1}? (yes/no)\n").strip().lower()
        if play == 'yes':
            planetName, gravity, fuel = planets[level]
            print(f"Entering Level {level + 1}")
            result = playLevel(planetName, gravity, fuel)
            if (result == True):
                level+=1
            nextLevel = input("Do you want to play level {}? (yes/no)\n".format(level + 1)).strip().lower()
            while nextLevel == 'yes' and level < len(planets) - 1:
                planetName, gravity, fuel = planets[level]
                print(f"Entering Level {level + 1}")
                nextLevel = playLevel(planetName, gravity, fuel)
            if nextLevel == 'no':
                break
        elif play == 'no':
                break
        else:
            print("Please enter 'yes' or 'no'.")
            
    print(f"You made to past {level} levels.")
    print("Thanks For Playing.")