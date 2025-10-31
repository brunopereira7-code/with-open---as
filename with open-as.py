import os
os.system("cls") 

#Texto que desejo salvar
texto=input("Digite seu nome:")

# definir nome do arquivo pra salvar.
nome_arquivo ="exemplo.txt" 

#comando pra salvar. 
with open(nome_arquivo,"a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n") 
    print("salvo com sucesso!") 