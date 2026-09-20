# Aqui o padrão é 'r' de read, mas colocamos 'w' de write
# Para escrever em uma rquivo
with open('text2.txt', 'w') as file:
    file.write("Olá a todos\nsegunda linha")