import rsa

def encode(mensagem, p, q, e): # Função de encode
        
        # Chamoa  função StringToASCII, como o nome já diz, eu traformo cada char em ascii
        # Essa função vai pegar cada caractere, transformar em um int e coloca ele dentro de uam lista
        letrasASCII = []
        rsa.StringToASCII(mensagem, letrasASCII)

        n = p * q # Chave Pública N

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
