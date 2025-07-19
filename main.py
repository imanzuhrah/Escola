# Importar o módulo de produto
from aluno_media import aluno


# Solicita o nome e o preço
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota do 1° Bimestre: '))
nota2 = float(input('Digite a nota do 2° Bimestre: '))
nota3 = float(input('Digite a nota do 3° Bimestre: '))
nota4 = float(input('Digite a nota do 4° Bimestre: '))

meu_aluno = aluno(nome, nota1, nota2, nota3, nota4)

media = meu_aluno.aplicar_desconto()

print(f'Nome do Aluno: {meu_aluno.nome}')
print(f'Nota do 1° Bimestre: {nota1:.2f}')
print(f'Nota do 2° Bimestre: {nota2:.2f}')
print(f'Nota do 3° Bimestre: {nota3:.2f}')
print(f'Nota do 4° Bimestre: {nota4:.2f}')
print(f'A Media Final é: {media:.2f}')