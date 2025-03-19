def filteration(user_city,df):
    filtered = df[df['leadingInstitutionCity']==user_city]
    return filtered if not filtered.empty else df