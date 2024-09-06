## ESTRUTURA DE CONDIÇÃO

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print("A média do aluno é: " + str(media))

MEDIA = (NOTA1 + NOTA2 + NOTA3) / 3
print("A média do aluno é " + str(MEDIA))

if (MEDIA >= 7):
    print("Aluno APROVADO! com média de: " + str(MEDIA))
    if(MEDIA > 5):
        print("Aluno esta em RECUPERAÇÃO!")
else:
    print("Aluno esta REPROVADO! com média de: " + str(MEDIA))
