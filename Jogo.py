class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        # Definindo o ataque com base no tipo do herói
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"

        # Exibindo a mensagem do ataque
        print(f"o {self.tipo} atacou usando {ataque}")

# Criando instâncias da classe Heroi
heroi1 = Heroi("Gandalf", 300, "mago")
heroi2 = Heroi("Conan", 30, "guerreiro")
heroi3 = Heroi("Lao Tzu", 60, "monge")
heroi4 = Heroi("Naruto", 16, "ninja")
# Realizando ataques e imprimindo na tela
heroi1.atacar()  # Exibe: o mago atacou usando magia
heroi2.atacar()  # Exibe: o guerreiro atacou usando espada
heroi3.atacar()  # Exibe: o monge atacou usando artes marciais
heroi4.atacar()  # Exibe: o ninja atacou
