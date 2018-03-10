states = {
    'Oregan':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville',
    'NY':'New York City',
    'OR':'Portland'
}
print("-"*10)
print("NY State Has: ", cities['NY'])
print("OR State Has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for state, abbrev in states.items():
    print("%s is the abbreviated %s" % (state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
          print("%s has the city %s" % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
          print("%s state is abbreviated %s and has the city %s" % (state, abbrev, cities[abbrev]))

print("-"* 10)
state = states.get("Texas", None)
if not state:
          print("sorry, no Texas")
city = cities.get("TX", "Does not exist")
print("the city for the state TX is %s" % city)

