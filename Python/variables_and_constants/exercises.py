# 1 - 343

KmByLitre = 12

print("Olá! Vamos calcular a autonomia da sua viajem")

time = float(input("Quantas horas durou sua viagem?"))
speed = float(input("Qual foi a velocidade média do carro?"))

print("A autonomia do seu carro foi: ", (time * speed) / 12)

print("\n\n---------------------------\n\n")
# 2 - 347

print("Olá! Vamos classificá-lo por sua idade!")

age = float(input("digite sua idade: "))

if age < 0:
    print("Idade inválida")
elif age < 13:
    print("Você é criança!")
elif age < 18:
    print("Você é adolescente!")
else:
    print("Você é adulto!")

print("\n\n---------------------------\n\n")
# 3 - 351

notes = []
media = 0
for i in range(5):
    note = float(input(f"Digite a nota número {i + 1}: "))
    notes.append(note)

for note in notes:
    media += note

print("Sua média foi: ", media / 5)

print("\n\n---------------------------\n\n")

print("Tabuada do 3:")
for i in range(0, 10):
    print("3 x", i, "=", i * 3)
