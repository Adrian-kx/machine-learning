import pandas as pd


def log_separator(size=70):
    print("\n\n", "-" * size, "\n\n")


dataframe = pd.DataFrame(
    data=[[1, "Adrian", "Xavier"], [2, "Gabi", "da Silva"]],
    columns=["ID", "Name", "Surname"],
)

log_separator()
print(dataframe)

dataframe_with_index = pd.DataFrame(
    data=[[1, "Adrian", "Xavier"], [2, "Gabi", "da Silva"]],
    columns=["ID", "Name", "Surname"],
    index=["marido", "mulher"],
)

log_separator()
print(dataframe_with_index)


dados = {"ID": [1, 2, 3], "Nome": ["John", "Jane", "Jim"], "Idade": [22, 33, 44]}
dataframe_with_dictionary = pd.DataFrame(dados)

log_separator()
print(dataframe_with_dictionary)

dataframe_with_dictionary["Salario"] = [1000, 2000, 3000]

log_separator()
print(dataframe_with_dictionary)

classData = pd.read_csv(
    "curso-2/module_one/data/pandas-sample-data.csv"
    )

log_separator()
print(classData)