class Pessoa:
    olhos = 2

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
    brenda.olhos =1
    del brenda.olhos
    print (brenda.__dict__)
    print(lins.__dict__)
    Pessoa.olhos = 3
    print(brenda.olhos)
    print(lins.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(brenda.olhos), id(lins.olhos))