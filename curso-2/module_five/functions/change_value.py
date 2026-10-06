def change_values(data):
    data = data.dropna()
    data = data.round(2)
    for value in data.columns:
        if value != "Categoria":
            data = data[data[value] >= 0]

    return data
