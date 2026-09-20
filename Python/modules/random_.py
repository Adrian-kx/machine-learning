import random

print(random.random())
print(random.randint(0, 10))
print(random.randrange(0, 10, 2))  # Gera de 0 a 10 que sejam multiplos de 2


list = ["a", "b", "d", "x", "w"]
print(random.choice(list))
print(random.choices(list))
