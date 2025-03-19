from config import load_data
from filters import *
from prompts import *

data_path = "data.csv"
data = load_data(data_path)

user_city_input = input("Podaj miasto, w którym chcesz studiować: ") # albo pole tekstowe, albo lista z miastami (unikalne rekordy z kolumny mainInstitutionCity)
filtered_data = city_filter(user_city_input, data)

user_profile_input = input("Czy profil ma być praktyczny czy ogólnoakademicki?: ") # lista z dwoma opcjami do wyboru: praktyczny/ogólnoakademicki
filtered_data = city_filter(user_profile_input, filtered_data)

user_level_input = input("Jakiego stopnia?: ") # lista do wyboru: jednolite magisterskie, pierwszego stopnia, drugiego stopnia
filtered_data = level_filter(user_level_input, filtered_data)

user_institution_kind_input = input("Jakiego rodzaju ma być uczelnia?: ") # lista do wyboru: Uczelnia publiczna, Uczelnia niepubliczna, Uczelnia kościelna
filtered_data = institution_kind_filter(user_institution_kind_input, filtered_data)

user_interest_input = input("Podaj swoje zainteresowania: ") # pole tekstowe
suggestions = get_suggestions(user_interest_input, filtered_data)


print("\nRekomendowane kierunki studiów:\n", suggestions)