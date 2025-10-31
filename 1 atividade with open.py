import os 
from dataclasses import dataclass
os.system("cls")

@dataclass
class Aluno:
    nome:str 
    idade:int 
    e_mail:str
    telefone:int
quantidade=2
lista_alunos=[] 

print("solicitando dados") 
for i in range(quantidade):
    aluno=Aluno(
        nome=input("Digite seu nome"),
        idade=int(input("Digite sua idade")),
        e_mail=input("Digite seu E-mail:"),
        telefone=int(input("Digite seu telefone:"))
        )
     
    lista_alunos.append(aluno) 

print()
print("Salvando dados")
arquivo="dados_alunos.txt" 

with open(arquivo,"w") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome},{aluno.idade},{aluno.e_mail},{aluno.telefone}\n")
    print("Salvo com sucesso")