class List:
    def __init__(self, name):
        self._filename = f"{name}.txt"

    def get_list(self):
        list = []
        with open(self._filename, "r") as arquivo:
            for linha in arquivo:
                list.append(linha.strip())
        return list

    def add_item(self, item):
        with open(self._filename, "a") as arquivo:
            if item != "":
                arquivo.write(f"\n{item}")
                return True
            else:
                return False


list = List("lista")
for item in list.get_list():
    print(f"-- {item}")

new_item = input("Digite o item que deseja adicionar: ")
added = list.add_item(new_item)
if added == True:
    print("Item adicionado com sucesso!")

    list = List("lista")
    for item in list.get_list():
        print(f"-- {item}")
else:
    print("Item inválido!")
