import os
from dataclasses import dataclass

os.system("cls")

@dataclass 
class Autor:
    nome: str = "Antoine de Saint-Exupéry"
    biografia: str = (
        "Fala sobre temas como amizade, amor, perda da inocência "
        "e o que é realmente essencial na vida, contrastando a visão de mundo "
        "adulta com a pureza e imaginação da infância."
    )

@dataclass
class Livro: 
    titulo: str = "O Pequeno Príncipe"
    ano: int = 1990
    autor: Autor = Autor()

    def exibir_resultado(self):  # corrigido o nome
        print("----- Detalhes do Livro -----")
        print(f"Nome do autor: {self.autor.nome}")
        print(f"Biografia: {self.autor.biografia}")
        print(f"Título do livro: {self.titulo}")
        print(f"Ano do livro: {self.ano}")

livro = Livro()
livro.exibir_resultado()
