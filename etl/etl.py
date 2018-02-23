def transform(legacy_data):
    result = {}
    for item in legacy_data.items():
        for letter in item[1]:
            result[letter.lower()] = item[0]

    return result