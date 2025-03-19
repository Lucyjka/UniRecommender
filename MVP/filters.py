def city_filter(user_city,df):
    filtered = df[df['leadingInstitutionCity']==user_city]
    return filtered if not filtered.empty else df

def profile_filter(user_profile,df):
    filtered = df[df['profileName']==user_profile]
    return filtered if not filtered.empty else df


def level_filter(user_level, df):
    level_mapping = {
        'jednolite magisterskie': 1,
        'pierwszego stopnia': 2,
        'drugiego stopnia': 3
    }

    level_code = level_mapping.get(user_level, user_level)
    filtered = df[df['levelCode'] == level_code]
    return filtered if not filtered.empty else df

def institution_kind_filter(user_institution_kind, df):
    filtered = df[df['mainInstitutionKind'] == user_institution_kind]
    return filtered if not filtered.empty else df
