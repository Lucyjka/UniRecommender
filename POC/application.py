from config import load_data
from filters import filteration
from prompts import *

data_path = "data.csv"
data = load_data(data_path)

user_city_input = input("Podaj miasto, w którym chcesz studiować: ")
filtered_data = filteration(user_city_input, data)

user_interest_input = input("Podaj swoje zainteresowania: ")
suggestions = get_suggestions(user_interest_input, filtered_data)

print("\nRekomendowane kierunki studiów:\n", suggestions)