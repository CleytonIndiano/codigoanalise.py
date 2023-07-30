#Análise de maior e menor peso
def linha():
    print('=====' * 8)


maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Informe o peso da {pessoa}ª pessoa: kg '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
            menor = peso
linha()
print(f'O maior peso encontrado foi de {maior}kg.')
print(f'O menor peso encontrado foi de {menor}kg.') 
linha()
