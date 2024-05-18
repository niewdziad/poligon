# Najważniejszą rzeczą do zapamiętania podczas tworzenia while pętli jest zapewnienie, że warunek ulegnie zmianie. 
# Jeśli warunek jest zawsze spełniony, język Python będzie nadal uruchamiać kod do momentu awarii programu.

# while condition:
#   code

# Utwórz zmienną do wprowadzenia przez użytkownika
user_input = ''
# Utwórz listę do przechowywania wartości
inputs = []

# Pętla while
while user_input.lower() != 'done':
    # Sprawdź, czy istnieje wartość w user_input
    if user_input:
        # Zapisz wartość na liście
        inputs.append(user_input)
    # Monituj o nową wartość
    user_input = input('Enter a new value, or done when done: ')

print(user_input)  



new_planet = ''
planets = []

while user_planet != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done: ')

print(planets)