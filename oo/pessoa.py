class Pessoa:
    olhos = 2

    def __init__(self,*filhos, nome=None,idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá, meu nome é {(self.nome)}'

    @staticmethod
    def metodo_static ():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
            return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return  f'{cumprimentar_da_classe}.aperto de mão'

class Mutante (Pessoa):
    olhos = 5

if __name__ == '__main__':
    lins = Mutante(nome='Lins')
    brenda = Homem(lins, nome='brenda')
    print(Pessoa.cumprimentar(brenda))
    print(id(brenda))
    print(brenda.cumprimentar())
    print(brenda.nome)
    print(brenda.idade)
    for filho in brenda.filhos:
        print(filho.nome)
    brenda.sobrenome = 'Layse'
    del brenda.filhos
    brenda.olhos =1
    del brenda.olhos
    print (brenda.__dict__)
    print(lins.__dict__)
    print(brenda.olhos)
    print(lins.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(brenda.olhos), id(lins.olhos))
    print(Pessoa.metodo_static(), brenda.metodo_static())
    print(Pessoa.nome_e_atributos_de_classe(), brenda.nome_e_atributos_de_classe())
    pessoa= Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa,Homem))
    print(isinstance(lins, Pessoa))
    print(isinstance(lins, Homem))
    print(lins.olhos)
    print(lins.cumprimentar())
    print(brenda.cumprimentar())
