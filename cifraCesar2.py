import os
alfa = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z") #tupla do alfabeto

def Criptografar(msg,des,x,k,z):
    os.system("cls")
    cripto = ""
    textoCript = ""
    if des <= 25 and des >= 0: #verifica se o valor inserido está entre 25 e 0 
        while x < len(msg): #enquanto a variavel x for menor que o tamanho da mensagem ele continuara executando o loop até toda  a mensagem ser exibida
            for i in alfa: #para cada letra do alfabeto (lista alfa anteriormente criada) ele ira realizar esse for
                k += 1 #sempre que uma letra nao estiver na mensagem o k ganha 1 de valor
                if i in msg[x].lower(): #se o i, ou seja, se a letra presente no i estiver na posiçao x da mensagem, no inicio sera 0, ele ira adicionar essa letra e criptografar ela com a cifra de cesar na lista cripto. O .lower é pra ler o valor em letra minuscula para nao da erro
                    k = 0 #caso a letra esteja o k é resetado
                    if alfa.index(i)+des >= len(alfa): #aqui ele ve se a soma da posição do caractere mais o deslocamento fica maior que a tupla com o alfabeto, se for ele vai subtrair a tupla pela soma e inserir o valor como posiçao da tupla do alfabeto
                        cripto = cripto + alfa[alfa.index(i)+des - len(alfa)] #aqui é a subtração da posição com o deslocamento desejado menos o tamanho do alfabeto
                        x += 1
                    else:
                        cripto = cripto + alfa[alfa.index(i)+des] #ele adicionar o elemento que está na posiçao alfa.index(i), ou seja a posição do valor do i que seria a letra do alfabeto, somada com o deslocamento desejado, assim o valor que sera inserido na lista cripto ja estará criptografado
                        x += 1 #caso o if execute ele passara para a proxima letra da mensagem
                    break                
                if k == 26: #caso o k seja 26 significa que todas as letras do alfabeto foram testadas, então ele colocará o caractere ou numero inserido no lugar
                        cripto = cripto + msg[x] #insere o caractere na mensagem codificada
                        k = 0   #reseta o k
                        x += 1 #passa para o proximo caractere da mensagem
                        break #quebra o loop for e volta para o while
        for i in cripto: 
            if msg[z] == msg[z].upper(): #caso a letra esteja em maiusculo ele transforma o texto criptografado em maiusculo também
                textoCript = textoCript+ i.upper()
                z += 1
            else:
                textoCript = textoCript + cripto[z]
                z += 1

        os.system("cls")
        print(f'Mensagem original: {msg}\nMensagem Criptografada: {textoCript}')

def Descriptografar(Criptografada,des,x,k,z):
    os.system("cls")
    decripto = ""
    textoDecript = ""
    if des <= 25 and des >= 0:
        while x < len(Criptografada):
            for i in alfa:
                k += 1
                if i in Criptografada[x].lower():#mesma logica da criptografar
                    k = 0
                    if len(alfa)-abs((alfa.index(i)-des)) >= 26: #ele vai ver se 26- a poesiçao da letra no alfabeto menos o deslocamento é mairo que 26, se for ele vai entrar no if
                        decripto = decripto + alfa[len(alfa)-abs((alfa.index(i)-des))-len(alfa)] #ele vai colocar a letra no decripto da posição 26 - a posiçao da letra menos a quantidade de desclocamentos - 26 novamente, para assim fazer o valor ficar abaixo de 26 e encontrar a letra original
                        x += 1
                    else:
                        if alfa.index(i)-des > 0:
                            decripto = decripto + alfa[abs((alfa.index(i)-des))]
                            x += 1
                        else:
                            decripto = decripto + alfa[len(alfa)-abs((alfa.index(i)-des))]
                            x += 1
                    break
                if k == 26: #mesma logica do outro
                    decripto = decripto + Criptografada[x]
                    k = 0  
                    x += 1 
                    break
        for i in decripto: #mesma logica do outro
            if Criptografada[z] == Criptografada[z].upper():
                textoDecript = textoDecript + i.upper()
            else:
                textoDecript = textoDecript + i
            z += 1

        print(f'Mensagem Criptografada: {Criptografada}\nMensagem Descriptografada: {textoDecript}')

opcao = input("O que deseja fazer?\n1- Codificar uma mensagem em cifra de cesar\n2- Decodificar uma mensagem em cifra de cesar\n")
if opcao == "1":
    mensagem = input("Digite uma mensagem: ")
    deslocamentos = int(input("Digite quantos deslocamentos voce deseja (0-26): "))
    Criptografar(mensagem,deslocamentos,0,0,0)
elif opcao == "2":
    mensagem = input("Digite a mensagem criptografada: ")
    deslocamentos = int(input("Digite em quantos deslocamentos ela foi criptografada: "))
    Descriptografar(mensagem,deslocamentos,0,0,0)