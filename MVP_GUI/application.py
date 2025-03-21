from config import load_data
from filters import *
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

def get_recommendations(city, profile, level, institution_kind, interests):
    city = match_city(city)
#user_city_input = input("Podaj miasto, w którym chcesz studiować: ") # albo pole tekstowe, albo lista z miastami (unikalne rekordy z kolumny mainInstitutionCity)
    filtered_data = city_filter(city, data)

#ser_profile_input = input("Czy profil ma być praktyczny czy ogólnoakademicki?: ") # lista z dwoma opcjami do wyboru: praktyczny/ogólnoakademicki
    filtered_data = profile_filter(profile, filtered_data)

#user_level_input = input("Jakiego stopnia?: ") # lista do wyboru: jednolite magisterskie, pierwszego stopnia, drugiego stopnia
    filtered_data = level_filter(level, filtered_data)

#user_institution_kind_input = input("Jakiego rodzaju ma być uczelnia?: ") # lista do wyboru: Uczelnia publiczna, Uczelnia niepubliczna, Uczelnia kościelna
    filtered_data = institution_kind_filter(institution_kind, filtered_data)

#user_interest_input = input("Podaj swoje zainteresowania: ") # pole tekstowe

    suggestions = get_suggestions(interests, filtered_data)

    return suggestions if suggestions else ["Brak pasujących kierunków studiów."]


#print("\nRekomendowane kierunki studiów:\n", suggestions)