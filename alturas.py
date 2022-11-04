numero_pessoas = input("informe o numero de pessoas: ")
# Todo dado que é digitado (input) por padrão ele é uma string
# se for ter calculos com estas informações é necessario transformar para inteiro (int)
numero_pessoas = int(numero_pessoas)
lista_nomes = []
lista_idade = []
lista_altura = []
soma_altura = 0
contador_numero_pessoas_menor = 0
contador_numero_pessoas_maior = 0
lista_menores_idade = []
for i in range(int((numero_pessoas))):
    nome = input("informe um nome: ")
    lista_nomes.append(nome)
    altura = input("informe a altura: ")
    # Todo dado que é digitado (input) por padrão ele é uma string
    # se for ter calculos com estas informações é necessario transformar para inteiro (int)
    altura = int(altura)
    lista_altura.append(altura)
    idade = input("informe a idade: ")
    # Todo dado que é digitado (input) por padrão ele é uma string
    # se for ter calculos com estas informações é necessario transformar para inteiro (int)
    idade = int(idade)
    lista_idade.append(idade)
    soma_altura = soma_altura + altura
    # if se menor do que 16 entra na lista de menores de idade e entra no cantador menor de idade
    # se não entra na contador maior idade
    if (idade < 16):
        lista_menores_idade.append(nome)
        lista_menores_idade.append(altura)
        lista_menores_idade.append(idade)
        contador_numero_pessoas_menor = contador_numero_pessoas_menor + 1
    else:
        contador_numero_pessoas_maior = contador_numero_pessoas_maior + 1

        idade = int(idade)
        lista_idade.append(idade)
        soma_altura = soma_altura + altura
        # if se menor do que 16 entra na lista de menores de idade e entra no cantador menor de idade
        # se não entra na contador maior idade
        if (idade < 16):
            lista_menores_idade.append(nome)
            lista_menores_idade.append(altura)
            lista_menores_idade.append(idade)
            contador_numero_pessoas_menor = contador_numero_pessoas_menor + 1
        else:
            contador_numero_pessoas_maior = contador_numero_pessoas_maior + 1

            # media simples soma da alturas de todas a pessoas pelo numero de pessoas
media = soma_altura/numero_pessoas
print("A altura media é: ", media)

# para achar o percentual fazemos contato de pessoas menor / total de pessoas
total = contador_numero_pessoas_maior + contador_numero_pessoas_menor
percentual = (contador_numero_pessoas_menor / total) * 100
print("o percentual  de menores de idade e %", percentual)
['nino', 5, 6, 'laura', 5, 6, 'luiza', 4, 5]
