from flask import Flask, request
import requests
import decode
import encode

app = Flask(__name__)

key_a_p = 72053 # Chave Privada P de A
key_a_q = 71867 # Chave Privada Q de A
key_a_e = 65537 # Chave Publica E de A

key_b_p = 70297 # Chave Privada P de B
key_b_q = 71359 # Chave Privada Q de B
key_b_e = 65537 # Chave Publica E de B

@app.route('/webhook', methods=['POST'])
def receba():
    # Recebo uma mensagem codificada em formato json
    # Transformo ela em string e passo para a vaiável encoded
    encoded = request.json['mensagem']
    # Decodifico a mensagem com a função decode, qua usa as chaves "p", "q" e "e" de A
    decoded = decode.decode(encoded, key_a_p, key_a_q, key_a_e)
    print(f"Mensagem recebida: {decoded}")
    return {"status":"ok"}

@app.route('/send', methods=['POST'])
def enviar():
    # Recebo uma mensagem em formato json
    # Transformo ela em string e passo para a vaiável encoded
    decoded = request.json['mensagem']
    # Codifico a mensagem com a função decode, qua usa as chaves "p", "q" e "e" de B
    encoded = encode.encode(decoded, key_b_p, key_b_q, key_b_e)
    # Envio ela para o webhook do app.py
    requests.post("http://localhost:5000/webhook", json={"mensagem":encoded})
    return {"status":"sent"}

if __name__ == '__main__':
    app.run(port=5001)