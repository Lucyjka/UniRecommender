from config import load_data
from filters import filteration
from prompts import *

import unicodedata
import difflib

data_path = "data.csv"
data = load_data(data_path)

#pobieranie miast
known_cities = data['leadingInstitutionCity'].dropna().unique().tolist()

#usuwa polskie znaki, zamienia na male litery
def normalize_text(text):
    text = text.lower()
    return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')

#dopasowuje miasta wpisanego do znanych miast
def match_city(user_input):
    normalized_input = normalize_text(user_input)
    normalized_city_map = {normalize_text(city): city for city in known_cities}

    match = difflib.get_close_matches(normalized_input, normalized_city_map.keys(), n=1, cutoff=0.6)

    if match:
        return normalized_city_map[match[0]]
    else:
        return user_input.title()


def get_recommendations(city, interests):
    city = match_city(city)
    #user_city_input = input("Podaj miasto, w którym chcesz studiować: ")
    filtered_data = filteration(city, data)

    #user_interest_input = input("Podaj swoje zainteresowania: ")

    suggestions = get_suggestions(interests, filtered_data)

    return suggestions if suggestions else ["Brak pasujących kierunków studiów."]

#print("\nRekomendowane kierunki studiów:\n", suggestions)

