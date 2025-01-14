import requests

# # Age guessing API
# name = input("Enter your name: ")
# response = requests.get(f"https://api.agify.io/?name={name}")
# print(response.json())

# # Joke API
# response = requests.get("https://api.chucknorris.io/jokes/random")
# print(response.json()["value"])

# OMDB API
response = requests.get("https://www.omdbapi.com/?apikey=xxxxx&t=Deewaar&plot=full")
print(response.json()['Plot'])