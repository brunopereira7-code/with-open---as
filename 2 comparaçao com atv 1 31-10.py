import os 
from dataclasses import dataclass
os.system("cls") 

@dataclass
class Autor:
    nome:str 
    idade:int 
    biografia:str
@dataclass
class Livro:
    titulo:str
    ano:int
    autor:Autor

    def exibir_resultado(self):
        print(f"titulo do livro é {self.titulo}")
        print(f"ano é {self.ano}")
        print(f"seu nome é {self.autor.nome}")
        print(f"idade do autor é {self.autor.idade}")
        print(f"sua biografia é  {self.autor.biografia}")

dados=Livro(titulo=input("Digite o titulo do livro:"),
            ano=int(input("Digite o ano:")),
            autor=Autor(nome=input("Digite o nome do autor"),idade=int(input("Digite sua idade")), biografia=input("digite a biografia")))
            

print("\n mostrar resultado") 
dados.exibir_resultado()

