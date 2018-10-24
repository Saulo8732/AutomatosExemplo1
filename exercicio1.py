"""
Linguagem pipoca
Letras possíveis:  +, -, *, /, imprima, recebe, entrada
Gramatica:
Toda sentença tem que terminar em !
Variaveis tem @ no inicio do nome

exemplo de codigo:

@nomedavariavel recebe 50!
@variavel2 recebe entrada!
imprima @variavel2 + @nomedavariavel!
"""

"""
Automato1:
Finito e deterministico:
Estado inicial:
Recebe uma letra
Estado do meio:
Testa se a letra está no alfabeto
Estado final:
Retorna um resultado booleano

Resposável por verificar a estrutura das palavras.
"""
def automato1(letra):
    alfabeto = ['+', '-', '*', '/', 'imprima', 'recebe', 'entrada']
    if letra.startswith('@'):
        return True
    elif(letra.isnumeric()):
        return True
    elif(letra in alfabeto):
        return True
    else:
        return False

"""
Automato2:
Finito e não deterministico:
Estado inicial:
Recebe uma sentenca
Estado 2:
divide a sentanca e envia cada letra para o automato1
Estado 3:
se o automato 1 retornar falso, passa para o estado final retornando falso, se recebe verdadeiro aguarda uma nova palavra, se não há mais palavras passa para o estado final retornando verdadeiro
Estado final:
retorna um resultado booleano

"""
def automato2(sentenca):
    letras  = sentenca.split()
    ultimaletra = ''
    for letra in letras:
        if(letra == ultimaletra):
            return False
        else:
            ultimaletra = letra
            if(automato1(letra)):
                continue
            else:
                return False
    return True


"""
Automato3:
Finito e não deterministico
Estado inicial:
recebe um texto
Estado 1:
divide as sentenças e envia uma a uma, para o automato2
Estado 2:
o automato2 rertonando verdadeiro, se mantem no mesmo estado, o automato2 retornando falso vai para o estado final retornando falso, se nao tem mais palavras vai para o estado final retornando verdadeiro
Estado final:
Retorna um resultado

"""
def automato3(texto):
    sentencas = texto.split('!')
    for sentenca in sentencas:
        if(automato2(sentenca)):
            continue
        else:
            return False
    return True




print("EXEMPLO DE AUTOMATO VERIFICADOR DA LINGUAGEM PIPOCA!\n")
print("Digite seu codigo abaixo:\n")
entrada = input()
resutado = automato3(entrada)
if resutado:
    print("O seu codigo funciona!")
else:
    print("O seu codigo não funciona!")










