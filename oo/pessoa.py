class Pessoa:
    def __init__(self,*filhos, nome=None,idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'olá {id(self)}'
if __name__ == '__main__':
    lins = Pessoa(nome='Lins')
    brenda = Pessoa(lins, nome='brenda')
    print(Pessoa.cumprimentar(brenda))
    print(id(brenda))
    print(brenda.cumprimentar())
    print(brenda.nome)
    print(brenda.idade)
    for filho in brenda.filhos:
        print(filho.nome)
    brenda.sobrenome = 'Layse'
    del brenda.filhos
    print (brenda.__dict__)
    print(lins.__dict__)
