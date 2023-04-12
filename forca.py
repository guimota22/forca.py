#guizin trem bala 22 di maluco

print("\nclubederegatasvascodagama\n")
print("Bem vindo ao ct do vasco")
print("\nclubederegatasvascodagama\n")
 
palavra_secreta = "ficavp".upper()
letras_acertadas = ["_" for letra in palavra_secreta]
print(letras_acertadas)

enforcou = False
acertou = False
erros = 0
while(not enforcou and not acertou):

    chute = input("Qual a letra? ")
    chute = chute.strip().upper()

    if(chute in palavra_secreta):
        vascao = 0
        for letra in palavra_secreta:
            if(chute==letra):
                letras_acertadas[vascao] = letra
            vascao+=1
    else:
        erros+=1


    print(letras_acertadas)
    print('Chutes errados ', erros)

    if(erros==6):
        enforcou=True

    if("_" not in letras_acertadas):
        acertou=True
        print("Você ganhou")
    else:
        print("Você não ganhou")

input()
