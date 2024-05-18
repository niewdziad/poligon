planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
print(planets)

print("The first planet is", planets[0])

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Ponieważ indeksowanie zaczyna się od 0, należy dodać wartość 1, aby wyświetlić odpowiednią liczbę.
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
mercury_index = planets.index("Mercury")
print("Mercury is the", mercury_index + 1, "planet from the sun")

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptun']
print(planets)
print('There are', len(planets), 'planets')

planets.append('Pluto')
print('Actually, there are', len(planets), 'planets')
print('The last planet is', planets[-1])

planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:]
print(planets_after_earth)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satelite_moons = amalthea_group + galilean_moons
regular_satelite_moons.sort()
print('The regular satelite moons of Jupiter are', regular_satelite_moons)

regular_satelite_moons.sort(reverse=True)
print('The regular satelite moons of Jupiter are', regular_satelite_moons)

# Wycinek tworzy nową listę. Nie modyfikuje bieżącej listy.
# Łączenie list tworzy nową listę. Nie modyfikuje bieżącej listy.
# Użycie sort modyfikuje bieżącą listę.

# zadanie:

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
user_planet = input('Please enter the name of the planet - use a capital letter to start: ')

planet_index = planets.index(user_planet)

print('Here are the planet closer than ' + user_planet)
print(planets[0:planet_index])

print('Here are the planets further than ' + user_planet)
print(planets[planet_index + 1:])

