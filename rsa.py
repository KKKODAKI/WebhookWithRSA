# Função recursiva para descobrir o minimo multiplo inverso
def MinMultiploInverso(r1, r2, t1, t2, totienteDeN):

    # Descubro qual o quociente de r1 por r2
    q = r1 // r2 

    # Desbro o resto da divisão de r1 por r2
    r = r1 - q * r2

    # Número temporário para descobrir o minimo multiplo inverso
    t = t1 - q * t2
    
    # Esse if é a parada da função recursiva
    # Quando o resto for 1, eu retono o número temporário
    if r == 1:
        # Se o número temporário for negativo
        # É feito totiente de N mais t (que vai ser menos pq o t é negativo)
        # Caso ele já seja positivo ele já será o minimo multiplo inverso
        # Daí nem entra no if
        if t < 0:
            t = totienteDeN + t
        return t
    
    # Eu reparei algumas coisa quando eu estava vendo as contas do minimo multiplo inverso
    # O r1 começa sendo o totiente de euler de N
    # E depois r1 recebe o valor do antigo r2
    # O r2 começa sendo o valor de e
    # E depois r2 recebe o valor de r(resto)
    # O t1 começa sendo o valor 0
    # E depois t1 recebe o antigo valor de t2
    # O t2 começa sendo o valor 1
    # E depois t1 recebe o antigo valor de t

    # Com isso eu vi que poderia ser feito uma função recursiva
    # Por isso eu retorno a chamada da função com esses valores
    return MinMultiploInverso(r2, r, t2, t, totienteDeN)

# Função para tranformar string em ascii
def StringToASCII(mensagem, letrasASCII):
    # Pego cada caractere, transaformo em ascii e salvo em uma lista
    for i in range(len(mensagem)):
        letrasASCII.append(ord(mensagem[i]))

# Função encode
def Encode(letrasASCII, c, e, n):
    # Pego os asciis de cada letra, elevo eles a e, divido por n e pego o resto
    # Salvo esses novos números em uma lista
    for i  in range(len(letrasASCII)):
        c.append((letrasASCII[i] ** e) % n)

# Função encode
def Decode(c, d, n):
    # Pego essa lista com inteiros, elevo eles a d, divido por n e pego o resto
    # Transformo esses novos ints em chars, e junto esses chars em uma string
    palavra = ''
    for i  in range(len(c)):

        # Passo 3 parâmetros, base, expoente e o mod
        # Esse pow vai retornar um número inteiro
        # Transformo esse número inteiro em uma letra
        # Junto essas letras em uma variável para formar a palavra
        palavra = palavra + chr(pow(c[i], d, n))
        
    # Retorno a palavra original
    return palavra
