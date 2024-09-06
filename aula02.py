idade = int(input("Digite sua idade: "))
tem_convite = True #booleano

if idade >= 18:
    if tem_convite:
        print("Pode entrar na festa!")
    else:
        print("Precisa de um convite pa entrar na festa. ")
else:
    print("Não pode entrar. É menor de idade.")