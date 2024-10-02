import random
import requests

# URL for API
base_url = "https://swapi.dev/api/people/"


# fetch data for the first character in the API (Luke Skywalker)
response = requests.get(base_url + "1/")
character_data = response.json()


# print the character's name
print("Character Name:", character_data['name'])

# generate a random number between 1 and 83
random_character_id = random.randint(1, 83)


# fetch data for the randomly selected character
response = requests.get(base_url + str(random_character_id) + "/")
character_data = response.json()


# Print the character's name and other details
print("Randomly Selected Character:", character_data['name'])
print("Character Height:", character_data['height'], "cm")
print("Character Mass:", character_data['mass'], "kg")
print("Character Birth Year:", character_data['birth_year'])

# Select 3 random Star Wars characters
for i in range(3):
   random_character_id = random.randint(1, 83)
   response = requests.get(base_url + str(random_character_id) + "/")
   character_data = response.json()
  
   print(f"\nCharacter {i+1}: {character_data['name']}")
   print("Height:", character_data['height'], "cm")
   print("Mass:", character_data['mass'], "kg")
   print("Birth Year:", character_data['birth_year'])
