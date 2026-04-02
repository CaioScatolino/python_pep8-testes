# r = read
# w = write
# a = append
# x = create
# b = binary
# t = text
# + = update


with open("lista.txt", "a") as arquivo:
    item = input("Digite algo: ")

    if item != "":
        arquivo.write("\n" + item)

        with open("lista.txt", "r") as arquivo:
            for linha in arquivo:
                print(f"-- {linha.strip()}")

    else:
        print("Item inválido")


