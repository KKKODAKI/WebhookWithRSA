import rsa

def decode(encoded): # Função de encode

        # Pego essa string de inteiros separados por espaços
        # E coloco cada um desses inteiros em uma posição de uma lista
        c = encoded.split()

        # Trasformo essa lista de string para uma lista de ints
        for i in range(len(c)):
                c[i] = int(c[i])
        
        p = 999999999989 # Chave Privada P
        q = 999999999959 # Chave Privada Q
        n = p * q # Chave Pública N

        totienteDeN = (p - 1) * (q - 1) # Totiente de Euler do número n

        e = 65537 # Chave Pública E

        # Chamo essa função para descobrir qual o multíplo inverso
        d = rsa.MinMultiploInverso(totienteDeN, e, 0, 1, totienteDeN) # Chave Privada D
        
        # Chamo a função dencode que transforma cada int da lista em um char
        # Essa função retorna a palavra descriptografada
        return rsa.Decode(c, d, n)
