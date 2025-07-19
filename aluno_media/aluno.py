# Classe aluno
class aluno:

    # Método construtor de objetos
    def __init__ (self, nome: str, nota1: float, nota2: float, nota3: float, nota4: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        


    # Método para calcular media
    def aplicar_desconto (self) -> float:

        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

        
        # Retorna a media
        return media
