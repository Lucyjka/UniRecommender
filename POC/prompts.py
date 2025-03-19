from config import model


def generate_prompt(user_interests, df):
    grouped_programs = (
        df.groupby("iscedName", group_keys=False)["mainInstitutionName"]
        .unique()
        .apply(lambda x: list(x)[:3])  # Maksymalnie 3 uczelnie
        .reset_index()
    )

    program_data = "\n".join(
        [f"Kierunek: {row['iscedName']}\nUczelnie: {', '.join(row['mainInstitutionName'])}"
         for _, row in grouped_programs.iterrows()]
    )

    prompt = (
        f"Użytkownik ma zainteresowania: {user_interests}.\n"
        f"Na podstawie dostępnych kierunków studiów w Polsce zasugeruj mu odpowiednie kierunki oraz uczelnie.\n\n"
        f"Lista dostępnych kierunków:\n{program_data}\n\n"
        f"Format odpowiedzi:\n"
        f"Kierunek: [Nazwa kierunku]\n"
        f"Uczelnie: [Nazwa uczelni], [Nazwa uczelni], [Nazwa uczelni]\n\n"
        f"Podaj maksymalnie 5 kierunków, a dla każdego z nich do 3 uczelni. "
        f"Jeśli w bazie nie ma pasujących kierunków, napisz: "
        f"'Nie znaleziono odpowiednich kierunków dla Twoich zainteresowań, spróbuj podać inne zainteresowania lub miasto.'"
    )
    return prompt


def get_suggestions(user_interests, df):
    prompt = generate_prompt(user_interests, df)
    response = model.generate_content(prompt)
    return response.text