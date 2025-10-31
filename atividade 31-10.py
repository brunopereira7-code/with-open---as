import os 
from dataclasses import dataclass
os.system("cls") 

@dataclass

class Endereco:
    logradouro:str
    numero:int 

@dataclass

class Pessoa:
    nome:str
    idade:int
    endereco:Endereco

    def mostrar_resultado(self):
        print(f"seu nome é {self.nome}")
        print(f"sua idade é {self.idade}")
        print(f"seu nome de casa é {self.endereco.numero}")
        print(f"seu endereço é {self.endereco.logradouro}") 



nome=input("Digite seu nome")
idade=int(input("Digite sua idade"))
logradouro=input("Digite seu logradouro")
numero=int(input("Digite seu numero de casa"))

#é um exemplo de instanciação de objetos — ou seja, você está criando instâncias (objetos) das classes Autor e Livro.
endereco=Endereco(logradouro=logradouro,numero=numero)
pessoa=Pessoa(nome=nome,idade=idade,endereco=endereco)

pessoa.mostrar_resultado()


#jeito 1
# dados=Pessoa(nome=input("Digite seu nome"),
#              idade=int(input("Digite o numero ")),
#              ) 

# endereco=Endereco(logradouro=input("Digite seu logradouro"),
#                   numero=int(input("Digite seu numero")),
#                   ) 

# dados.mostrar_resultado()