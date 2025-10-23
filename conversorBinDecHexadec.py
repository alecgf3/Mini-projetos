import os, math
def binarioDecimal(valorInicial):
    valorFinal = 0
    x = 0
    valorCalcular = valorInicial[::-1] #inverte a sequencia pois o codigo começa a contar da esquerda pra direita e nao da direita pra esquerda que é o correto para descobrir o valor do binario

    for i in valorCalcular:
        valorFinal += int(valorCalcular[x]) * (2**x) #formula para descobrir o valor binario, como é de base 2 (0 e 1), o valor será multiplicado por 2 elevado à posição dele
        x+=1
    return valorFinal

def decimalBinario(valorInicial):
    valorFinal = ''
    resto = int(valorInicial)

    while resto != 0:
        valorFinal = valorFinal + str(round(resto%2)) #aqui utiliza=se aquele método da divisao por 2 para encontrar o valor binario do numero decimal o round() é pra arrendodar o valor e fazer dar certo esse metodo
        resto = math.floor(resto/2) #aqui é pra ir diminundo o valor até chegar em 0 q é quando temos o codigo já

    valorFinal = valorFinal[::-1]
    return valorFinal

def binarioHexadecimal(valorInicial):
    letrasValues = ('a', 'b', 'c', 'd', 'e', 'f') #valores de 10 a 15 hexadecimais
    valores = ''
    valorDecimal = 0
    valorFinal = ''
    x=1
    y=0
    while len(valorInicial)%4 != 0: #aqui é pra completar o numero com zeros para poder dividir ele em grupos de 4
        valorInicial = '0' + valorInicial 

    for i in valorInicial:
        if x % 4 == 0 and x != 0: #aqui é o metodo de conversao binario/hexadecimal onde vc pega 4 numeros do binario e transforma em 1 valor hexadecimal, faz isso até chegar ao fim do numero
            valores += valorInicial[y:x] #aqui é pra ele ir pegando os proximos grupos de 4 numeros (0:4) (4:8) (8:12) e assim por diante
            valorDecimal += binarioDecimal(valores)
            valores = ''
            if valorDecimal <= 9:#os digitos hexadecimais equivalentes aos numeros de 1-9 são 1-9 também
                valorFinal = str(valorDecimal) + valorFinal
            else:
                valorFinal = letrasValues[valorDecimal-10] + valorFinal #aqui  pega os valores de 10 a 15 em hexadecimal
            y+=4
            valorDecimal = 0
        x+=1    
    valorFinal = valorFinal[::-1] #aqui inverte o valor final para ficar o valor correto
    return valorFinal

def hexadecimalBinario(valorInicial):
    x=0
    valorFinal = 0
    letrasValues = ('a', 'b', 'c', 'd', 'e', 'f')
    valorInicial = valorInicial[::-1]
    for i in valorInicial:
            if i.lower() in letrasValues:
                valorFinal += (letrasValues.index(i.lower())+10) * (16 ** x) #mesma ideia da conversao do binario mas com base 16 e as letras que equivalem 10-15
            else:
                valorFinal += int(valorInicial[x]) * (16 ** x)
            x+=1
    return str(valorFinal)

op = input("O que deseja fazer?\n1 - Converter um numero binario nos outros\n2 - Converter um numero decimal nos outros\n3 - Converter um numero hexadecimal nos outros\n")
match op:
    case '1':
        os.system('cls')
        valorInicial = input("Digite um valor binário: ")
        print(f'Binário: {valorInicial}')
        print(f'Decimal: {binarioDecimal(valorInicial)}')
        print(f'Hexadecimal: {binarioHexadecimal(valorInicial)}')
    case '2':
        os.system('cls')
        valorInicial = input("Digite um numero decimal: ")
        print(f'Decimal: {valorInicial}')
        print(f'Binário: {decimalBinario(valorInicial)}')
        print(f'Hexadecimal: {binarioHexadecimal(decimalBinario(valorInicial))}')
    case '3':
        os.system('cls')
        valorInicial = input("Digite um valor hexadecimal: ")
        print(f'Hexadecimal: {valorInicial}')
        print(f'Decimal: {hexadecimalBinario(valorInicial)}')
        print(f'Binario: {decimalBinario(hexadecimalBinario(valorInicial))}')