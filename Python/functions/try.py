def read_num():
    try:
        num = int(input("Infrome o número"))
    except:
        print("Valor inválido")
    else:
        print("Numero digitado: ", num)

read_num()


def read_num2():
    try:
        num = int(input("Infrome o número"))
    except ValueError:
        print("Valor inválido")
    except KeyboardInterrupt:
        print("Ususario interrompeu o código")
    else:
        print("Numero digitado: ", num)

read_num2()