'''------------------------------------------------------------------------
    UNIVERSIDADE CRUZEIRO DO SUL
    CURSO DE ANÁLISE E DESENSOLVIMENTO DE SISTEMAS
    DISCIPLINAS: ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES &
    PROGRAMAÇÃO DE COMPUTADORES
    Educandos do 1º Semestre / 2022
    Andréa Alves dos Santos – RGM: 5829895324
    Gabriel de Oliveira Rodrigues – RGM: 5829641748
    Jordi Mello Llinares – RGM: 5829771480
    Luciana da Silva Lucindo – RGM: 5828831322
    Tarcísio Silva Souza – RGM: 5829368090

    EDUCADORES: MAURÍCIO MENDES FARIA E VINICIUS HELTAI PACHECO

    Enunciado: O projeto interdisciplinar deste semestre tem como
    objetivo promover a integração das disciplinas de Organização e
    Arquitetura de Computadores e Programação de Computadores e consiste
    na construção de um software utilizando-se da linguagem de programação
    Python, que permita a realização de operações que envolvam Sistemas de
    Numeração.
    Apropriando-se da tecnologia descrita acima, cada grupo deverá desenvolver
    um programa para resolver questões pertinentes a um problema específico a
    ser escolhido dentre as opções apresentadas abaixo:
    Opção 1: Conversão da base decimal para as bases binário, hexadecimal e
    octadecimal.
    
    -------------------------------------------------------------------------'''




while(True): #Função usada para deixar o código em loop para que possa ser feita varias operações seguidas
    nDecimal = int(input('Digite um número inteiro de base decimal: ')) #Entrada do valor do número decimal a ser convertido para demais bases
    num = nDecimal #Variável atribuida para ser usada no print final.

    print('''Escolha uma das bases numericas para conversão: 

    [1] converter para binário
    [2] converter para octal
    [3] converter para hexadecimal
    [0] finalizar o programa''') #Texto impressão para informar opções que possam ser usadas.
    sobra = [] #Lista que será usada para armazenar os resultados dos restos de divisões para fazer a conversão de bases.
    opcao = int(input(' A opção é: ')) #Entrada da opção de base para ser convertida a var = nDecimal, ou opção para finalizar o programa.

    if opcao == 1: #Condição para conversão da opção 1 - binário
        while nDecimal != 0: #Enquanto a var = nDecimal for diferente de "0" o programa irá continuar as subsequêntes diviões até a condição ser atingida.
            resto = nDecimal % 2 #variável para armazenar o resultado do resto da divisão 
            quociente = nDecimal // 2  #váriável para armazenar o resultado da divisão inteira.
            sobra.append(resto) #Será inserido o valor da variável "resto" dentro da lista "sobra" para ser construído o número convertido
            nDecimal = quociente
            '''Atribuido novo valor para a variável nDecimal para que seja continuado o programa
            até ser atingida a condição predominante do while onde Ndecimal é diferente de '0'.'''
            

    if opcao == 2: #Condição para conversão da opção 2 - Octal
        while nDecimal != 0: #Enquanto a var = nDecimal for diferente de "0" o programa irá continuar as subsequêntes diviões até a condição ser atingida.
            resto = nDecimal % 8  #variável para armazenar o resultado do resto da divisão
            quociente = nDecimal // 8 #váriável para armazenar o resultado da divisão inteira.
            sobra.append(resto) #Será inserido o valor da variável "resto" dentro da lista "sobra" para ser construído o número convertido
            nDecimal = quociente
            '''Atribuido novo valor para a variável nDecimal para que seja continuado o programa
            até ser atingida a condição predominante do while onde Ndecimal é diferente de '0'.'''
            

    if opcao == 3: #Condição para conversão da opção 1 - binário
        while nDecimal != 0:#Enquanto a var = nDecimal for diferente de "0" o programa irá continuar as subsequêntes diviões até a condição ser atingida.
            resto = nDecimal % 16  #variável para armazenar o resultado do resto da divisão
            quociente = nDecimal // 16 #váriável para armazenar o resultado da divisão inteira.
            sobra.append(resto) #Será inserido o valor da variável "resto" dentro da lista "sobra" para ser construído o número convertido
            nDecimal = quociente
            '''Atribuido novo valor para a variável nDecimal para que seja continuado o programa
            até ser atingida a condição predominante do while onde Ndecimal é diferente de '0'.'''


            for index, value in enumerate(sobra): #Varíavel atribuida "Index", onde o valor da lista "restos" será verificado se:
                if value == 10: #Se o valor for igual a 10...
                    sobra [index] = 'A' #A variável  index será convertida em 'A'
                elif value == 11: #Se o valor for igual a 11...
                    sobra [index] = 'B' #A variável  index será convertida em 'B'
                elif value == 12: #Se o valor for igual a 12...
                    sobra [index] = 'C' #A variável  index será convertida em 'C'
                elif value == 13: #Se o valor for igual a 13...
                    sobra [index] = 'D' #A variável  index será convertida em 'D'
                elif value == 14: #Se o valor for igual a 14...
                    sobra [index] = 'E' #A variável  index será convertida em 'E'
                elif value == 15: #Se o valor for igual a 15...
                    sobra [index] = 'F' #A variável  index será convertida em 'F'

    if opcao == 0: #Condição para conversão da opção 0 - Finalizar programa
        print (f" O programa foi finalizado") #Informativo que o programa foi finalizado.
        break 

                    
    
    
    list.reverse(sobra) #função de lista para reescrever a mesma de trás para frente.
    print(f' O número decimal {num} convertido é igual à: {sobra}') #Impressão do resultado da conversão
    print(f' ===================================================== \n')
    
