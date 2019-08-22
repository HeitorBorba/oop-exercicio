nome = input('Digite seu nome')
idade = input('Digite sua idade')
rg = input('Digite seu rg')



class Pessoa:
    def __init__(self,nome,idade,rg):
        self.nome = nome
        self.idade = idade
        self.rg =rg






class Paciente(Pessoa):
    def __init__(self,enfermidade,nd_risco,sintomas):
        self.enferidade = enfermidade
        self.nd_risco = nd_risco
        self.sintomas = sintomas
    # super().__init__(nome,idade,rg)
    # self.nome = nome
    # self.idade = idade
    # self.rg = rg







class Medico(Pessoa):
    def __init__(self,crm):
        self.crm = crm

    # super().__init__(nome, idade, rg)


pessoa = Pessoa (nome, idade,rg)
paciente = Paciente('')
medico = Medico('')