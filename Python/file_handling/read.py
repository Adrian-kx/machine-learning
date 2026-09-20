with open('text.txt') as file:
    for line in file:
        print("- ", line)


with open('text.txt') as file:
    r = file.readlines()
    print(r)
