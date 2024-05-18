temperatures = """Saturn has a daytime temperature of -170 degrees Celcius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has - 28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())

print("the moon and the earth".title())

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

mars_temperature = "The highest temperature on Mars is about 30 C"
print(mars_temperature.split())
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

mars_temperature = "The highest temperature on Mars is about 30 C"
if "30 C".endswith("C"):
        print("This temperature is in Celsius")

        mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text)

text = "Temperatures on the Moon can vary wildly."
print("temperatures" in text.lower())

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is mooving about 4cm every year."]
print(' '.join(moon_facts))

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
sentences = text.split(". ")
print(sentences)

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)


mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

subject = "intresting facts about the moon"
heading = f"{subject.title()}"
print(heading)

name = 'Ganymede'
gravity = '1.43'
planet = 'Mars'

template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))

