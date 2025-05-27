import rsa

def encode(mensagem): # Função de encode
        
        # Chamoa  função StringToASCII, como o nome já diz, eu traformo cada char em ascii
        # Essa função vai pegar cada caractere, transformar em um int e coloca ele dentro de uam lista
        letrasASCII = []
        rsa.StringToASCII(mensagem, letrasASCII)

        p = 999999999989 # Chave Privada P
        q = 999999999959 # Chave Privada Q
        n = p * q # Chave Pública N
        e = 65537 # Chave Pública E

        # Chamo a função encode que transforma cada int da lista um int codificado
        # E adiciono esses ints codificados nesta lista C
        c = []
        rsa.Encode(letrasASCII, c, e, n)
        
        # Transformo essa lista de inteiros em uma string
        # Separando cada inteiro com um espaço
        palavraCodificada = ''
        for i in range(len(c)):
                palavraCodificada = palavraCodificada + str(c[i]) + ' '

        # retorno esses inteiros separados por espaços
        return palavraCodificada
